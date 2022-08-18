def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letra_acertada = ["_" for letras in palavra_secreta ]

    print(letra_acertada)

    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        chute = input("Digite aqui sua letra: ")
        i = 0
        for letra in palavra_secreta:
            if chute.lower().strip() == letra.lower():
                letra_acertada[i] = letra
            i = i + 1
        print("Encontrei a letra {} no momento a forca está:  {}".format(letra, letra_acertada))

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()
