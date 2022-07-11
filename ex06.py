def dominos(n, m):
    tabuleiro = n * m
    if (tabuleiro % 2) == 0:
        print(int(tabuleiro / 2))
    else:
        print(tabuleiro // 2)
