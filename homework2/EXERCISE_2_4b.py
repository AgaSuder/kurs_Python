#!/usr/bin/python3

from tabulate import tabulate
pt = [(1,"Hydrogen","H",1), (2,"Helium","He",4), (3,"Lithium","Li",7), (4,"Berilium","Be",9), (5,"Boron","B",10.8), (6,"Carbon","C",12), (7,"Nitrogen","N",14), (8,"Oxygen","O",16), (9,"Fluorine","F",19), (10,"Neon","Ne",20)]
col_names = ["No.", "Name (en)", "Symbol", "Weight (u)"]
print(tabulate(pt, headers=col_names))
input()
