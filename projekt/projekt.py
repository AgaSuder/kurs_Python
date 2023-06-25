#!/usr/bin/python3
import pandas as pd
import statistics
import numpy as np
import matplotlib.pyplot as plt

#Plik z danymi wejściowymi
excel_file = 'dane.xlsx'


#Przygotowanie listy próbek
def prepare_sample_list(gapdh):
    sample_list = []
    for j in(0,int(len(gapdh.index) / number_of_samples)): #pętla idzie od 0 do (liczb próbek dla gapdh/liczba próbek o danym numerku)
        for i in range(1,number_of_samples + 1): #dadaje kolejny numerek do listy
            sample_list.append(i)
    return sample_list

#Funkcja która oblicza średnie z wyników
def calculate_means(data): #tylko dla gapdh
    means_list = []
    for i in range(1,number_of_samples + 1): #pierwsza pętla dla kolejnych numerów próbki
        tmp_mean = 0; #tymczasowa średnia
        mean_counter = 0; #licznik potrzebny do obliczenia średniej
        for j in range(0,len(data.index)): #druga pętla szuka próbki o tym samym numerze, dadaje Cq z próbek i dzieli przez ilość próbek
            if i == data['Sample'][j]: #j to nr wiersza
                tmp_mean = tmp_mean + data['Cq'][j]
                mean_counter = mean_counter + 1
        tmp_mean = tmp_mean / mean_counter
        means_list.append(tmp_mean)
    return means_list;

#Funkcja obliczająca delta Cq
def calculate_deltaCq(data):
    deltaCq_list = []
    sample_number = 1
    remove_index_list = [] #żeby usunąć ze zbioru obliczone próbki, żeby dwa razy nie liczył próbki 11 i 12
    for i in range(0,len(data.index)):
        if data['Content'][i] != 'NTC' and sample_number == int(data['Sample'][i]) and sample_number < number_of_samples + 1: #wyrzucamy NTC, bo to jest woda - kontrola, czy primery do reakcji są czyste; != - ma być rózne od NTC
            deltaCq = data['Cq'][i] - cdf['gapdh_CqMean'][int(data['Sample'][i]) - 1]
            deltaCq_list.append(deltaCq)
            sample_number = sample_number + 1
            remove_index_list.append(i) #dodaje policzone próbki do listy do usunięcia
    data = data.drop(remove_index_list) #usówanie listy z obliczonymi próbkami
    data = data.reset_index() #resetowanie indeksów, żeby nie było diur w liście
    sample_number = 1 #liczy dla kolejnych próbek o tym samym numerze - próbki były mierzone przez qPCR w duplikacie
    for i in range(0,len(data.index)):
        if data['Content'][i] != 'NTC' and sample_number == int(data['Sample'][i]) and sample_number < number_of_samples + 1:
            deltaCq = data['Cq'][i] - cdf['gapdh_CqMean'][int(data['Sample'][i]) - 1]
            deltaCq_list.append(deltaCq)
            sample_number = sample_number + 1
    return deltaCq_list

#Funkcja obliczająca relatywną ekspresję
def calculate_relativeExpression(sample_name):
    relativeExpression_list = []
    name = str(sample_name) + "_DeltaCq" #tworzenie nazwy kolumny, na potrzeby obliczeń
    for i in range(0,len(cdf.index)):
        relativeEx = pow(2, -cdf[name][i]) #name to rre lub MS, a i to nr próbki
        relativeExpression_list.append(relativeEx) #dodaje kolejne wyiki do listy
    return relativeExpression_list
   
#Funkcja obliczająca średnią z próbki kontrolnej (próbka nr 1)  
def calculate_control_sample_mean(sample_name):
    control_sample_mean_list = []
    tmp_mean = 0
    mean_counter = 0
    name = str(sample_name) + "_RelativeExpression"
    for j in range(0,len(cdf.index)):
        if 1 == cdf['Sample'][j]:
            tmp_mean = tmp_mean + cdf[name][j]
            mean_counter = mean_counter + 1
    control_sample_mean_list.append(tmp_mean / mean_counter)
    return control_sample_mean_list

#Funkcja obliczająca fold change
def calculate_fold_change(sample_name):
    fold_change_list = []
    nameRelativeExpression = str(sample_name) + "_RelativeExpression" #tworzy nazwę kolumny
    nameControlSample = str(sample_name) + " control sample mean" #tworzy nazwę kolumny z próbką kontrolną
    for j in range(0,len(cdf.index)):
        fold_change = cdf[nameRelativeExpression][j] / cdf[nameControlSample][0]
        fold_change_list.append(fold_change)
    return fold_change_list

#Funkcja  obliczająca średnie ze specyficznych próbek
def calculate_sample_means(sample_name):
    mean_list = []
    name = str(sample_name) + "_fold_change"
    for i in range(1,number_of_samples + 1):
        tmp_mean = 0
        mean_counter = 0
        for j in range(0,len(cdf.index)):
            if i == cdf['Sample'][j]:
                tmp_mean = tmp_mean + cdf[name][j]
                mean_counter = mean_counter + 1
        tmp_mean = tmp_mean / mean_counter
        mean_list.append(tmp_mean)
    return mean_list

#Funkcja obliczająca odchylenia standardowe
def calculate_std(sample_name):
    std_list = []
    name = str(sample_name) + "_fold_change"
    for i in range(1,number_of_samples + 1):
        tmp_std_list = []
        for j in range(0,len(cdf.index)):
            if i == cdf['Sample'][j]:
                tmp_std_list.append(cdf[name][j])
        std_list.append(statistics.stdev(tmp_std_list))
        tmp_std_list = []
    return std_list

# "0" jest nazwą karty w escelu która jest zapisywana przez maszynę
data_frame = pd.read_excel(excel_file,"0")

#Wyszukanie tylko gapdh w arkuszu
gapdh = data_frame.loc[data_frame['Target'] == 'gapdh'] #lokalizacja i przefiltrowanie w arkuszu danych
gapdh = gapdh.reset_index() # resetuję indeksy, gdy próbki sa nie pokolei (np. brakła miejsca na płytce do PCR)
max_sample = gapdh.loc[gapdh["Sample"].idxmax()] #znajduje wiersz z ostatnim nr próbki (w tym pliku - 12)
number_of_samples = int(max_sample["Sample"]) # zapisuje max nr próbki jako liczbę całokowitą

cdf = pd.DataFrame() #tworzenie nowego arkuszu w excelu, cdf = calculations data frame
cdf['gapdh_CqMean'] = calculate_means(gapdh)

#Rozmiary kolumn się nie zgadzają więć musimy zrobić nowy DataFrame i połączyć z istniejącym. Pandas nie wspiera dodawania kolumn o różnych rozmiarach w ramach jednego DataFrame
sampledf = pd.DataFrame() #pusty data frame na numery próbek
sampledf['Sample'] = prepare_sample_list(gapdh) # przygotaowanie listy z nr próbek
cdf = pd.concat([sampledf , cdf], axis = 1) #łączy oba data frame w jeden (czyli nr próbek są obok średniej wartości Ct dla gapdh)

#Wyszukanie tylko rre w arkuszu
rre = data_frame.loc[data_frame['Target'] == 'rre'] #tworzy zbiór wierszy z rre
rre = rre.reset_index() 
cdf['rre_DeltaCq'] = calculate_deltaCq(rre) #tworzy kolumnę w arkuszu z oblicaonym deltaCq

#Wyszukanie tylko ms w arkuszu
ms = data_frame.loc[data_frame['Target'] == 'ms'] #tworzy zbiór wierszy z ms
ms = ms.reset_index()
cdf['ms_DeltaCq'] = calculate_deltaCq(ms)
    
cdf['rre_RelativeExpression'] = calculate_relativeExpression("rre")
cdf['ms_RelativeExpression'] = calculate_relativeExpression("ms")


controlsampledf = pd.DataFrame() #tworzony jest tymczasowy arkusz, bo liczba kolumn jest inna (1) niż w oryginalnym arkuszu (23) - bo liczona średnia tylko dla pierwszej próbki
controlsampledf['rre control sample mean'] = calculate_control_sample_mean("rre")
controlsampledf['ms control sample mean'] = calculate_control_sample_mean("ms")
cdf = pd.concat([cdf , controlsampledf], axis = 1) #łaczymy kolumnę z wynikami do reszty kolumn

cdf['rre_fold_change'] = calculate_fold_change("rre")
cdf['ms_fold_change'] = calculate_fold_change("ms")

#Rozmiary kolumn się nie zgadzają więć musimy zrobić nowy DataFrame i połączyć z istniejącym. Pandas nie wspiera dodawania kolumn o różnych rozmiarach w ramach jednego DataFrame
meandf = pd.DataFrame()
meandf['rre_mean'] = calculate_sample_means("rre")
meandf['ms_mean'] = calculate_sample_means("ms")
meandf['rre_std'] = calculate_std("rre")
meandf['ms_std'] = calculate_std("ms")
cdf = pd.concat([cdf , meandf], axis = 1)

#Dopisanie obliczeń do excela w nowej zakladce "Calculations"
with pd.ExcelWriter(excel_file, engine='openpyxl', mode='a', if_sheet_exists="replace") as writer:  
    cdf.to_excel(writer, sheet_name='Calculations')

#Labelki do wykresu
labels = []
for i in range(1,13):
    labels.append(i)

#Rysowanie wykresu Rre
x_pos = np.arange(len(labels)) #nr próbek na osi X
CTEs = calculate_sample_means("rre") #wartości na wykresie
error = calculate_std("rre") #odchylenie standordowe jako słupek błędu

fig, ax = plt.subplots()
ax.bar(x_pos, CTEs,
       yerr=error,
       align='center',
       alpha=0.5,
       ecolor='black',
       capsize=10)
ax.set_ylabel('fold change of reltive expression')
ax.set_xticks(x_pos)
ax.set_xticklabels(labels)
ax.set_title('Rre')
ax.yaxis.grid(True)

#Wyswietlenie oraz zapis wykresu do pliku
plt.tight_layout()
plt.savefig('rre.png')
plt.show()

#Rysowanie wykresu ms
CTEs = calculate_sample_means("ms")
error = calculate_std("ms")

fig, ax = plt.subplots()
ax.bar(x_pos, CTEs,
       yerr=error,
       align='center',
       alpha=0.5,
       ecolor='black',
       capsize=10)
ax.set_ylabel('fold change of reltive expression')
ax.set_xticks(x_pos)
ax.set_xticklabels(labels)
ax.set_title('Ms')
ax.yaxis.grid(True)

#Wyswietlenie oraz zapis wykresu do pliku
plt.tight_layout()
plt.savefig('ms.png')
plt.show()
input()