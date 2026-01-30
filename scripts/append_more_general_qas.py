import json
from pathlib import Path

outpath = Path('scripts/vikas-dataset-augmented.jsonl')
more = [
    {'messages':[{'role':'user','content':'Hey there'},{'role':'assistant','content':'Hi — how can I assist you today? Share a brief goal and I will suggest clear next steps.'}]},
    {'messages':[{'role':'user','content':'Could you provide the immediate next steps after a pilot?'},{'role':'assistant','content':'Review pilot results against defined KPIs, document learnings, and prepare a scaling plan for successful elements. Assign owners and set a 30-90 day roadmap to operationalize the wins.'}]},
    {'messages':[{'role':'user','content':'Thanks for the help — how do I follow up?'},{'role':'assistant','content':'Summarize decisions and next steps in a short email with owners and dates, then schedule a 2–4 week checkpoint. I can draft the follow-up message if you want.'}]}
]
with outpath.open('a', encoding='utf-8') as f:
    for it in more:
        f.write(json.dumps(it, ensure_ascii=False) + '\n')

# count lines
count = sum(1 for _ in outpath.open('r', encoding='utf-8'))
print('Appended', len(more), 'entries; total lines now', count)
