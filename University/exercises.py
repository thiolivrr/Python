nome = 'Thiago de Sousa de Oliveira'
ra = 'G7695H4'

print(f'Nome: {nome}\nRA: {ra}')
print(7**4)

print(f'Nome: {nome}\nRA: {ra}')
print(21424 / 89)

print(f'Nome: {nome}\nRA: {ra}')
frase = 'Boa noite, Python'
print(frase[::-1])

print(f'Nome: {nome}\nRA: {ra}')
base, altura = float(input('Qual a base do rêtangulo?')),float(input('Qual a altura do rêtangulo?'))
print(f'A área do rêtangulo é: {str(base * altura)}')

print(f'Nome: {nome}\nRA: {ra}')
aresta = float(input('Qual a aresta do quadrado?'))
print(f'Logo, a área do quadrado é {str(aresta**2)}')

print(f'Nome: {nome}\nRA: {ra}')
base_tri, altura_tri = float(input('Qual a base do triangulo?')),float(input('Qual a altura do triangulo?'))
print(f'A área do rêtangulo é: {str(base_tri * altura_tri / 2)}')

print(f'Nome: {nome}\nRA: {ra}')
v1, v2, v3, v4 = float(input('Digite o primeiro valor:')),float(input('Digite o segundo valor:')),float(input('Digite o terceiro valor:')),float(input('Digite o quarto valor:'))
print(f'A média aritmetica é {str((v1 + v2 + v3 + v4) / 4)}')

print(f'Nome: {nome}\nRA: {ra}')
celsius = float(input('Qual a temperatura em graus Celsius?'))
fahrenheit = celsius * (9/5) + 32
print(fahrenheit)
print(f'A temperatura convertida para Fahrenheit é:{str(fahrenheit)}')

print(f'Nome: {nome}\nRA: {ra}')
quantity, price = float(input('Quantos dólares? ')), float(input('Qual a cotação atual do dólar '))
print(f'O valor correspondente em reais é {str(quantity * price)}')

print(f'Nome: {nome}\nRA: {ra}')
p1, p2, p3 ,p4, p5 = float(input('Qual valor do primeiro produto?')),float(input('Qual valor do segundo produto?')),float(input('Qual valor do terceiro produto?')),float(input('Qual valor do quarto produto?')),float(input('Qual valor do quinto produto?'))
total = p1+p2+p3+p4+p5  
pagamento = float(input('Digite o valor de pagamento: '))
if pagamento > total:
    print('Seu troco é ', pagamento - total)
elif pagamento == total:
    print('Certinho, muito obrigado!')
elif pagamento < total:
    print('Opa!, ainda faltam ', total - pagamento)

print(f'Nome: {nome}\nRA: {ra}')
bolsa = float(input('Qual valor total da compra?'))
choice = input('Olá, Maria!\nComo deseja pagar? As opções são\na) A vista com 10% de desconto\nb) Parcelado em 3 vezes sem desconto\nc) Dividido em 10 vezes com juros de 5% sobre o valor total\nDigite a letra referente a sua escolha:\nApenas três opções válidas, são elas: a, b ou c ')
if choice == 'a':
    print('O total à vista com desconto é:', (bolsa - bolsa * (1/10)))
elif choice == 'b':
    print('Okay, cada parcela fica em:', bolsa / 3 ,'\nTotal de', bolsa)
elif choice == 'c':
    print('Okay, cada parcela fica em:', (bolsa + bolsa * (1/20)) / 10, '\nTotal de', bolsa + bolsa * (1/20))

print(f'Nome: {nome}\nRA: {ra}')
gasoline = float(input(('Qual o preço da gasolina por litro?')))
payment = float(input('Qual valor do pagamento?'))
print(f'Você pode abastecer {payment / gasoline} litros no seu tanque')

print(f'Nome: {nome}\nRA: {ra}')
peso = float(input('Quantos kg o prato pesa?')) 
print(f'Você deve {str((peso + (1/5)) * 23)}')

print(f'Nome: {nome}\nRA: {ra}')
year, month, day = int(input('Escreva abaixo sua idade em anos, meses e dias:\nAnos:')), int(input('Meses:')), int(input('Dias:'))
print(f'Sua idade em dias é {str(year * 365 + month * 30 + day)}')

print(f'Nome: {nome}\nRA: {ra}')
days = int(input('Quantos dias você já viveu?'))
years = int(days / 365)
months = (days - years * 365) // 30 
days = (days - years * 365 - months*30)
print(f'Você tem {str(years)} anos, {str(months)} meses e {str(days)} dias de idade')











