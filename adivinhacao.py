print('bem-vindo ao jogo de adivinhação', sep='', end='\n')
print('**************************************************', end='\n')




dificult = input('Deseja jogar no modo Facil (digite 1), normal (digite 2) ou dificil (digite 3)?')

if(int(dificult) == 2):

    chute = input('Digite o valor que você acredita ser o correto, somente inteiros. \n')
    correctValue = 72
    correctAnswer = 0


    while(int(chute) != correctValue):
        correto = int(chute) == correctValue
        maior = int(chute) > correctValue
        menor = int(chute) < correctValue
        if(correto):
            print('Parabéns, você acertou a resposta e ganhou 1 milhão de reais!!')
            break
        else:
            print('Uma pena!, Você errou, tente novamente! \n')
            if(maior):
                print('O Valor dito é Maior que o valor secreto')

            elif(menor):
                print('O valor dito é Menor que o valor secreto')

            chute = int(input('Digite o valor que você acredita ser o correto, somente inteiros. \n'))
elif(int(dificult)==1):

    '--------------------------------------------------------------------------------'
    'Jogo no caso de rodadas limitadas'
    '--------------------------------------------------------------------------------'

    tentativas = 5
    acerto = 0
    valorSecreto = 52

    print('Você possui ' + str(tentativas) + ' tentativas restantes \n')



    'while(tentativas > 1 and acerto == 0):'
    for nrodadas in range(1, tentativas+1):
        print('Você possui {} de {} tentativas restantes \n'.format(nrodadas, tentativas))
        chute = input('Digite o valor que deseja chutar \n')

        if (int(chute) < 1 or int(chute) > 100):
            print('Digite o número de 1 a 100')
            continue

        else:
            if(valorSecreto == int(chute)):
                print('Parabéns você acertou a resposta, acaba de ganhar 1 milhão de reais!!')
                break
            elif(valorSecreto != int(chute)):

                'tentativas = tentativas - 1'

                print('Infelizmente você errou a questão tente novamente \n *****************************')









