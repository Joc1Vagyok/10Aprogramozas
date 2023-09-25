# Adatszerkezet inicializálása
eladasok = [0] * 10

# 1. feladat: Feltöltés 0-9 közötti számokkal
def feltoltes_adatszerkezetbe():
    for i in range(10):
        eladasok[i] = i

# 2. feladat: Összes eladás kiírása
def osszes_eladas():
    return sum(eladasok)

# 3. feladat: Heti eladás kiírása
def heti_eladas(het):
    return eladasok[het]

# 4. feladat: Legsikeresebb hét
def legsikeresebb_het():
    return eladasok.index(max(eladasok))

# 5. feladat: Eladás mentes napok
def eladasmentes_napok():
    return eladasok.count(0)

# 6. feladat: Legkevesebb páratlan számú eladás
def legkevesebb_paratlan_eladas_nap():
    min_paratlan = min(eladasok[1::2])  # Csak páratlan napok
    return eladasok.index(min_paratlan)

# Teszteljük a függvényeket
feltoltes_adatszerkezetbe()
print("Összes eladás:", osszes_eladas())
print("Heti eladás (hét 4):", heti_eladas(4))
print("Legsikeresebb hét:", legsikeresebb_het())
print("Eladás mentes napok:", eladasmentes_napok())
print("Legkevesebb páratlan eladás nap:", legkevesebb_paratlan_eladas_nap())
