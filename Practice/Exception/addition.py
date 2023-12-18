while True:
    try:
        n1 = int(input('Enter a number: '))
        n2 = int(input('Enter a number: '))
    except ValueError:
        print("Enter a number!")
    else:
        sum = n1 + n2
        print(sum)
        break