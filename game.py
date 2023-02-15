import os

numero = int(input("Escolha o número para seu oponente acertar (Entre 0 e 1000): "))
os.system('clear') or None
tent = 5
rodada = 1
while(tent > 0):
    print("Rodada", rodada, " de 5.")
    chute = int(input("Escolha um número:"))
    if(chute == numero):
        print("Parabéns, você acertou!")
        break
    else:
        if(chute > numero):
            print("Errado! Tente um número menor")
        elif(chute < numero):
            print("Errado! Tente um número maior")
        elif(tent == 0):
            print("Acabou suas chances!")
            break
    rodada += 1
    tent -= 1