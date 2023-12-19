import os
from pathlib import Path
import json

os.chdir(r'C:\Users\Pichau\Documents\studies\Python\Practice\Files')
path = Path('number.json')
n = float(input("Enter your favorite number: "))
n = json.dumps(n)
if n in path.read_text():
    print(f"Your number is already stored, it is {n}")
else:
    path.write_text(n)
    print(f"{n} has been added")

content = path.read_text()


