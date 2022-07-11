def formamisteriosa(a, b, c):
    if a == b:
        print('pode ser quadrado')
    if a > b or b > a:
        print('pode ser retangulo')
    
    if (a + b) > c and (a+b) > c and (b+c)>a:
        if a != b and b != c and a != c:
             print('pode ser triangulo escaleno')
        if (a == b and c != a) or (c == a and b != a):
            print('pode ser triangulo isosceles')
        if a == b and a== c and b == c:
            print('pode ser triangulo equilatero')
    