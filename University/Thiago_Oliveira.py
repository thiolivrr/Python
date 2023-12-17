#Exercicio Fix40

# def increase(wage):
#     print("Nome: Thiago de Sousa de Oliveira\nRA: G7695H4")
#     if wage <= 1500:
#         print(f"Seu sálario era {wage}, agora é {wage * 1.20}")
#     elif wage < 2500:
#         print(f"Seu sálario era {wage}, agora é {wage * 1.10}")
#     else:
#         print(f"Seu sálario era {wage}, agora é {wage * 1.05}")

# increase(3000)

# #Exercicio Fix41

# def factorial(n):
#     print("Nome: Thiago de Sousa de Oliveira\nRA: G7695H4")
#     for i in range(1, n):
#         n = n * i
#     print(f"O fatorial é {n}")

# factorial(10)

# #Exercicio Fix42

# def best(g1, g2, g3, g4, g5):
#     print("Nome: Thiago de Sousa de Oliveira\nRA: G7695H4")
#     grades = [g1, g2, g3, g4, g5]
#     ordered = sorted(grades)
#     print(f"A melhor nota é {ordered[-1]}")
# best(3,1,3,4,0)

# #Exercicio Fix 43

# def imc(height, weight, gender):
#     print("Nome: Thiago de Sousa de Oliveira\nRA: G7695H4")
#     imc = weight / height**2
#     if gender == "m" or "M":
#         if imc < 20:
#             print("Abaixo do peso")
#         elif imc < 25:
#             print("Peso Ideal")
#         else:
#             print("Acima do peso")
#     elif gender == "f" or "F":
#         if imc < 19:
#             print("Abaixo do peso")
#         elif imc < 24:
#             print("Peso Ideal")
#         else:
#             print("Acima do peso")
# imc(1.75, 75, "m")

# #Exercicio Fix44

def semester(name, np1, np2):
    print("Nome: Thiago de Sousa de Oliveira\nRA: G7695H4")
    m = (np1 * 4 + np2 * 6) / 10
    if m >= 9:
        print(f"{name}, você está Aprovado.\nConceito: A")
    elif m >= 7:
        print(f"{name}, você está Aprovado.\nConceito: b")
    elif m >= 3:
        print(f"{name}, você está de Exame.\nConceito: C")
    elif m >= 0:
        print(f"{name}, você está de DP.\nConceito: D")
    else:
        (f"{name}, as notas inseridas estão incorretas")
semester("Sonic", 9, 9)

# #Exercicio Fix45

authorized = "professor"
authorizedPassword = "/:`9eV_3yF3|"
def login(role, password):
    print("Nome: Thiago de Sousa de Oliveira\nRA: G7695H4")
    if role == authorized and password == authorizedPassword:
        semester("Thiago", 10, 10)
login("professor", "/:`9eV_3yF3|")


