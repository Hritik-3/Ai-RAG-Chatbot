import json

def load_rulebook(path):
    with open(path, "r") as f:
        return [json.loads(line) for line in f] 


# Reads JSONL line by line.
# Each line becomes one Python dictionary.