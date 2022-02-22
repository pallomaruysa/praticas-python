"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada
por aluno e apresentar:
       - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
       - A mensagem "Reprovado", se a média for menor do que sete;
       - A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

nota1 = input("Digite sua primeira nota parcial: ")
nota2 = input("Digite sua segunda nota parcial: ")

if not nota1.isnumeric() and not nota2.isnumeric():
    print("O valor digitado não é válido!")

nota1 = float(nota1)
nota2 = float(nota2)

media = (nota1+nota2)/2

if media == 10:
    print("\nAprovado com Distinção!")
elif media >= 7:
    print("\nAprovado!")
else:
    print("\nReprovado!")
