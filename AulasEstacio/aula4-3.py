"""
* Criar variáveis para nome (str), idade (int), altura (float), e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = "Palloma Ruysa"
sobrenome = "Cardoso dos Santos Soares"
idade = 18
altura = 1.62
peso = 74
imc = peso / (altura**2)
anoAtual = 2021
anoNascimento = anoAtual - idade

print(f'{nome} {sobrenome}, tem {idade} anos de idade, nasceu no ano de {anoNascimento} e tem seu IMC é de {imc:.2f}'
      f' dados recolhidos no ano de {anoAtual}')
