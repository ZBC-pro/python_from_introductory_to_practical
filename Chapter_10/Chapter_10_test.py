#10.11
import json
import pathlib
from pathlib import Path

path = Path('favorite_numbers.json')
if path.exists():
    contents = path.read_text()
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}")
else:
    number = input("Enter your favorite numbers: ")
    contents = json.dumps(number)
    path.write_text(contents)
