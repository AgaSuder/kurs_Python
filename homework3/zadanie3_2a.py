#!/usr/bin/python3
for i in range(1,41): #o 1 więcej bo nawias okrągły to przediał otwarty, czyli mniejsze niż 40
    print(i)#wypisuje cyferki
    if i % 5 == 0 and i % 7 == 0: #najpierw to, bo inaczej napisze tylko, zę jest podzielne przez 5
	    print("x is divided by 5 and 7")
    elif i % 5 == 0: #czy reszta z dzielenia jest równa 0
        print("x is divided by 5")
    elif i % 7 == 0:
	    print("x is divided by 7")
    elif i == 13:
        continue #pomijanie 13
    elif i % 5 != 0 and i % 7 != 0: #!= - różne od (przeciwieństwo ==)
        print("x is not important")
input()