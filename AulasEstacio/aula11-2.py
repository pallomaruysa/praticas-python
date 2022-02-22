"""
Interando strings com while
"""

#   Índices
#   0123456789.........................33

frase = "o rato roeu a roupa do rei de Roma" # interavél
length_frase = len(frase)
print(frase[5])
print(length_frase)

cont = 0
# while cont < 34:
#     print(frase[cont])
#     cont += 1

nova_string = ''
input_usuario = input("Qual letra você deseja colocar em maiúsculo? ")

# Interação <- Interar
while cont < length_frase:
    print(frase[cont], cont)
    letra = frase[cont]
    if letra == input_usuario:
        nova_string += input_usuario.upper()
    else:
        nova_string += letra
    cont += 1

print(nova_string)

# while cont < 10:
#     print(cont)
#     cont += 1
