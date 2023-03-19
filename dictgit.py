def slovarb(dict):
    dict = {}
    a = input('enet key1: ')
    b = input('enet key2: ')
    c = input('enet key3: ')
    a1 = input('enter value1: ')
    b1 = input('enter value2: ')
    c1 = input('enter value2: ')
    dict[a] = a1
    dict[b] = b1
    dict[c] = c1
    print(dict.items())

slovarb(dict)