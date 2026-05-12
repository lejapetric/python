import numpy as np

def je_potenca_dveh(x):
    return (x & (x - 1)) == 0

def matrika_H(n):
    stolpci = list(range(1, n))  
    vrstice = len(bin(n - 1)) - 2  
    H = [[0 for _ in range(n - 1)] for _ in range(vrstice)]

    for i, st in enumerate(stolpci):
        bin_st = bin(st)[2:].zfill(vrstice)  
        for j, bit in enumerate(bin_st):
            H[j][i] = int(bit)  

    stolpci_potence = [i for i, v in enumerate(stolpci) if je_potenca_dveh(v)] 
    stolpci_ostali = [i for i in range(len(stolpci)) if i not in stolpci_potence]

    nov_vrstni_red = stolpci_ostali + stolpci_potence[::-1]  

    H_nova = []
    for vrstica in H:
        nova_vrstica = [vrstica[j] for j in nov_vrstni_red]
        H_nova.append(nova_vrstica)

    return np.array(H_nova), np.array(H_nova).T



def paritetni_bit(vhod: list[int]) -> int:
    p = sum(vhod) % 2 
    return p

def izracun_sindroma(vhod: list[int], Ht: np.ndarray) -> np.ndarray:
    y = np.array(vhod[:-1])  
    s = np.dot(y, Ht) % 2
    return s




def popravi_napako(vhod: list[int], s: np.ndarray, H: np.ndarray) -> list[int]:
    for i in range(H.shape[1]):  
        if np.array_equal(s, H[:, i] % 2):  
            vhod[i] ^= 1  
            return vhod
    
    return vhod



def dekodiraj(vhod: list[int], n: int) -> list[int]:
    m = int(np.log2(n))
    k = n - m - 1  

    H, Ht = matrika_H(n)
    p = paritetni_bit(vhod)
    s = izracun_sindroma(vhod, Ht)

    if p == 0 and np.all(s == 0):
        podatki = vhod[:k]
    elif p == 0 and not np.all(s == 0):
        podatki = [-1] * k
    elif p == 1 and np.all(s == 0):
        podatki = vhod[:k]
    elif p == 1 and not np.all(s == 0):
        popravljeno = popravi_napako(vhod, s, H) 
        podatki = popravljeno[:k]

    print(f"{podatki}")
    return podatki


def izracunaj_crc8_lte(vhod: list[int]) -> str:
    POLY = 0x9A        
    crc  = 0          

    for bit in vhod:
        feedback = ((crc >> 7) & 1) ^ bit
        crc = ((crc << 1) & 0xFF) | feedback
        if feedback:
            crc ^= POLY

    return f"{crc:02X}"




def naloga3(vhod: list[int], n: int) -> tuple[list, str]:
    m = int(np.log2(n))
    k = n - m - 1  
    H, Ht = matrika_H(n)

    izhod = []
    for i in range(0, len(vhod), n):
        blok = vhod[i:i + n]
        if len(blok) != n:
            continue  

        s = izracun_sindroma(blok, Ht)
        p = paritetni_bit(blok)

        if np.all(s == 0) and p == 0:
            popravljeno = blok
        elif np.all(s == 0) and p == 1:
            popravljeno = blok  
        elif not np.all(s == 0) and p == 0:
            izhod.extend([-1] * k)
            continue
        else:
            popravljeno = popravi_napako(blok, s, H)

        izhod.extend(popravljeno[:k])

    crc = izracunaj_crc8_lte(vhod)
    return izhod, crc

