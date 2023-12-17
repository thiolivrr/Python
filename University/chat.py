import math

# Função para calcular a quantidade de latas de 18 litros necessárias
def calcular_latas_18_litros(area):
    litros_necessarios = (area / 6) * 1.1  # Acrescentando 10% de folga
    latas_18_litros = math.ceil(litros_necessarios / 18)
    return latas_18_litros

# Função para calcular a quantidade de galões de 3,6 litros necessários
def calcular_galoes_3_6_litros(area):
    litros_necessarios = (area / 6) * 1.1  # Acrescentando 10% de folga
    galoes_3_6_litros = math.ceil(litros_necessarios / 3.6)
    return galoes_3_6_litros

# Função para calcular a mistura de latas e galões
def calcular_mistura(area):
    litros_necessarios = (area / 6) * 1.1  # Acrescentando 10% de folga
    latas_18_litros = int(litros_necessarios // 18)
    litros_restantes = litros_necessarios % 18
    galoes_3_6_litros = math.ceil(litros_restantes / 3.6)
    return latas_18_litros, galoes_3_6_litros

# Função para calcular o preço com base na quantidade de latas ou galões
def calcular_preco(latas_18_litros, galoes_3_6_litros):
    preco_latas = latas_18_litros * 80
    preco_galoes = galoes_3_6_litros * 35
    return preco_latas, preco_galoes

# Entrada do usuário
area_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Calcula as quantidades necessárias
latas_18_litros = calcular_latas_18_litros(area_pintada)
galoes_3_6_litros = calcular_galoes_3_6_litros(area_pintada)
latas_mistura, galoes_mistura = calcular_mistura(area_pintada)

# Calcula os preços
preco_latas, preco_galoes = calcular_preco(latas_18_litros, galoes_3_6_litros)
preco_mistura = (latas_mistura * 80) + (galoes_mistura * 35)

# Exibe os resultados
print(f"Quantidade de latas de 18 litros necessárias: {latas_18_litros}")
print(f"Preço das latas de 18 litros: R$ {preco_latas:.2f}")
print(f"Quantidade de galões de 3,6 litros necessários: {galoes_3_6_litros}")
print(f"Preço dos galões de 3,6 litros: R$ {preco_galoes:.2f}")
print(f"Para a mistura mais econômica:")
print(f"Quantidade de latas de 18 litros: {latas_mistura}")
print(f"Quantidade de galões de 3,6 litros: {galoes_mistura}")
print(f"Preço total da mistura: R$ {preco_mistura:.2f}")
