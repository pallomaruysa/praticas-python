"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto.",
se tiver entre 5 e 6 letras escreva "Seu nome é normal.", maior que 6 letras escreva "Seu nome é muito grande."
"""

print("\n\t\t\t\t\t\t\tPrograma para identificar o tamanho de seu nome (curto / médio / grande)")
nome = input("\nDigite seu primeiro nome apenas: ")

tamanho = nome.__len__()

if nome.isnumeric():
    print("Digite um valor válido!")
elif tamanho < 3:
    print("Quantidade de letras insuficinete para formar um nome!")
elif 3 <= tamanho <= 4:
    print("Seu nome é curto!")
elif 5 <= tamanho <= 6:
    print("Seu nome é normal.")
else:
    print("Seu nome é muito grande.")

