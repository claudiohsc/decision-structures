def quantosJantam(n, g, f, c):
    pares = 0
    if n == 0:
        print('0')
    else:
        while True:
            if g == 0:
                break
            elif f == 0:
                break
            g -= 1
            f -= 1
            pares += 1
      
        jantam = pares + c
        if jantam > n:
            print(n)
        else:
            print(jantam)