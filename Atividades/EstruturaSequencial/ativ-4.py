"""

Faça um Programa que peça as 4 notas bimestrais e mostre a média.

"""

nota1 = float(input("Digite sua nota do 1º Bimestre: "))
nota2 = float(input("Digite sua nota do 2º Bimestre: "))
nota3 = float(input("Digite sua nota do 3º Bimestre: "))
nota4 = float(input("Digite sua nota do 4º Bimestre: "))

media = (nota1+nota2+nota3+nota4)/4

print(f"Sua média anual foi: {media:.2f}")
