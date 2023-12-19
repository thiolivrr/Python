import os
from pathlib import Path
import json
#PAREI NA PAGINA 244 DO LIVRO
os.chdir(r'C:\Users\Pichau\Documents\studies\Python\Practice\Files')
path = Path('users.json')
first_name = input("Enter your first name: ")
middle_name = input("Enter your middle name: ")
last_name = input("Enter your last name: ")
first_name = json.dumps(first_name)
middle_name = json.dumps(first_name)
last_name = json.dumps(first_name)
user = {
    'first name': first_name,
    'middle name': middle_name,
    'last name': last_name
}
user = json.dumps(user)
print(user)
path.write_text(user)
content = path.read_text()