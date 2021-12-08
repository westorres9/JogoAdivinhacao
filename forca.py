
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca***!")
    print("*********************************")

    palavra_secreta = "abacaxi".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]


    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    #enquanto true e true
    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute =chute.strip().upper()

        if(chute in palavra_secreta):
            i=0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[i] = letra
                    print(f'Encontrei a letra {chute} na posicao {i}')

                i += 1
        else:
            erros += 1


        enforcou = erros == len(palavra_secreta)
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Voce ganhou")
    else:
        print("Voce perdeu")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()