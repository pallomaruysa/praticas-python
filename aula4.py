"""
Variaveis

iniciar com letra, pode conter numeros, separar com letras maisculas camelCase
"""

nome = "Palloma Ruysa"
sobrenome = " Cardoso dos Santos Soares"
idade = 18
altura = 1.62
e_maior = idade >= 18
peso = 74

print('Nome: ', nome)
print('Sobrenome: ', sobrenome)
print('Idade: ', idade)
print('Altura: ', altura)
print('É maior de idade? ', e_maior)
print('Idade x Altura',idade * altura)

print("\n \t\t\t\t\t\t\t\tCalculando o meu IMC")

'''
divide-se o peso do paciente pela sua altura elevada ao quadrado.
'''
imc = peso / (altura**2)
print(nome+" "+sobrenome+", tem "+str(idade)+" anos de idade"+" e seu IMC é: "+str(imc))


