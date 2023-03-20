#!/usr/bin/python3
#!/usr/bin/python3
n = 2022
import math
x = round(math.pi, 5)
word = "Python"
polish = "książka"
file = open("vars.txt", "w")
file.write(str(n))
file.write("\n")
file.write(str(x))
file.write("\n")
file.write(word)
file.write("\n")
file.write(polish)
file.write("\n")
file.close()
file = open("vars.txt", "r")
S = file.read()
file.close()
print(S)
input()