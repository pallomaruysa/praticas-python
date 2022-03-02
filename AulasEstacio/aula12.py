"""
For
Interando Strings com for
                        FATIAMENTO
Função range(start = 0, stop, step=1) => PADRÃO!

"""

texto = "Python"

# c=0
# while c < len(texto):
#     print(texto[c])
#     c += 1

# for letra in texto:
#     print(letra)

# for num in range(10):
#         print(num)
#
# for num in range(2, 10):
#         print(num)

# for num in range(0, 100, 10):
#         print(num)

# for num in range(20, 9, -1):
#         print(num)

# # multiplos de um numero
# for num in range(0, 100, 8):
#         print(num)

# multiplos de um numero
for num in range(100):
        if num % 8 == 0:
              print(num)

nova_string = ""

for letra in texto:
        if letra == "t":
                nova_string = nova_string + letra.upper()
        elif letra == "h":
                nova_string += letra.upper()
        else:
                nova_string += letra
print(nova_string)

# continue - pula para o próximo laço
# break - termina laço
