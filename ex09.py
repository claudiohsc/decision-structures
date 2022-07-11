def classificador(a, b, c):
    if a + b > c and a + c >  b and b + c  > a:
        print("triangulo")
        
        if a != b and b != c and c != a:
            print("escaleno")
        elif a == b or b == c or c == a:
            print("isosceles")
        
        if a == b and b == c:
            print("equilatero")
        
        if a*a == b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
            print("retangulo")
    else:
        print("gondim sendo gondim")