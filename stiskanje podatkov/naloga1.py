import json
import os
from collections import Counter

MAX_DOLZINA = 4096


# KODIRANJE---------------------------------------------------------------------------------------------------------------------------------------------------------------
def kodiranje(vhod: list) -> tuple[list, list, float]:

    tabela = list(range(256))  
    vhod = list(map(ord, vhod))
      
    dolzina = len(vhod)

    while len(tabela) < 4096:

        frekvence = {}

        for i in range(len(vhod) - 1):
            par = (vhod[i], vhod[i + 1])
            frekvence[par] = frekvence.get(par, 0) + 1

        if not frekvence:
            break

        najpogostejši_par = max(frekvence, key = frekvence.get)
        if frekvence[najpogostejši_par] < 2:
            break

        #par dodam v tabelo
        tabela.append(najpogostejši_par)
        indeks = len(tabela) - 1

        #par -> stevilo iz tabele
        i = 0
        nov_vhod = []

        while i < len(vhod):

            if i < len(vhod) - 1 and (vhod[i], vhod[i + 1]) == najpogostejši_par:
                nov_vhod.append(indeks)
                i += 2
            else:
                nov_vhod.append(vhod[i])
                i += 1

        vhod = nov_vhod

    #seznam za pare
    tabela = [f"[{pair[0]}, {pair[1]}]" if isinstance(pair, tuple) else str(pair) for pair in tabela]

    izhodS = tabela
    izhod = vhod

    R = (dolzina * 8) / (len(izhod) * 12) if len(izhod) > 0 else float('nan')

    print(izhodS)
    print(R)

    return izhod, izhodS, R  



# DEKODIRANJE---------------------------------------------------------------------------------------------------------------------------------------------------------------
def dekodiranje(vhod: list, vhodS: list) -> tuple[list, list, float]:

    tabela = vhodS
    dolzina = len(vhod)

    i = len(tabela) - 1

    while i > 255:
        new_vhod = []

        for x in vhod:

            if isinstance(tabela[x], (tuple, list)):
                new_vhod.extend(tabela[x]) 
            else:
                new_vhod.append(tabela[x])  

        vhod = new_vhod
        i -= 1

    #stevilke -> znaki
    izhod = [chr(i) for i in vhod] 
    izhodS = []

    R = (len(izhod) * 8) / (dolzina * 12) if len(vhod) > 0 else float('nan')

    return izhod, izhodS, R


# Naloga1 - Funkcija za obdelavo podatkov
def naloga1(vhod: list, vhodS: list) -> tuple[list, list, float]:
    izhod = vhod[:]
    izhodS = []

    # če vhodS ni prazen, izvajamo DEKODIRANJE
    if vhodS:  
        return dekodiranje(vhod, vhodS)  
    else:
        return kodiranje(vhod)  
