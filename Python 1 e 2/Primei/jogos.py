import adivinhacao
import forca


print("********************************************")
print("Escolha o jogo: Adivinhação (1), Forca (2)")
print("********************************************")

gameChoice = input("Digite o número do jogo desejado:")

if gameChoice == 1:
    adivinhacao.runAdivinhacao()
elif gameChoice == 2:
    forca.runForca()