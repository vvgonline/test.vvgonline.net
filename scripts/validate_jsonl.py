#!/usr/bin/env python3
"""
JSONL Validator - Checks digital consulting dataset quality
"""

import sys
import json
import argparse
from pathlib import Path

def validate_jsonl(file_path, strict_mode=True):
    """Validate JSONL file for consulting dataset"""
    
    errors = []
    warnings = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.rstrip('\n')
            
            # Skip empty lines
            if not line:
                continue
            
            try:
                # Parse JSON object
                obj = json.loads(line)
                
                # Required fields check
                required = ['question', 'answer']
                if strict_mode:
                    # Optional auto-added fields
                    optional = ['topic', 'key_metric']
                else:
                    optional = []
                
                missing = [f for f in required if f not in obj]
                if missing:
                    errors.append(f"Line {line_num}: Missing fields - {', '.join(missing)}")
                    continue
                
                # Answer content validation
                answer = obj['answer']
                if len(answer) > 400:  # Max answer length
                    warnings.append(f"Line {line_num}: Answer too long ({len(answer)} chars). Limit: 400")
                elif '\n' in answer or '```' in answer:
                    errors.append(f"Line {line_num}: Contains newlines or codeblocks: {answer[:80]}...")
                
                # Word count for answers
                words = len(answer.split())
                if words < 30 and strict_mode:
                    warnings.append(f"Line {line_num}: Answer too short ({words} words). Minimum: 30")
                
            except json.JSONDecodeError as e:
                errors.append(f"Line {line_num}: JSON error at position {e.pos or 0}: {e.msg}")
            except KeyError as e:
                errors.append(f"Line {line_num}: Missing key: {e.args[0]}")
    
    # Generate report
    if errors:
        print(f"❌ Found {len(errors)} errors in {file_path}")
        for err in errors:
            print(f"  - {err}")
        return False
    elif warnings:
        print(f"⚠️ Found {len(warnings)} potential issues:")
        for warn in warnings:
            print(f"  - {warn}")
        return False
    else:
        print(f"✅ {file_path} is valid!")
        return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="JSONL file to validate")
    parser.add_argument("--strict", action="store_true", 
                       help="Enable strict validation mode")
    args = parser.parse_args()
    
    validate_jsonl(args.file, args.strict)