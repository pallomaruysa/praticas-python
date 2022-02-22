"""
 len = contador de caracteres em uma string
"""

usuario = input("Digite seu usuário: ")

qnt_caracteres = len(usuario)
print(usuario, qnt_caracteres, type(qnt_caracteres))

if qnt_caracteres < 6:
    print("Você precisa digitar pelo ou menos 6 caracters. ")
else:
    print("Você entrou no sistema. ")

string1 = input('Digite algo: ')
string2 = input('Digite algo: ')

print(f"A quantidade total de caracteres digitados foi: {len(string1)+ len(string2)}")

print(len(string1))  # função
print(string1.__len__())  # método
