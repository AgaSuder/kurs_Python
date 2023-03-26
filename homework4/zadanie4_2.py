#!/usr/bin/python3

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def reverse_range(L,left, right): 
    right_count = right
    for i in range(left, int(left + (right-left)/2) + 1,1): #idziemy od lewej do połowy przedziału, + 1, zeby włączyć cyfre na 6 miejscu
         tmp = L[right_count] #zapisuje tymczasową wartosć prawego elementu do podmmiany
         L[right_count] = L[i] #w prawym elemencie zapisuję lewy
         L[i] = tmp # w drugą strone
         right_count = right_count - 1 #zmniejszam licznk, żeby zamienić kolejne elementy
    return L

print(reverse_range(L, 3, 7))

def reverse_range_recursive(L,left, right): 
    if right >= left:
        tmp = L[right]
        L[right] = L[left]
        L[left] = tmp
        reverse_range_recursive(L, left + 1, right - 1) #rekursywnie wywołuje funkcje, zaweżając listę reverse_range_recursive(L, 3 ,6 ) -> reverse_range_recursive(L, 4 , 5 )
    return L
    
print(reverse_range_recursive(L, 3, 7)) #odwraca mi tę listę z powrotem (lczyli oryginalna lista)
input()