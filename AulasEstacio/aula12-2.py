"""
Listas em Python
Fatiamento
append, insert, pop, del, clear, extend, min, max
range
"""

# texto = "Valor"
#        0  1  2  3       4            5     6
lista = [1, 2, 3, 4, "palloma ruysa", True, 10.2]
#       -7  -6 -5 -4       -3          -2    -1

# print(lista[-3])

# print(lista[0:3])
# print(lista[:3]) inicia por padrão em 0
# print(lista[3:]) termina por padrão no fim da lista
# print(lista[-1]) pegando o ultimo valor da lista
# print(lista[0]) pegando o primeiro valor da lista
# print(lista[::2]) pulando os valores da lista de 2 em 2
# print(lista[::-1]) imprime todos os elementos da lista -> só que ao contrário

# print(lista) imprime todos os elementos da lista

# for indice in lista:
#     print(indice)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
# l3 = l1 + l2 -> outra forma ->
l1.extend(l2)
# l1.extend("a") => não utiliza esse, para adicionar, e sim o "append"
# l1.append("palloma ruysa") => desse jeito só adiciona no fim da lista
# l1.insert(0, "lua") => adiciona em qualquer lugar da lista mensionado pelo indice
# l2.clear() => limpa toda a lista = []
# l2.pop() => exclui o último elemento da lista => ultimo indice
# del(l2[:2]) => deleta a sequencia colocada

# print(l1)
# print(max(l1))
# print(l2)
# print(min(l2))

l3 = list(range(1, 10))
print(l3)

l3 = list(range(0, 100, 9))
print(l3)

# soma = 0
# for valor in l2:
#     soma = soma + valor
# print(soma)

for elen in lista:
    print(f"O tipo do elemento é: {type(elen)} e o seu valor é: {elen}")
