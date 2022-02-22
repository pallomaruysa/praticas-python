num1 = (input("Digite um número: "))
num2 = input("Digite um número: ")
num3 = input("Digite um número: ")
num4 = input("Digite um número: ")

# num2 = int(num2)  # Unresolved attribute reference 'isdigit' for class 'int'
#
#
# soma = num1+num2
# subi = num1-num2
# multi = num1*num2
# divi = num1/num2
# print(f'\nSoma: {soma}')
# print(f'Subtração: {subi}')
# print(f'Multiplicação: {multi}')
# print(f'Divisão: {divi}')
#
# print(num3.isdigit())
# print(num4.isdigit())

try:
    num1 = float(num1)
    num2 = float(num2)
    print(num1+num2)
except:
    if num3.isdigit() and num4.isdigit():
        num3 = int(num3)
        num4 = int(num4)
        print('Verdadeiro. Soma:', num3+num4)
    else:
        print('Por favor, digite um valor válido!')
