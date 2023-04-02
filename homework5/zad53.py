#!/usr/bin/python3
import random

def random_walk(start):
    random.seed() #initialize the random number generator
    for moves in range(0,100):
        start = start + random.choice([-1, 1]) #tworzy losowy numer -1,1
    print(start)

random_walk(0)
input()