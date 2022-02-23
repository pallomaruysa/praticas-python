"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""

print("Digite seu usuário. Ex.: fulanociclano@gmail.com")
usuario = input("usuário: ")

while True:
    senha = input("senha: ")

    if senha == usuario:
        print("\nSua senha não pode ser igual ao seu usuário! Por favor, digite sua senha novamente.")
    else:
        break
