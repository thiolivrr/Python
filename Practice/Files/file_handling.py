import os
from pathlib import Path

#Reading

# changing current directory and finding file with path
os.chdir(r'C:\Users\Pichau\Documents\studies\Python\Practice\Files')
path = Path('learning_python.txt')

# getting all info at once
content = path.read_text()
print(content)

# line by line
for line in content.splitlines():
    line = line.replace('Python', 'C')
    print(line)

#Writing
    
guests = Path('guest_book.txt')
active = True
names = ''
while active == True:
    name = input("Qual seu nome?")
    names += f"{name}\n"
    going = input("Há mais alguém? (S/N)")
    if going.upper() == 'N':
        active = False
guests.write_text(names)




