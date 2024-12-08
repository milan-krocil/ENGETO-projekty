# KOMPREHENCE zapis
# Nejoblibenejsi prvek pro zapis pekne smycky
# Doposud jsme vytvareli prazdny objekt (napr list) a teprve pote jsme do nej pomoci metody pridavali nove hodnoty
pismena = list()
for pismeno in "Matous":
      pismena.append(pismeno)
 # komprehence zapis (vytvoreni promenne)
pismena = [pismeno for pismeno in "Matous"]    # vytvoreni listu tj nazev listu a hranate zavorky a pote pred smycku pouzit pomocnou promennou
print (pismena)

# klasický zápis smyčky
pismena = list()

for pismeno in "Matous":
    pismena.append(pismeno)
else:
    print('Klasický zápis', pismena)

# list comprehension
nova_pismena = [pismeno for pismeno in "Matous"]
print(f"List comprehension: {nova_pismena}")

#Komprehence zapis  muze byt i u slovniku = DICTIONARY COMPREHENSION
druhe_mocniny = {cislo: cislo**2 for cislo in (1, 2, 3, 4, 5)}
print(f"Dict: {druhe_mocniny}")

#Komprehence zapis  muze byt i u setu = SET COMPREHENSION. 
#entokrát máme proměnnou jmena: string a chceme získat pouze unikátní hodnoty s velkým počátečním písmenem:
jmena = {jmeno.title() for jmeno in "matous matous marek lukas jan jan".split()}
print(f"Set: {jmena}")

#Priklad, jak vypsat mesta jen s vice nez 200 000 obyvateli
mesta = {
    "Praha": 1_335_084, 
    "Brno": 382_405, 
    "Ostrava": 284_982,
    "Plzen": 175_219, 
    "Liberec": 104_261
}
nad_sto_tisic_obyv = dict()

for mesto in mesta:
    if mesta[mesto] > 200_000:
        nad_sto_tisic_obyv[mesto] = mesta[mesto]