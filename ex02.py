def area(a, b, c):
    if c == 'losango':
        print(f'O {c} tem {int((a*b)/2)} de area')
    elif c == 'retangulo':
        print(f'O {c} tem {int(a*b)} de area')
    else:
        print(f'O {c} tem {round((a*b)/2)} de area')
    
