#!/usr/bin/python3
word=input("podaj słowo:")
print(word)
count=len(str(word)) #liczba liter
print(count)
header_line = "" #lina górna i spodnia tabelki (napisane tu, żeby było w obrębie całego programu, a nie pętli 
for i in range(1,count+1): #pętla do rysowania plusów
    header_line = header_line + '+'
    for j in range(0,3):
        header_line = header_line + '-' #pętla do rysowania minusów
header_line = header_line + '+' #brakujący + na końcu nagłówka tabelki
print(header_line)
content="" #zawartość tabelki
S=str(word) #słowo wpisane na początku
for i in range(1,count+1): #pętla do rysowania kresek pionowych
    content = content + '| '+S[i-1]+' ' #wydobycie liter ze słowa, kreska przed słowem, spacja po słowie
content = content + '|' #brakująca kreska na końcu
print(content)
print(header_line)
input()