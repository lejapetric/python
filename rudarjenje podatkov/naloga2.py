import math

#izracuna entropijo
def entropija (seznam):
    dolzina = len(seznam)
    stevci = {}
    vsota = 0

    if dolzina == 0:
        return 0
    
    for s in seznam:
        if s not in stevci:
            stevci[s] = 0
        stevci[s] += 1

    for v in stevci.values():
        delez = v / dolzina
        vsota += delez * math.log2(delez)

    return -vsota


#naredi skupine glede na izbrane atribute
def razdeli_po_atributih (podatki, atributi):
    rezultat = {}
    st_vrstic = len(podatki[atributi[0]])

    for i in range(st_vrstic):
        kljuc = []

        for z in atributi:
            kljuc.append(podatki[z][i])

        kljuc = tuple(kljuc)

        if kljuc not in rezultat:
            rezultat[kljuc] = []

        rezultat[kljuc].append(i)

    return rezultat


#izracuna utezeno entropijo
def izracunaj_tezo (razpored, razredi):
    dolzina = len(razredi)
    skupna = 0

    for indeks in razpored.values():
        podrazred = []

        for i in indeks:
            podrazred.append(razredi[i])

        skupna += len(indeks) / dolzina * entropija(podrazred)

    return skupna


#najde razred z najvec ponovitvami
def najvec_ponovitev (razpored, razredi):
    rezultat = {}

    for kljuc in razpored:
        št = {}

        for i in razpored[kljuc]:
            r = razredi[i]

            if r not in št:
                št[r] = 0

            št[r] += 1

        najboljsi = None
        naj_stevilo = -1

        for r in št:
            if št[r] > naj_stevilo or (št[r] == naj_stevilo and r < najboljsi):
                najboljsi = r
                naj_stevilo = št[r]
        rezultat[kljuc] = najboljsi

    return rezultat


#ustvari napoved
def naredi_napovedi (podatki, atributi, pravila):
    napoved = []
    st = len(podatki[atributi[0]])

    for i in range(st):
        kljuc = []

        for z in atributi:
            kljuc.append(podatki[z][i])

        kljuc = tuple(kljuc)
        napoved.append(pravila.get(kljuc))

    return napoved


#izraacuna tocnost klasifikacije
def izracunaj_tocnost (napovedi, pravi):
    pravilno = 0

    for i in range(len(napovedi)):
        if napovedi[i] == pravi[i]:
            pravilno += 1

    return pravilno / len(pravi)


######################################################################################################

def naloga2 (podatki, razredi, koraki):
    vse = list(podatki.keys())
    izbrane = []

    for _ in range(koraki):
        najmanjsa = None
        najmanjsa_vrednost = None

        for z in vse:
            tmp = izbrane + [z]
            r = razdeli_po_atributih(podatki, tmp)
            e = izracunaj_tezo(r, razredi)

            if najmanjsa_vrednost is None or e < najmanjsa_vrednost:
                najmanjsa = z
                najmanjsa_vrednost = e

        if najmanjsa is not None:
            izbrane.append(najmanjsa)
            vse.remove(najmanjsa)

    skupine = razdeli_po_atributih(podatki, izbrane)
    teza = izracunaj_tezo(skupine, razredi)
    ponovitev = najvec_ponovitev(skupine, razredi)
    napovedi = naredi_napovedi(podatki, izbrane, ponovitev)
    tocnost = izracunaj_tocnost(napovedi, razredi)

    return round(teza, 5), round(tocnost, 4)
