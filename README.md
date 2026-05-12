# Repozitorij Python Algoritmov - Akademska Zbirka

## Pregled Repozitorija

Ta repozitorij vsebuje celovito zbirko naprednih algoritmov in računskih tehnik, implementiranih v Pythonu kot del akademskega študija računalništva in informacijskih znanosti. Vsak projekt predstavlja praktično implementacijo temeljnih konceptov iz področij stiskanja podatkov, varnostnega kodiranja, rudarjenja podatkov in obdelave slik.

## Akademski Kontekst

Implementacije so bile razvite kot sestavni del študija na naslednjih področjih:

### Glavne Discipline
- **Stiskanje podatkov** - Brezizgubno stiskanje z algoritmom BPE (Byte Pair Encoding)
- **Varnostno kodiranje** - Hammingovi kodi, SEC-DED, CRC za odkrivanje napak
- **Rudarjenje podatkov** - Odločitvena drevesa, entropija, klasifikacija
- **Obdelava slik** - Fourierova transformacija, visokoprepustni filtri, zaznavanje robov

---

## Katalog Projektov

### 1. Naloga 1: Stiskanje podatkov z BPE (naloga1.py)

**Problem:** Brezizgubno stiskanje podatkov z algoritmom kodiranja bajtnih parov (Byte Pair Encoding)

**Algoritem:**
- Iterativno združevanje najpogostejših parov znakov
- Slovar z največ 4096 vnosi (12-bitni indeksi)
- Kodiranje ASCII znakov v indekse

**Funkcionalnost:**
- `kodiranje(vhod)` - zakodira vhodno sporočilo
- `dekodiranje(vhod, vhodS)` - odkodira sporočilo s slovarjem
- Izračun kompresijskega razmerja R

**Vhod:** Seznam znakov (ASCII) ali indeksov, seznam slovarja
**Izhod:** Zakodirano/odkodirano sporočilo, slovar, kompresijsko razmerje

---

### 2. Naloga 2: Rudarjenje podatkov – Odločitvena drevesa (naloga2.py)

**Problem:** Gradnja poenostavljenega odločitvenega drevesa za klasifikacijo podatkov

**Algoritem:**
- Izbiranje značilk z minimalno uteženo entropijo
- Razdeljevanje podatkov glede na vrednosti izbranih značilk
- Določanje razredov po večinskem glasovanju

**Metrike:**
- Entropija: `H(R) = -Σ p(r_i) log₂ p(r_i)`
- Utežena povprečna entropija za vrednotenje značilk
- Točnost: delež pravilno uvrščenih zapisov

**Vhod:** Slovar značilk, seznam razredov, število korakov
**Izhod:** Povprečna entropija, točnost (zaokrožena na 4-5 decimalk)

**Dodatna naloga (naloga2tekma):**
- Diskretizacija realnih vrednosti značilk
- Gradnja drevesa s per-značilno izbiro po vejah
- Napovedovanje za testno množico

---

### 3. Naloga 3: Varnostno kodiranje (naloga3.py)

**Problem:** Odkrivanje in popravljanje napak z razširjenim Hammingovim kodom (SEC-DED) in CRC

**Komponente:**

#### Razširjeni Hammingov kod (SEC-DED)
- Dolžina kodne besede: n = 2^m
- Število podatkovnih bitov: k = n - m - 1
- Matrika H za preverjanje sodnosti
- Popravljanje enojnih napak, odkrivanje dvojnih

#### Pravila dekodiranja:
| Pariteta p | Sindrom s | Dogodek | Akcija |
|------------|-----------|---------|--------|
| 0 | =0 | Brez napak | Vrni podatkovne bite |
| 0 | ≠0 | Dvojna napaka | Vrni -1 |
| 1 | =0 | Napaka na pariteti | Vrni podatkovne bite |
| 1 | ≠0 | Enojna napaka | Popravi in vrni |

#### CRC-8/LTE
- Polinom: 0x9B (p⁸ + p⁷ + p⁴ + p³ + p + 1)
- Začetna vrednost registra: 0x00
- Izhod: dvočrkovni šestnajstiški niz

**Vhod:** Seznam bitov (0/1), dolžina kodne besede n
**Izhod:** Odkodirano sporočilo, CRC vrednost

---

### 4. Naloga 4: Odkrivanje robov v slikah z DFT (naloga4.py)

**Problem:** Zaznavanje robov v slikah z uporabo diskretne Fourierove transformacije

**Postopek:**
1. 2D DFT vhodne slike
2. Premik Fourierove predstavitve v središče (fftshift)
3. Ustvarjanje visokoprepustnega filtra
4. Množenje s filtrom v Fourierovi domeni
5. Obratni premik (ifftshift)
6. Inverzna DFT (ifft2)
7. Odstranjevanje anomalij (realni del, clip na [0,256])

**Visokoprepustni filter:**
```
H(n,m) = 1, če (n/N)² + (m/M)² ≥ h²
         0, drugače
```

**Merjenje podobnosti – Medsebojna informacija (MI):**
```
MI = H(SV) + H(SO) - H(SV, SO)
```
Kjer je H entropija, računana iz histogramov sivin (256 binov)

**Vhod:** Matrika slike (numpy array), prag filtra
**Izhod:** Medsebojna informacija (float)

---

## Tehnološki Sklad

| Komponenta | Specifikacija |
|------------|---------------|
| **Programski jezik** | Python 3.12 |
| **Dovoljeni paketi** | Standardna knjižnica, numpy |
| **Omejitve** | Brez zunanjih paketov (PIL, matplotlib, scipy itd. niso dovoljeni) |

### Dovoljene numpy funkcije:
- `fft.fft2`, `fft.ifft2`, `fft.fftshift`, `fft.ifftshift`
- `np.ogrid`, `np.clip`, `np.histogram`, `np.histogram2d`
- `np.log2`, `np.sum`, matrične operacije

---

## Metodologija Razvoja

### Načelo Delovanja
1. **Teoretično ozadje** - Matematična osnova vsakega algoritma
2. **Implementacija** - Praktična kodna izvedba
3. **Validacija** - Testiranje s primeri (JSON datoteke)
4. **Analiza** - Empirično merjenje zmogljivosti (omejitev 15-30s)

### Standardi Kode
- Funkcijski prototipi po navodilih nalog
- Uporaba numpy za numerične operacije
- Obdelava robnih primerov (prazni seznami, ničelne matrike)
- Natančnost: odstopanje ≤ 10⁻⁴ za entropije, 10⁻⁶ za R

---

## Navodila za Uporabo

### Priprava okolja
```bash
# Zahtevane komponente
- Python 3.12+
- numpy paket

# Namestitev numpy
pip install numpy
```

### Zagon projektov

Vsaka datoteka vsebuje glavno funkcijo, ki se kliče s testnimi primeri:

```python
# Primer za nalogo 1
from naloga1 import naloga1
izhod, izhodS, R = naloga1(vhod, vhodS)

# Primer za nalogo 2
from naloga2 import naloga2
entropija, tocnost = naloga2(znacilke, razredi, koraki)

# Primer za nalogo 3
from naloga3 import naloga3
izhod, crc = naloga3(vhod, n)

# Primer za nalogo 4
from naloga4 import naloga4
MI = naloga4(slika, prag)
```

### Testiranje

Priložene so testne funkcije:
- `test_naloga1.py` - testiranje BPE kodiranja/dekodiranja
- `test_naloga2.py` - testiranje odločitvenega drevesa
- `test_naloga3.py` - testiranje Hammingovega koda in CRC
- `test_naloga4.py` - testiranje zaznavanja robov

Testni primeri so v JSON datotekah:
```bash
python test_naloga1.py
```

---

## Omejitve Izvajanja

| Naloga | Časovna omejitev | Posebnosti |
|--------|------------------|------------|
| Naloga 1 | 30 sekund | Največ 4096 vnosov v slovar |
| Naloga 2 | 30 sekund | Do 500.000 zapisov |
| Naloga 3 | 15 sekund | Do 500.000 bitov, n ≤ 256 |
| Naloga 4 | 30 sekund | Poljubna velikost slike |

---

## Akademske Kompetence

Skozi razvoj teh projektov so pridobljene naslednje kompetence:

### Teoretično razumevanje
- Informacijska teorija (entropija, medsebojna informacija)
- Fourierova analiza (DFT, frekvenčni filtri)
- Teorija kodiranja (Hammingovi kodi, CRC, SEC-DED)
- Strojno učenje (odločitvena drevesa, klasifikacija)

### Praktične sposobnosti
- Obdelava slik v frekvenčni domeni
- Implementacija brezizgubnega stiskanja
- Odkrivanje in popravljanje napak
- Gradnja klasifikacijskih modelov

### Inženirske veščine
- Učinkovita uporaba numpy za numerične izračune
- Optimizacija za časovne omejitve
- Obdelava robnih primerov
