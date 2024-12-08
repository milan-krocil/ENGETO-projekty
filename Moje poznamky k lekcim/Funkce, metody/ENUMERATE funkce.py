# zabudovana funkce, jejiz ukolem je ocislovat iterovany objekt
jmena = ("Java", "C", "Rust", "Python")
print(enumerate(jmena))                   # vysledkem je <enumarate object> tzn umisteni vyvoreneho objektu
# Pro detailni vypis se musi pouzit napr funkce list (), nebo tuple()
print(tuple(enumerate (jmena)))      # vysledek je prirazene cislo : ((0, 'Java'), (1, 'C'), (2, 'Rust'), (3, 'Python'))
# Velmi casto se enumerate spojuje se smyckou, zejmena pokud je potreba pomocny index
for pismeno in enumerate("Ahoj, vsem"):    #Funkce enumerate() způsobí, že místo jednotlivých písmen, ze kterých je složený string "Ahoj, vsem", získáváš tuple.
    print(pismeno)                         # pod sebou se vytiskne (0, 'A'), v dalsim radku (1,'h') atd.
# index 0, tedy číslo přidělené od funkce (defaultně 0),index 1, tedy jednotlivé údaje z objektu.
# pokud chceme pracovat s obema indexy yvlast, pak je nutne upravit
for index, symbol in enumerate("Ahoj, vsem"):
    print (index,symbol)
    #print(f"INDEX: {index}, SYMBOL: {symbol}")
# vystupem bude:
# prvni radek   INDEX: 0, SYMBOL: A
# druhy radek   INDEX: 1, SYMBOL: h    atd.

# muj_string = "hups"
# muj_slovnik = {}

# for x, muj_slovnik[x] in enumerate(muj_string):
#    print(x, muj_slovnik[x])
muj_list_1 = [1, 2, 3, 4]
muj_list_2 = [1, 2, 3, 4]
muj_list_3 = [1, 2, 3, 4]
muj_list_4 = [1, 2, 3, 4]

for index, cislo in enumerate(muj_list_1):
    del cislo

for index, cislo in enumerate(muj_list_2):
    muj_list_2.remove(cislo)

for index, cislo in enumerate(muj_list_3[:]):
    muj_list_3.remove(cislo)

for index, cislo in enumerate(muj_list_4):
    muj_list_4.pop(index)

print(
    f"{muj_list_1=}",
    f"{muj_list_2=}",
    f"{muj_list_3=}",
    f"{muj_list_4=}",
    sep="\n"
)
klice =[]
hodnoty = []
klice_hodnoty ={}
for index, symbol in enumerate("Ahoj, vsem"):
    #print(f"INDEX: {index}, SYMBOL: {symbol}")
    hodnoty.append(symbol)
    klice.append(index)
    klice_hodnoty[index] = symbol
print(klice)
print(hodnoty)
print(klice_hodnoty)