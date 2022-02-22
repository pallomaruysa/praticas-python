'''
Tipos de dados

str = strings = '' || ""

int = inteiro = positivo = negativo = neutro[0] = [1,2,3,4]
float = ponto flutuante = positivo = negativo = neutro[0] = [0.3,0.7,9.5]
bool = boleano = true || false
'''

print('palloma', type('palloma'))
print(type('palloma'))

print('10', type('10'))
print(10, type(10))

print(5.3, type(5.3))
print(type(25.23))

print(type(10 == 10))
print(10 == 10, type(10 == 10))
print(type(100 == 10))
print(100 == 10, type(100 == 10))

print('l' == 'L', type('l' == 'L'))
print('l' == 'l', type('l' == 'l'))

print('palloma', type('palloma'), bool('paulo'), bool(''))
# bool == string[vazio] == false || bool == string[cheia] == true

# type castings -> conversão de tipos de dados
print('10', type('10'), type(int('10')))
print('10', int('10'), float(10))
print('20', type('10'), int('10'), type(10), float(10), type(10.0))

