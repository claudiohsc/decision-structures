def riscu(powerA, powerB):
    if powerA == powerB:
        print('Dois jogadores igualmente fracos')
    else:
        a = max(powerA, powerB)
        if a == powerA:
            print('Jogador A vence')
        else:
            print('Jogador B vence')