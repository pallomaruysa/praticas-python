"""
IF  /   ELIF = else if    /   ELSE     +     Operadores Lógicos

and, or, not,
in e not in
"""

a = ''  # é diferente de ' ' -> o espaço é contado como espaço e não vazio -> '' == vazio -> sem nada dentro
b = 0   # é considerado como vazio para os tipos numbers

# if not a:  # nesse caso o 'not' não é usado para negação -> e sim para perguntar se está vazio(true) ou não(false)
#     print('Favor insira valor na variável A')

# ------------------------------------------------------------------
nome = 'palloma ruysa'
if 'p' in nome:  # difere p(true) de P(false)
    print("existe a letra")

nome = 'palloma ruysa'
if not 'P' in nome:  # difere p(true) de P(false)
    print("não existe a letra")
# ------------------------------------------------------------------
usuario = input("Nome de usuário: ")
senha = input("Senha de usuário: ")

usuario_bd = "nery"
senha_bd = 12345

if usuario_bd == usuario and senha_bd == senha:
    print("Você está logado no sistema")
else:
    print('Usuário ou Senha incorretos')
