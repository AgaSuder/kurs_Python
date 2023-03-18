#!/usr/bin/python3
n = 2022
import math
import open
x = round(math.pi, 5)
word = "Python"
polish = "książka"
file = open("vars.txt", "w")
file.write(n)
file.write("\n")
file.write(x)
file.write("\n")
file.write(word)
file.write("\n")
file.write(polish)
file.write("\n")
S = file.read() 
file.close()
print(S)
input()