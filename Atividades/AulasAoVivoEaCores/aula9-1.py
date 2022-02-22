"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""
print("\n\t\t\t\t\t\t\tPrograma para identificar se o valor digitado é par ou ímpar")
num = input("\nDigite um número: ")

try:
    num = int(num)
    if(num % 2 == 0):
        print("Esse número é par!")
    else:
        print("Esse número é ímpar!")

except:
    if(not num.isnumeric()):
        print("Digite um valor válido!")
