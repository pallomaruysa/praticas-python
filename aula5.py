"""
Input

Entrada de dados em Python
"""

# input('Qual é o seu apelido? ')

nome = input('Qual é o seu nome? ')
idade = input('Qual é a sua idade? ')
ano_nascimento = 2021 - int(idade)

print('\nNome:', nome)
print('Idade:', idade)
print('Ano Nascimento:', ano_nascimento)

print('\nO usuário digitou:', nome, 'e o tipo da variável é:', type(nome))
print(f'O usuário digitou: {idade} e o tipo da variável é: {type(idade)}')
print(f'O usuário digitou: {ano_nascimento} e o tipo da variável é: {type(ano_nascimento)}')

# casting int -> input
num1 = int(input('\nDigite um valor '))
num2 = int(input('Digite um valor '))
soma = num1+num2

print(soma)
print(num1+num2)
