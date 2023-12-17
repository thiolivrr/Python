name = 'Thiago de Sousa de Oliveira'
ra = 'G7695H4'
# numeros = [100, 20, 30, 90, 50, 60, 70, 80, 40, 100, 10]
# ordenados = sorted(numeros)
# def choice(letter):
#     file = open("ListaCompras.txt","w")
#     if letter == 'a':
#         file.write(f'Conteudo da lista: {numeros}')
#     elif letter == 'b':
#         file.write(f"A lista tem tem {len(numeros)} elementos")
#     elif letter == 'c':
#         file.write("Ordem ascendente:")
#         file.write(f"{ordenados}")
#     elif letter == 'd':
#         sem_dup = set()
#         dup = []
#         count = 0
#         for i in numeros:
#             if i in sem_dup:
#                 file.write(f"Duplicata na posicao {count + 1}")
#                 dup.append(i)
#             else:
#                 sem_dup.add(i)
#             count = count + 1
#     else:
#         file.write("Opção Inválida!\nInsira a, b, c ou d!")
#     file.write(f'\nNome: {name}')
#     file.write(f'\nRA: {ra}')
# choice('d')

# itens_compra =  ["Arroz", "Leite", "Ovos", "Feijao", "Tomate", "Kimojo"]
# def escolha(letter):
#     file = open("ListaCompras.txt", "w")
#     if letter == 'a':
#         file.write(f'Lista: {itens_compra}')
#     elif letter == 'b':
#         file.write("Itens de compra:\n")
#         for i in itens_compra:
#             file.write(f"{i}\n")
#     elif letter == 'c':
#         itens_compra.append("Óleo de canola")
#         file.write("Óleo de canola foi adicionado! Confira abaixo:\n")
#         file.write(f"{itens_compra}")
#     elif letter == 'd':
#         itens_compra.remove("Tomate")
#         file.write("Tomate foi removido, confira:\n")
#         file.write(f"{itens_compra}")
#     else:
#         file.write("Opção Inválida!\nInsira a, b, c ou d!")
#     file.write(f'\nNome: {name}')
#     file.write(f'\nRA: {ra}')
# escolha('d')

def manage(letter):
    file = open("ListaClientes.txt", 'w')
    people = {
        "Solange": {
            'Nome': 'Solange',
            'Sexo': "F",
            'Idade': 34
        },
        "Marcelo": {
            'Nome': 'Marcelo',
            'Sexo': "M",
            'Idade': 36
        },
        "João": {
            'Nome': 'João',
            'Sexo': "M",
            'Idade': 11
        },
        "Magna": {
            'Nome': 'Magna',
            'Sexo': "F",
            'Idade': 34
        },
        "Junior": {
            'Nome': 'Junior',
            'Sexo': "M",
            'Idade': 6
        },
        "Maria": {
            'Nome': 'Maria',
            'Sexo': "F",
            'Idade': 35
        },
        "Lucas": {
            'Nome': 'Lucas',
            'Sexo': "M",
            'Idade': 10
        },
        "Gabriel": {
            'Nome': 'Gabriel',
            'Sexo': "M",
            'Idade': 7
        },
        "Felipe": {
            'Nome': 'Felipe',
            'Sexo': "M",
            'Idade': 10
        },
        "Maria": {
            'Nome': 'Maria',
            'Sexo': "F",
            'Idade': 35
        }
    }
    if letter == "a":
        people = {}
        print("Digite apenas M para masculino e F para feminino, isso vai evitar um erro, thank u Teacher!")
        for i in range(10):
            nome = input(f"Qual nome da pessoa número {i + 1}?")
            sexo = input(f"Qual sexo da pessoa {i + 1}?")
            idade = input(f"Qual idade da pessoa {i + 1}?")
            people.update({f"{i}": {"Nome": f"{nome}", "Sexo": f"{sexo}", "Idade": f"{idade}"}})
        file.write(f"{people}\n")
    elif letter == "b":
        file.write("Escolhendo a letra a, você pode inserir as pessoas! Como escolheu outra, serão consideradas pessoas previamente inseridas.\n")
        males = []
        for i in people:
            if people[i]['Sexo'] == 'M':
                males.append(people[i])
        malesOrdered = sorted(males, key=lambda d: d['Idade'])
        file.write("Homens") 
        file.write(f"{malesOrdered}\n")
        females = []
        for i in people:
            if people[i]['Sexo'] == 'F':
                females.append(people[i])
        femalesOrdered = sorted(females, key=lambda d: d['Idade'])
        file.write("Mulheres: ")
        file.write(f"{femalesOrdered}\n")
    elif letter == "c":
        file.write("Escolhendo a letra a, você pode inserir as pessoas! Como escolheu outra, serão consideradas pessoas previamente inseridas.")
        males = []
        for i in people:
            if people[i]['Sexo'] == 'M':
                males.append(people[i])
        malesOrdered = sorted(males, key=lambda d: d['Idade'], reverse=True)
        file.write("\nHomens: ") 
        file.write(f"{malesOrdered}\n")
        females = []
        for i in people:
            if people[i]['Sexo'] == 'F':
                females.append(people[i])
        femalesOrdered = sorted(females, key=lambda d: d['Idade'], reverse=True)
        file.write("Mulheres: ")
        file.write(f"{femalesOrdered}")
    elif letter == "d":
        file.write("Escolhendo a letra a, você pode inserir as pessoas! Como escolheu outra, serão consideradas pessoas previamente inseridas.\n")
        file.write(f"Ordem alfabetica: {sorted(people)}\n")
    else:
        file.write("Digite a, b, c ou d apenas, please.")
    file.write(f"{name}\n")
    file.write(ra)

manage("a")