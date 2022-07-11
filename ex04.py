def banner(a):
    if a % 2 == 0 and a > 0:
        print('| | | | | | | | | |')
    elif a % 2 != 0 and a > 0:
        print('- - - - - - - - - -')
    elif a % 2 == 0 and a < 0:
        print('. . . . . . . . . .')
    elif a % 2 != 0 and a < 0:
        print('= = = = = = = = = =')