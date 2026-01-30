import json

def convert_txt_to_jsonl(input_file, output_file):
    dataset = []
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    current_q = ""
    current_a = ""

    for line in lines:
        line = line.strip()
        if line.startswith(("Q:", "Q ")):
            if current_q and current_a:
                dataset.append({"instruction": current_q.strip(), "output": current_a.strip()})
            current_q = line.replace("Q:", "").replace("Q ", "").strip()
            current_a = ""
        elif line.startswith(("A:", "A ")):
            current_a = line.replace("A:", "").replace("A ", "").strip()
        elif line and current_a:
            current_a += " " + line.strip()

    if current_q and current_a:
        dataset.append({"instruction": current_q.strip(), "output": current_a.strip()})

    with open(output_file, 'w', encoding='utf-8') as f:
        for entry in dataset:
            f.write(json.dumps(entry) + '\n')

    print(f"Converted {len(dataset)} pairs to {output_file}")

# Run
convert_txt_to_jsonl('digital-business-consulting-qna.txt', 'vikas_qa.jsonl')
