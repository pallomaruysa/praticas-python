"""
IF  /   ELIF = else if    /   ELSE     +     Booleanos
"""

if True:
    print("Verdadeiro.")

    num1 = 2
    num2 = 4

    print(num1+num2)
# -----------------------------------------------------------
if False:
    print("Falso.") # comentado ou não (if falso) nao executa essa linha e pula para a próxima
print('A minha expressão não é verdadeira!')

# -----------------------------------------------------------
if False:
    print("Verdadeiro.")
else:
    print("Não é Verdadeiro -> é Falso")

if not False:
    print("Verdadeiro.")
else:
    print("Não é Verdadeiro -> é Falso")

# -----------------------------------------------------------
if False:
    print("Falso.")
elif True:
    print("Agora é Verdadeiro.")
else:
    print("Não é Verdadeiro -> é Falso")

# -----------------------------------------------------------
if 2 == 5:
    print("Falso.")
elif 2 == 2:
    print("Agora é Verdadeiro.")
elif 3 == 3:
    print("Esse também é verdadeiro")
else:
    print("Não é Verdadeiro -> é Falso")

# -----------------------------------------------------------
if 2 == 5:
    print("Falso.")

elif 2 == 2:
    print("Agora é Verdadeiro.")
    nome = input("Digite o seu nome: ")
    print(f'Seu nome é: {nome}')

elif 3 == 3:
    print("Esse também é verdadeiro")

else:
    print("Não é Verdadeiro -> é Falso")