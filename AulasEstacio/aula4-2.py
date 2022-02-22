"""
Introdução e formatação de strings
"""
nome = "Palloma Ruysa"
sobrenome = " Cardoso dos Santos Soares"
idade = 18
altura = 1.62
e_maior = idade >= 18
peso = 74
imc = peso / (altura**2)

print(nome+" "+sobrenome+", tem "+str(idade)+" anos de idade"+" e seu IMC é: "+str(imc))  # concatenação
print(nome, sobrenome, ', tem ', str(idade), ' anos de idade', ' e seu IMC é: ', str(imc))  # concatenação
print(f'{nome} {sobrenome}, tem {idade} anos de idade e seu IMC é: {imc}')  # f strings
print(f'{nome} {sobrenome}, tem {idade} anos de idade e seu IMC é: {imc:.2f}')  # f strings
print('{} {}, tem {} anos de idade e seu IMC é: {}'.format(nome, sobrenome, idade, imc))  # format
print('{} {}, tem {} anos de idade e seu IMC é: {:.2f}'.format(nome, sobrenome, idade, imc))  # format
print('{0} {1}, tem {2} anos de idade e seu IMC é: {3:.2f}'.format(nome, sobrenome, idade, imc))  # format
print('{3} {2}, tem {1} anos de idade e seu IMC é: {0:.2f}'.format(imc, idade, sobrenome, nome))  # format
print('{n} {s}, tem {i} anos de idade e seu IMC é: {im:.2f}'.format(n=nome, s=sobrenome, i=idade, im=imc))  # format
