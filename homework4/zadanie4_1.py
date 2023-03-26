#!/usr/bin/python3
import math

def test_unit_circle(x, y): #podpunkt a
    return math.sqrt(math.pow(x,2) + math.pow(y,2)) < 1  #obliczone ze wzoru na długość odzinka na płaszczyżnie, odległość od punktu 0,0
print(test_unit_circle(0,2)) #tu wpisać dowolne współrzędne
def test_czy_dodatnie(x, y): #podpunkt b
    return x>0 and y>0
print(test_czy_dodatnie(1,2)) #tu wpisać dowolne współrzędne

P = [[0, 1], [1, 5], [1, 2], [8, 3], [5, 3]] #podpunkt c, tutaj dane wejściowe (punkty)
print(sorted(P, key=lambda x: (-x[1], x[0]))) #-, czyli malejąco, bez minusa - rosnąco

P = [[0, 1], [1, 5], [1, 2], [8, 3], [5, 3], [-5, 3]] #podpunkt d, tutaj dane wejściowe (punkty)
print(sorted(P, key=lambda x: abs(x[0])+abs(x[1]))) #sortowanie po wartości bezwzględnej (abs) sumy x+y
input()