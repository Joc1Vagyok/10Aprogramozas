def szigoruan_monoton_novekvo(lista):
    for i in range(1, len(lista)):
        if lista[i] <= lista[i - 1]:
            return False
    return True

# Példa egy számlistára
szamlalista = [1, 2, 3, 4, 5]

if szigoruan_monoton_novekvo(szamlalista):
    print("A számlista szigorúan monoton növekvő.")
else:
    print("A számlista nem szigorúan monoton növekvő.")
