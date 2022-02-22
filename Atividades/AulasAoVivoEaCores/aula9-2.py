"""
Faça um programa que pergunte a hora ao usuário. Baseando-se no horário descrito, exiba a saudação apropriada.
Ex: 0h-11h "Bom dia!"
"""
print("\n\t\t\t\t\t\t\tPrograma para identificar o horário e mostrar uma saudação de boas-vindas")
hora = input("\nDigite um horário. Ex: 0, 14, 20: ")

try:
    hora = int(hora)
    if 0 < hora and hora >= 24:
        print("Número fora do intervalo de horas (0h - 23h)!")
    elif hora <= 11:
        print("Bom dia!")
    elif hora < 18:
        print("Boa tarde!")
    else:
        print("Boa noite!")
except:
    if not hora.isnumeric():
        print("Digite um valor válido!")
