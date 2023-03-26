#!/usr/bin/python3


def iter_even():   # an infinite iterator for even numbers
    i = 0
    while True:
        yield i
        i += 2

def iter_odd():   # an infinite iterator for odd numbers
    i = 1
    while True:
        yield i
        i += 2
        
def iter_power(k):   # an infinite iterator for producing powers of k
    i = 1
    while True:
        yield i
        i *= k
        
#for i in iter_power(5): # zakomentowane, po oddkomentowaniu można testować (zamienić nazwę funkcji, na odd lub even)
     #print(i, end=" ")  #odkomentować do testu
input()