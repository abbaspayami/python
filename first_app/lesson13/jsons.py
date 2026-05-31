import json
from pathlib import Path

data = [
    {"id": 1,"name": "ali", "salary" : "100"},
    {"id": 2,"name": "Zahra", "salary" : "200"},
    {"id": 3,"name": "Nikoo", "salary" : "150"}
]

json_str = json.dumps(data)
Path("docs/test.json").write_text(json_str)

data = Path("docs/test.json").read_text(encoding="utf-8")
result = json.loads(data)
print(result)
print(result[0]["salary"])