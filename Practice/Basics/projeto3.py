velocidade_maxima = 80
velocidade_atual = int(input('Qual a velocidade atual? '))

if velocidade_atual <= velocidade_maxima:
    print('Não houve multa')
elif velocidade_atual > velocidade_maxima and velocidade_atual <= velocidade_maxima +10:
    print('multa leve')
elif velocidade_atual > velocidade_maxima +11 and velocidade_atual <= velocidade_maxima +20:
    print('multa grave')
elif velocidade_atual > velocidade_maxima +20:
    print('multa gravissima')
