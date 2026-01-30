import os, json, re
from pathlib import Path

blogs_dir = Path('src/wwwroot/assets/data/blogs')
dataset_dir = Path('src/wwwroot/assets/data/dataset')
outpath = Path('scripts/vikas-dataset-augmented.jsonl')

def summarize_text(text, maxlen=300):
    text = re.sub(r"\s+"," ", text.strip())
    if len(text) <= maxlen:
        return text
    return text[:maxlen].rsplit(' ',1)[0] + '...'

entries = []

# Process blog markdown files
if blogs_dir.exists():
    for md in sorted(blogs_dir.glob('*.md')):
        try:
            raw = md.read_text(encoding='utf-8')
        except Exception:
            continue
        # title from filename or first heading
        title = md.stem.replace('-', ' ').replace('_',' ').strip()
        m = re.search(r'^#\s+(.+)', raw, flags=re.MULTILINE)
        if m:
            title = m.group(1).strip()
        summary = summarize_text(re.sub(r'#.*\n', '', raw).strip(), 400)
        # short question
        q1 = f"What is the main idea of '{title}'?"
        a1 = f"{summary.split('.')[0]}. {summary.split('.')[1] if len(summary.split('.'))>1 else ''}".strip()
        if not a1:
            a1 = summary
        # ensure 2-3 sentences
        a1_sents = re.split(r'(?<=[.!?])\s+', a1)
        a1 = ' '.join(a1_sents[:2]) if len(a1_sents)>1 else a1
        entries.append({'messages':[{'role':'user','content':q1},{'role':'assistant','content':a1}]})
        # detailed question
        q2 = f"How can a business act on the recommendations from '{title}'?"
        a2 = f"Start with a small pilot that applies the article's recommended changes, set clear KPIs, and measure results over 30-90 days. Iterate based on user feedback and analytics to scale what works." 
        entries.append({'messages':[{'role':'user','content':q2},{'role':'assistant','content':a2}]})

# Process dataset files (docs, knowledge, prompts, services)
if dataset_dir.exists():
    for root, dirs, files in os.walk(dataset_dir):
        for fname in sorted(files):
            p = Path(root) / fname
            try:
                raw = p.read_text(encoding='utf-8')
            except Exception:
                raw = ''
            short_name = fname.replace('-', ' ').replace('_',' ').split('.')[0]
            # For CSVs, create a question about how to use the data
            if p.suffix.lower() in ['.csv']:
                q = f"How can we use the dataset '{fname}' to improve digital consulting outcomes?"
                a = f"Ingest the CSV into your analytics stack or a Customer Data Platform, clean and unify identifiers, then build models or dashboards that track the key metrics in the file. Use insights to prioritize capability gaps and measure impact." 
                entries.append({'messages':[{'role':'user','content':q},{'role':'assistant','content':a}]})
            elif p.suffix.lower() in ['.json']:
                q = f"What practical steps should we take to integrate '{fname}' into our consulting workflows?"
                a = f"Validate the JSON schema, map fields to your CRM/CDP, and automate ingestion into reporting dashboards. Use the structured data to create repeatable playbooks and measure before/after effects on target KPIs." 
                entries.append({'messages':[{'role':'user','content':q},{'role':'assistant','content':a}]})
            elif p.suffix.lower() in ['.md','.txt']:
                summary = summarize_text(raw, 400)
                q_short = f"Summarize the key guidance in '{short_name}' for a leadership team."
                a_short = f"{summary.split('.')[0]}. {summary.split('.')[1] if len(summary.split('.'))>1 else ''}".strip()
                a_short_sents = re.split(r'(?<=[.!?])\s+', a_short)
                a_short = ' '.join(a_short_sents[:2]) if len(a_short_sents)>1 else a_short
                entries.append({'messages':[{'role':'user','content':q_short},{'role':'assistant','content':a_short}]})
                q_action = f"What are two immediate actions to take from '{short_name}'?"
                a_action = f"Identify a single quick-win experiment (30-90 days) and assign an owner, then instrument measurement to track impact. If successful, formalize learnings into a capability playbook." 
                entries.append({'messages':[{'role':'user','content':q_action},{'role':'assistant','content':a_action}]})

# Append to existing JSONL
if entries:
    with outpath.open('a', encoding='utf-8') as f:
        for it in entries:
            f.write(json.dumps(it, ensure_ascii=False) + '\n')

# Basic validation: count lines
count = 0
with outpath.open('r', encoding='utf-8') as f:
    for _ in f:
        count += 1
print('Appended', len(entries), 'entries; total lines now', count)
