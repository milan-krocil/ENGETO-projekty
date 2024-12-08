# Ucelem smycky 'for' ke projit zadanou hodnotu ( pripadne hodnotu ulozenou do promenne) od prvniho udaje ay do posledmiho
muj_seznam = [1,2,3,4,5]      
print (muj_seznam [0])
print (muj_seznam [1])
print (muj_seznam [2])
print (muj_seznam [3])
print (muj_seznam [4])

#equivalentem je smycka for
for cislo in [1,2,3,4,5] :     # cislo je pomocna promenna (byva zvykem, ze se jmenuje podle obsahu v zavorkach) a je platna pouze v te konkretni smycce
                               # in rika odkud ma brat promenna jednotlive hodnoty
                               # v hranatych zavorkach se zapise, co chceme prohledat (=iterovat.). Iterace (kolo). Iterovatelny je takovy objekt, ktery lze pomoci smycky prochazet.
                               # Cele je to zakonceno dvojteckou. @    print (cislo)              # v cyklu je telo odskoceno (tab), tak jak je to u podminek

# ITERACE je mozna s datovymi typy
# 1. str
for pismeno in "abcd":
    print(pismeno)
# 2.Tuple
for pismeno in ("a", "b", "c", "d"):
    print(pismeno)
# 3. dict 
for klic in {"jmeno": "Matous", "vek": 100, "email": None}:
    print(klic)                 # vytiskne pod sebe vsechny klice
# 4. set
for symbol in {"#", "$", "%", "&"}:
    print(symbol)
# ITERACE NENI mozna pro 
# 1. int
# 2. float

# PODMINKOVY ZAPIS pro for napr pro hledani sudych cisel
suda_cisla = list()
licha_cisla = list ()
seznam_cisel = (1,2,3,4,5)
for cislo in seznam_cisel:           # vezme prvni cislo ze seznamu cisel
    if cislo % 2 == 0:               # zjisti, jestli cislo po deleni je nulove
        suda_cisla.append (cislo)    # pokud je nulove, tak ji prida metodou append do tuplu sudych cisel 
    else:
       licha_cisla.append (cislo)
print (suda_cisla)
print (licha_cisla)

# OHLASENI ve smyckach
# break  - preskoci zbytek smycky a pokracuje kodem pod ni. Vyuziti napr. pokud najdeme hledanou hodnotu nebo podminkovy zapis je True a uz NECHCI pokracovat ve smycce
# continue  - vraci se k definici smycky a pokracuje cela smycka
for pismeno in ('a','b','c','d','e'):
   if pismeno == 'c' :
      print ('nasel jsem pismeno', pismeno)
      break
   else:
      print ('Pismeno',pismeno,'neni hledane c')    # po splneni pozadavku s break se iterovani ukonci = nevytiskne se nic co je v 'else' 

for pismeno in ('a','b','c','d','e'):
   if pismeno == 'c' :
      print ('nasel jsem pismeno', pismeno)
      continue
   else:
      print ('Pismeno',pismeno,'neni hledane c')   

for pismeno in ("a", "b", "c", "d"):
    if pismeno in {"a", "b"}:
        print(pismeno)
        continue
    print("Hodnota", pismeno, "je dulezita")     # toto oznameni se vypise pro hodnoty 'c' a 'd'. V prvnim kole je podminka splnena, proto skoci zpet na smycku, ve druhem to stejne. Ve tretim podminka splena neni, proto pokracuje v kodu dale.

for pismeno in ("a", "b", "c", "d"):
    if pismeno in {"a", "b"}:
        print(pismeno)
        break
    print("Hodnota", pismeno, "je dulezita")  

for pismeno in ("a", "b", "c", "d"):
    print(pismeno.upper())                      # vse, co je v listu se vypise velkymi pismeny
else:
    print("Vsechna pismena vypsana")

for pismeno in ("a", "b", "c", "d"):
    if pismeno == "c":
        print("Nasel jsem 'c', preskakuji cyklus..")
        break
else:
    # kvůli 'break' se tento text nevypíše po ukončení smyčky
    print("Vsechna pismena vypsana")

print("Pokracuji po smycce")

# Vnorena smycka - pouziva se napr v pripadech, kdy pracujeme s nestovanymi datovymi typy napr objekty typu list v promenne jmena. 
jmena = [
    ["Matous", "Marek", "Lukas", "Jan"],
    ["Lucie", "Aneta", "Eva", "Lenka"],
    ["Helmut", "Hammet", "Hetfield", "Harold"]
]
for jmeno in jmena:
    print(jmeno)
#Smycka typu 'for' pracuje s udaji index po indexu od pocatku az na konec seznamu
# pridanim dalsi smycky budeme prochazet jednotlive indexy unvnitr kazdeho seznamu
jmena = [
    ["Matous", "Marek", "Lukas", "Jan"],
    ["Lucie", "Aneta", "Eva", "Lenka"],
    ["Helmut", "Hammet", "Hetfield", "Harold"],
]
for seznam in jmena:
      for jmeno in seznam:
        print(jmeno)
# Do proměnné seznam na začátku uloží ["Matous", "Marek", "Lukas", "Jan"] ve vnější smyčce,
# přejde k vnitřní smyčce a tady do proměnné jmeno uloží první hodnotu z výše zmíněného seznamu, tedy "Matous",
# potom bude pokračovat tak dlouho, dokud z proměnné seznam nevypíše poslední hodnotu "Jan",
# vnitřní smyčka končí a vrací se do vnější smyčky, kde do proměnné seznam nachystá hodnotu ["Lucie", "Aneta", "Eva", "Lenka"],
# celý postup se opakuje tak dlouho, dokud nevypíše Harold,nyní už nemá ve vnitřní smyčce žádnou hodnotu, vrací se do vnější smyčky, kde nastala stejná situace,
# vnější for skončí a interpret pokračuje čtením zápisu pod smyčkou (další zápis není a proto skončí).