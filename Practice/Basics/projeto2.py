import random

aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
    chute = int(input('Chute um valor de 1 a 10: '))
    if chute > aleatorio:
        print('Chute mais baixo')
        chute = int(input('Chute um valor de 1 a 10: '))
    elif chute < aleatorio:
        print('Chute mais alto')
        chute = int(input('Chute um valor de 1 a 10: '))
    elif chute == aleatorio:
        print('Você acertou!')
        acertou = True



