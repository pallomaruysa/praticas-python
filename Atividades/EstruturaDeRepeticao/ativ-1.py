"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
e continue pedindo até que o usuário informe um valor válido.
"""

while True:
    nota = float(input("Digite uma nota: "))
    if not 0 <= nota <= 10:
        print("Digite um valor válido!\n90")
    else:
        break


