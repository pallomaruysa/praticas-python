"""
Mini Calculadora -> italo
"""

while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite um outro número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 'S' or sair == 's':
        break

    if not num1.isdigit() or not num2.isdigit():
        print('Você digitou algo inválido, tente novamente.')
        continue
    #
    # num1 = float(num1)
    # num2 = float(num2)
    #
    # # + - / *
    # if operador == '+':
    #     print(num1 + num2)
    # elif operador == '-':
    #     print(num1 - num2)
    # elif operador == '/':
    #     print(num1 / num2)
    # elif operador == '*':
    #     print(num1 * num2)
    # else:
    #     print('Operador inválido.')
