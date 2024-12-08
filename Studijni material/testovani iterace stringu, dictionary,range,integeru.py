#########################################
# ITERACE DICTIONARY#
########################################

programovaci_jazyk = {
    0: "P", 1: "y", 2: "t", 3: "h", 4: "o", 5: "n"
    }

for symbol in programovaci_jazyk:
    print(f"{symbol=}")

for symbol in programovaci_jazyk.values():
    print(f"{symbol=}")
   
for k, v in programovaci_jazyk.items():
    print(k, v)

#Dalsi priklad
muj_string = "hups"
muj_slovnik = {}

for x, muj_slovnik in enumerate(muj_string):
   print(muj_slovnik)

##############################################
# ITERACE RANGE
##############################################
for cislo in range(5, 0, -1):    # iterace pozpatku
    print(f"{cislo=}")

###############################################
# ITERACE INTEGERU - int NENI iterovatelny
##############################################
#for cislo in 54321:
#    print(f"{cislo=}")     # int neni iterovatelny!

#################################################
# ITERACE STRINGU
#################################################
nazev_akademie = "Python Academy"
for pismeno in nazev_akademie:
    print(f"{pismeno=}")

