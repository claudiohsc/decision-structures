def piscininha(x, y, w, h, a, b):
    inside = ((a<=x+h) and (a>=x) and (b<=y+h) and (b>=y))
    borda = inside and (a==x or a==x+h or b==y or b==y+w)
    if inside and not borda:
        print('Dando um tchibum')
    elif borda:
        print('So com os pezin dentro da agua')
    else:
        print('Tomando um solzin')