
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca***!")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_",]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    #enquanto true e true
    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute =chute.strip()
        i=0
        for letra in palavra_secreta:
            if(chute == letra):
                letras_acertadas[i] = letra
                print(f'Encontrei a letra {chute} na posicao {i}')
                print(letras_acertadas)
            i = i + 1



    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()