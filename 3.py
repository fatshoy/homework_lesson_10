import json
import yaml

data = {
    'a': [1, 2],
    'b': [3, 4],
    'c': [5, 6]
}

with open('file3', 'w') as f:
    json.dump(data, f)

with open('file3', 'r') as f:
    loaded = json.load(f)
    print(loaded)

