#!/usr/bin/python3

name = input("Enter your name: ")
print ( "Hello {}!".format(name) )
for char in name:
    print(char, ord(char))   # ASCII code
input("Press any key ...")   # on Windows