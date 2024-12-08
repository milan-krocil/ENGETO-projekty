veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'
veta1 = veta.lower()                                 # Prevod na male pismena

samohlasky = 'aeiouáéíóú'
souhlasky = 'bcčdďfghjklmnňprřsštťvzžcdž'

list_sam = list (samohlasky)
list_sou = list (souhlasky)
vysledek = {}
pocet_sam = {}
pocet_souhl = {}

for finalni_cislo in veta:
    if finalni_cislo in list_sam:
        pocet_sam [finalni_cislo] = pocet_sam.get (finalni_cislo,0) + 1
    elif finalni_cislo in list_sou:
        pocet_souhl [finalni_cislo] = pocet_souhl.get (finalni_cislo,0) + 1
print (pocet_sam)
print (pocet_souhl)
pocet_samohlasek = sum(pocet_sam.values())
pocet_souhlasek = sum(pocet_souhl.values())

print ('Pocet souhlasek: ', pocet_souhlasek,'|','Pocet samohlasek: ', pocet_samohlasek)

################################################################################################
# Jine reseni ze skoly
# Zadaná proměnná
veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'

# Samohlásky & souhlásky
samohlasky = 'aeiouáéíóú'
souhlasky = 'bcčdďfghjklmnňprřsštťvzžcdž'

# Slovník s evidencí výskytu jednotlivých typů písmen
vysledek = {'souhlasky': 0, 'samohlasky': 0}

# Iterace přes zadanou proměnnou 'veta'
for pismeno in veta:
    # .. pokud znak není písmeno
    if not pismeno.isalpha():
        continue

    # .. pokud je převedený znak mezi hodnotami samohlásek
    elif pismeno.lower() in samohlasky:
        vysledek['samohlasky'] += 1
    # .. pokud je převedený znak mezi hodnotami souhlásek
    elif pismeno.lower() in souhlasky:
        vysledek['souhlasky'] += 1

# Vypiš závěrečný výstup v podobě celkového počtu samohlásek a souhlásek
print('Počet souhlásek:', vysledek['souhlasky'], '| Počet samohlásek:', vysledek['samohlasky'])




