def older(ageA, ageB):
    if ageA == ageB:
        print('Maybe twins')
    else:
        a = max(ageA, ageB)
        if a == ageA:
            print('A')
        else:
            print('B')