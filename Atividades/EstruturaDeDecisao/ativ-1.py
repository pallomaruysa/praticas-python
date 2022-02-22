"""
Faça um Programa que peça dois números e imprima o maior deles.
"""

num1 = int(input("Digite um número "))
num2 = int(input("Digite um número "))

if num1 > num2:
    print(f"O maior número é {num1}")
elif num1 == num2:
    print(f"Os números são inguais")
else:
    print(f"O maior número é {num2}")
