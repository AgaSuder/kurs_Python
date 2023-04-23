#!/usr/bin/python3
import itertools
import random

class MyInt:
    random.seed()
    def __init__(self):
        self.n = 0

    def __call__(self):
        return self.n + random.randint(0, 1)

iter1 = itertools.cycle([0,1]) # podpunkt a
iter2 = iter(MyInt(),10) #podpunkt b
iter3 = itertools.cycle([0, 1, 0, -1]) # podpunkt c

#for output in iter2:
    #print(output)
    #input()

input()