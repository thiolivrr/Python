import os
from pathlib import Path

os.chdir(r'C:\Users\Pichau\Documents\studies\Python\Practice\Exception')
def pets(*names):
    for name in names:
        path = Path(f'{name}')
        try:
            content = Path.read_text(path)
        except FileNotFoundError:
            # If i wanted to fail silently i could substitute the line below with pass
            print(f"{name} doesn't exist")
        else:
            print(content)
        
# pets('cats.txt','birds.txt', 'dogs.txt')

#Common Words
            
book = Path('random.txt')
text = Path.read_text(book)
print(text.count('sys'))