from random import choice

arr = [4, 'tyler', 'fuck', 6, 'mustang', 'sexo', 9, 2, 8, 7, 5, 2, 1, 2, 3, 'A']
mine = choice(arr)
count = 0
for i in arr:
    count += 1
    if choice(arr) == mine:
        print(f"You Win\nThe loop had to run {count} times")
        break
    else:
        print(f"Current: {choice(arr)}")