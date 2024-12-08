vysledek = list()
start = 3
stop = 9
delitel = 3
start1 = isinstance(start,int)
stop1 = isinstance (stop,int)
delitel1 = isinstance (delitel,int)

if start1 and  stop1 and  delitel1 :  #pokud je podminka splnena, pak se provede... jinak else
    print ('Zadane vstupy musi byt cisla')
    for cislo in range (start,stop + 1) :
        if cislo % int(delitel) == 0 :
            vysledek.append(cislo)
    print (vysledek)
    print(len(vysledek))
else:   
    print ('Zadane hodnoty musi byt cisla')

#################################################################################################
# Vysledek od skoly

# Zadaná proměnná
vysledek = []

# Zadané hodnoty: počáteční hodn., konečná hodn., dělitel
start = 3
stop = 9
delitel = 3

if isinstance(start, int) \
        and isinstance(stop, int) \
        and isinstance(delitel, int):
    print("Zadaný rozsah: <", start, ", ", stop, ">", sep="")

    # Iteruj skrze rozsah zadaných čísel
    for number in range(start, stop + 1):
        # .. pokud je vybrané číslo dělitelné hodnotou v prom. "delitel"
        if number % int(delitel) == 0:
            # .. přidej jej do seznamu "vysledek"
            vysledek.append(number)
    # doplň výpis hodnot v proměnné 'vysledek'
    print('Čísla dělitelná', delitel, ':', vysledek)

else:
    print("Zadané vstupy musí být čísla.")


