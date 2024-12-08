# slouzi k vytvoreni celociselnych rozsahu (intervalu) jako objektu v Pythonu
# vytvoreni hodnoty je potreba pouzit zabudovanou funkci range()
# po pouziti funkce print standardne nevypisuje vsechny hodnoty, ale jen okrajove
rozsah = range(11)
print (rozsah)
print (type (rozsah))     #vytiskne se  range (0,11)
# Pouziti funkce range()
# Jeden argument (stop)....           range(11) => zadaná stop hodnota, 	0, 1, 2, ..., 8, 9, 10 .. 
# Dva argumenty (start/stop)....      range (2, 11) => zadane start/stop hodnoty,    2, 3,...8, 9, 10
# Tri argumenty (start, stop,step)    range (1, 11, 3) => zadane start, stop a step hodnoty 1, 4, 7, 10 
# Datovy typ range pracuje jen s celymi cisly
print(tuple(range(11)))             # interval zacina hodnotou 0 (START) a konci jednu hodnotu drive nez stop 
print(tuple(range(1, 11)))          # interval zacina jednickou (START]) a konci hodnotou 10 (STOP)
print (tuple (range(1, 11, 3)))     # interval zacina jednickou (START), konci 10 (STOP) a je po krocich 3 (STEP)
print(
    tuple(range(11)),
    tuple(range(1, 11)),
    tuple(range(1, 11, 3)),
    sep="\n"                        # vypsani nekolika hodnot v jedne funkci print() pod sebou. Pouziva se sep=' ' = > nastaveni oddelovace " ". Pokud bych potreboval ; pak pouziju ";"
)

#SMYCKA a RANGE
for cislo in range(7):
    print(cislo)

for _ in range(5):                  # v pripadech, kde pomocna promenna nebude mit vyuziti, pak je vhodne ji pojmenovat _ , aby ctenar zapisu poznal, ze se s hodnotou nebude pracovat 
    print("Vypisuji text pomoci funkce 'print\'")

