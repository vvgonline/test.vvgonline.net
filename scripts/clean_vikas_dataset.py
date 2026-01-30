import json, re
from pathlib import Path

inpath = Path('scripts/vikas-dataset-augmented.jsonl')
outpath = Path('scripts/vikas_qa_cleaned.jsonl')
report_path = Path('scripts/cleaning_report.txt')

ws_re = re.compile(r"\s+")

def normalize_text(s: str) -> str:
    if s is None:
        return ''
    s = s.strip()
    s = ws_re.sub(' ', s)
    return s

summary = {
    'total_lines': 0,
    'parsed': 0,
    'valid': 0,
    'invalid': 0,
    'duplicates': 0,
}
invalid_samples = []
seen = set()

with inpath.open('r', encoding='utf-8') as inf, outpath.open('w', encoding='utf-8') as outf:
    for lineno, line in enumerate(inf, 1):
        summary['total_lines'] += 1
        line = line.strip()
        if not line:
            summary['invalid'] += 1
            if len(invalid_samples) < 10:
                invalid_samples.append((lineno, 'empty line'))
            continue
        try:
            obj = json.loads(line)
            summary['parsed'] += 1
        except Exception as e:
            summary['invalid'] += 1
            if len(invalid_samples) < 10:
                invalid_samples.append((lineno, f'json error: {e}'))
            continue
        # Validate messages structure
        if not isinstance(obj, dict) or 'messages' not in obj:
            summary['invalid'] += 1
            if len(invalid_samples) < 10:
                invalid_samples.append((lineno, 'missing messages'))
            continue
        msgs = obj.get('messages')
        if not isinstance(msgs, list) or len(msgs) < 2:
            summary['invalid'] += 1
            if len(invalid_samples) < 10:
                invalid_samples.append((lineno, 'messages not list or too short'))
            continue
        # find first user and assistant messages
        user_text = None
        assistant_text = None
        for m in msgs:
            if not isinstance(m, dict):
                continue
            role = m.get('role','').lower()
            content = m.get('content','')
            if role == 'user' and user_text is None:
                user_text = content
            elif role == 'assistant' and assistant_text is None:
                assistant_text = content
            if user_text and assistant_text:
                break
        if not user_text or not assistant_text:
            summary['invalid'] += 1
            if len(invalid_samples) < 10:
                invalid_samples.append((lineno, 'missing user or assistant message'))
            continue
        user_text = normalize_text(user_text)
        assistant_text = normalize_text(assistant_text)
        if user_text == '' or assistant_text == '':
            summary['invalid'] += 1
            if len(invalid_samples) < 10:
                invalid_samples.append((lineno, 'empty user or assistant content'))
            continue
        sig = (user_text.lower(), assistant_text.lower())
        if sig in seen:
            summary['duplicates'] += 1
            continue
        seen.add(sig)
        # write normalized item
        out_obj = {'messages': [{'role': 'user', 'content': user_text}, {'role': 'assistant', 'content': assistant_text}]}
        outf.write(json.dumps(out_obj, ensure_ascii=False) + '\n')
        summary['valid'] += 1

# write report
with report_path.open('w', encoding='utf-8') as rf:
    rf.write('Cleaning report\n')
    rf.write('================\n')
    for k,v in summary.items():
        rf.write(f'{k}: {v}\n')
    rf.write('\nInvalid samples (up to 10):\n')
    for ln,reason in invalid_samples:
        rf.write(f'  line {ln}: {reason}\n')

print('Cleaning complete. Summary:')
for k,v in summary.items():
    print(f'  {k}: {v}')
print('Report written to', report_path)
print('Cleaned dataset written to', outpath)
