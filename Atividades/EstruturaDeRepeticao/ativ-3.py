"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""
while True:
    while True:
        nome = input("Digite seu nome: ")
        if nome.__len__() < 3:
            print("Nome muito curto! Precisa ser maior que 3 caracteres.\n")
        else:
            break

    while True:
        idade = int(input("Digite sua idade: "))
        if not 0 < idade < 150:
            print("Erro! A idade precisa estar entre 0 e 150 anos.\n")
        else:
            break

    while True:
        salario = float(input("Digite seu salário: "))
        if salario < 0:
            print("Erro! O salário precisa ser maior que R$0,00.\n")
        else:
            break

    while True:
        sexo = input("Digite seu sexo. EX.: 'f' ou 'm': ")
        if not sexo == "f" or "F" and sexo == "m" or "M":
            print("Erro! Sexo Inválido.\n")
        else:
            break

    while True:
        estadoCivil = input("Digite seu Estado Civil. EX.: 's', 'c', 'v', 'd': ")
        if not estadoCivil == "s" or "S" and estadoCivil == "c" or "C" and estadoCivil == "v" or "V" \
                and estadoCivil == "d" or "D":
            print("Erro! Estado civil Inválido.\n")
        else:
            break

    break
print(f"DADOS INFORMADOS: \n \t\t\t {nome}\n \t\t\t {idade}\n \t\t\t {salario}\n "
      f"\t\t\t {sexo}\n \t\t\t {estadoCivil}")
