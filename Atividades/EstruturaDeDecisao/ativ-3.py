"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
F - Feminino, M - Masculino, Sexo Inválido.
"""

sexo = input("Digite seu sexo [F] ou [M]: ")

if sexo == 'F' or sexo == 'f':
    print(f"{sexo} -> Seu sexo é feminino!")
elif sexo == 'M' or sexo == 'm':
    print(f"{sexo} -> Seu sexo é masculino!")
else:
    print(f"{sexo} -> Sexo inválido!")
