#!/usr/bin/python3

S = """lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(S)
c = 0 #licznik czarnych znaków
for s in S:
    if not s.isspace(): #sprawdzam, czy s nie jest białym znakiem
        c = c + 1 #zwiększenie licznika o 1
print(c)
liczba_slow=len(S.split())
print(liczba_slow)
najdlozsze_slowo=max(S.split(), key=len)
print(najdlozsze_slowo)
kolejnosc_alfabetyczna=S.split()
kolejnosc_alfabetyczna.sort()
print(kolejnosc_alfabetyczna)
dludosc_slowa=S.split()
dludosc_slowa.sort(key=len)
print(dludosc_slowa)
input()
