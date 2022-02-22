"""
IF  /   ELIF = else if    /   ELSE     +     Operadores Relacionais

==   >   >=   <   <=   !=
"""

var = "valor"

print(2 == 2)
print(2 == 3)
print(2 != 2)
print(2 != '2')
print(2 == '2')

# ------------------------------------------------------------------
num1 = 2
# num2 = "2"
num2 = 20

print(num1, num2)
print(num1 == num2)
print(num1 != num2)

expressao = num1 == num2
print(expressao)

expressao = num1 <= num2
print(expressao)

# ------------------------------------------------------------------

var2 = "palloma"

expressao = var == var2
print(expressao)

expressao = var != var2
print(expressao)

# ------------------------------------------------------------------

# nome = input("Qual é o seu nome?")
# idade = input("Qual é a sua idade?")
#
# idade_minima = 18
#
# if int(idade) >= idade_minima:  # casting
#     print(f'{nome} pode pegae o empréstimo.')
# else:
#     print(f'{nome} NÃo pode pegar o empréstimo.')

# ------------------------------------------------------------------
# nome = input("Qual é o seu nome? ")
# idade = int(input("Qual é a sua idade? "))  # casting
#
# idade_minima = 18
#
# if idade >= idade_minima:
#     print(f'{nome} pode pegar o empréstimo.')
# else:
#     print(f'{nome} NÃo pode pegar o empréstimo.')

# ------------------------------------------------------------------
nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))  # casting

idade_menor = 20
idade_maior = 50
#
# if idade >= idade_menor and idade <= idade_maior:
#     print(f'{nome} pode pegar o empréstimo.')
# else:
#     print(f'{nome} NÃo pode pegar o empréstimo.')

# ------------------------------------------------------------------ ou
if idade_menor <= idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')

else:
    print(f'{nome} NÃo pode pegar o empréstimo.')

