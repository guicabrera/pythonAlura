import random
def runForca():  
    dificuldade = defineDificuldade()
    palavraChave = defineRandomWordFromDb()
    enforcou = False
    acertou = False
    chuteTry = {1}
    tentativas = len(palavraChave[0]) + round(10/dificuldade)
    print(f"Você possui {tentativas} chutes")
    chutesCorretos = palavraChave[1]
    print("______________________________________")
    print(chutesCorretos)
    print("--------------------------------------")
    #equivalente à escrever enforcou == false and acertou == false
    #isso pq o valor de acertou é false até que o player erre todas
    #é possível verificar a primeira ocorrência de algum caracter em uma string com a função string.find(oque quero procurar)
    while(not enforcou and not acertou):
        chute = input("Digite uma letra: \n").lower().strip()
        #verifica se o item já foi chutado antes de iniciar uma tentativa
        if not chute in chuteTry:            
            #adiciona o item chutado no set de chutes chuteTry (chuteTry é um set)
            chuteTry.add(chute)
            chutesCorretos = defineAcertos(palavraChave[0],chute,chutesCorretos)        
            #verifica se ainda existem campos a serem "descobertos" pelo usuário
            print(chutesCorretos) 
            #subtrai as tentativas a cada iteração do while
            tentativas += -1
            #calcula as letras restantes
            numRest = chutesCorretos.count("_")
            verifyEndGame(tentativas, numRest, round(10/dificuldade))
            print(f"Você ainda tem {tentativas} tentativas")
            print(f"Restam {numRest} letras")
            #verifica se o usuário conseguirá chegar ao fim do jogo com suas tentativas ou se suas tentativas ainda existem
            enforcou = tentativas <= 0 or tentativas < numRest
            acertou = not "_" in chutesCorretos
            displayEndGameTrophy(acertou,enforcou,palavraChave[0])
        else:
            print("Essa Letra já foi chutada")
def verifyEndGame(tentativas, numRest, dificulty):
    forcaTrue = False
    print("  _______     ")
    print(" |/      |    ")
    if ((tentativas<numRest) or tentativas<0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
        forcaTrue = True
    if(tentativas<=dificulty*0.2 and not forcaTrue):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
        forcaTrue = True 
    if(tentativas<=dificulty*0.5 and not forcaTrue):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
        forcaTrue = True      
    if(tentativas<=dificulty*0.9 and not forcaTrue):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        forcaTrue = True

    print(" |            ")
    print("_|___         ")
    print()
def displayEndGameTrophy(acertou, enforcou, palavraChave):
    if enforcou:
        print("Puxa, você foi enforcado!")
        print(f"A palavra era: {palavraChave}")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
    if acertou:       
        print("Parabéns, você ganhou!")
        print(f"Você acertou a palavra:  {palavraChave}")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
def defineAcertos(palavraChave,chute,chutesCorretos):
    posAcerto = 0
    for letra in palavraChave:
                #define valor de incremento das posições que o chute acertou (se acertou)
                
                if(letra == chute):   
                        chutesCorretos[posAcerto] = chute                           
                posAcerto += 1 
    return chutesCorretos
def defineDificuldade():
    print("---------------------------------------------------------")
    print("Bem vindo ao jogo da forca")
    dificuldade = int(input("Escolha uma dificuldade: Fácil(1), Normal(2), Difícil(3)"))
    print("---------------------------------------------------------")
    return dificuldade
def defineRandomWordFromDb():
    #abrindo arquivo txt com frutas de palavraChave
    myFruits = []
    with open("fruits.txt","r") as myFruitsDB:
        #o for, nesse caso, irá ler cada incremento como uma linha do arquivo Txt
        for frutas in myFruitsDB:
            myFruits.append(frutas)
    #------------------------------------------------
    finalRange = random.randrange(0,len(myFruits)) # O valor precisou ser colocado em variável para não alterar no teste
    return [str(myFruits[finalRange]).lower().strip(),["_" for x in str(myFruits[finalRange]).lower().strip()]] 
if __name__ == "__main__":
    runForca()