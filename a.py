n = 5
a = 0
for i in range(1, n):
    b = ""
    while i > a:
        b += str(i)
        b = b - 1
    print(b)