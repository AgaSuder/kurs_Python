#!/usr/bin/python3
i = 1 #zaczynamy od 1
while i < 40: 
    print(i)#wypisuje cyferki
    if i % 5 == 0 and i % 7 == 0: #najpierw to, bo inaczej napisze tylko, zę jest podzielne przez 5
	    print("x is divided by 5 and 7")
    elif i % 5 == 0: #czy reszta z dzielenia jest równa 0
        print("x is divided by 5")
    elif i % 7 == 0:
	    print("x is divided by 7")
    elif i == 13:
        i=i+1 # zwiększam licznik pętli, jeśli będzie 13
        continue #pomijanie 13
    elif i % 5 != 0 and i % 7 != 0: #!= - różne od (przeciwieństwo ==)
        print("x is not important")
    i=i+1 #zwiększam licznik pętli
input()