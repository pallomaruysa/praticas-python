secreto = "perfume"
letras_digitadas = []
chances = 3

while True:
    if chances == 0:
        print('POXA... VOCÊ PERDEU!')
        break

    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("Ação não permitida! Digite uma letra por vez.")
        continue

    letras_digitadas.append(letra)
    print(letras_digitadas)

    if letra in secreto:
        print(f"Aí, TU BROCOU!! A letra {letra} existe na palavra secreta.")
    else:
        print(f"POXA... A letra {letra} não existe na palavra secreta.")
        letras_digitadas.pop()

    secreto_temporario = ""

    for letra_secreta in secreto:
        if letra_secreta in letras_digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += "_"

    if secreto_temporario == secreto:
        print(f'PARABÉNS!!! Você venceu! A palavra secreta é "{secreto}". Bom jogo :D')
        break
    else:
        print(secreto_temporario)

    if letra not in secreto:
        chances -= 1
        print(f'Você ainda tem {chances} chance(s)\n')

