import json
from pathlib import Path

inpath = Path('scripts/vikas_qa_cleaned.jsonl')
outpath = Path('scripts/vikas_qa_cleaned.jsonl')

# Patterns for conversational/greeting responses
greeting_keywords = ['hello', 'hi', 'how are you', 'can you help', 'thanks', 'thank you']
vikas_id = "I'm Vikas AI assistant from VVG ONLINE"

items = []
updated = 0

with inpath.open('r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        obj = json.loads(line)
        msgs = obj.get('messages', [])
        
        # Check if this is a greeting/conversational response
        if len(msgs) >= 2:
            user_msg = msgs[0].get('content', '').lower().strip()
            assistant_msg = msgs[1].get('content', '')
            
            # Identify greeting/conversational questions
            is_greeting = any(kw in user_msg for kw in greeting_keywords)
            
            if is_greeting and vikas_id not in assistant_msg:
                # Add the identifier organically
                if user_msg in ['hi', 'hello', 'hey there']:
                    if assistant_msg.startswith('Hello'):
                        msgs[1]['content'] = f"Hello — I'm Vikas AI assistant from VVG ONLINE. How can I help today? I'm available to provide concise advice or step-by-step actions based on your goals."
                    else:
                        msgs[1]['content'] = f"{vikas_id} — {assistant_msg[0].lower()}{assistant_msg[1:]}"
                elif 'how are you' in user_msg:
                    msgs[1]['content'] = f"I'm {vikas_id}, and I'm ready to help you with practical guidance. Tell me your priority and I will suggest an actionable plan."
                elif 'can you help' in user_msg or 'help me' in user_msg:
                    if 'I can help' in assistant_msg:
                        msgs[1]['content'] = f"I can help — {vikas_id} here. Tell me more about your goals and constraints, and I will provide a short, actionable plan."
                elif 'thanks' in user_msg or 'thank you' in user_msg:
                    if 'welcome' in assistant_msg.lower():
                        msgs[1]['content'] = f"You're welcome! {vikas_id} is glad to help. If you'd like, I can expand on any of these points or provide next steps."
                
                updated += 1
        
        items.append(obj)

# Write back to cleaned file
with outpath.open('w', encoding='utf-8') as f:
    for it in items:
        f.write(json.dumps(it, ensure_ascii=False) + '\n')

print(f'Added Vikas AI identifier to {updated} greeting/conversational responses')
print(f'Updated file: {outpath}')
