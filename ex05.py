def dinheiros(n, a, b):
    if a<(b/2):
        print(a*n)
    else:
        print(((n//2)*b) + (n%2)*a)