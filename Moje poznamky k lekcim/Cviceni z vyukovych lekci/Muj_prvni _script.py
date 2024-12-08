
kg_lb = 2.2
km_mile = 0.62
l_gal = 0.26

kg_pocet = input('Zadej pocet kg:')
km_pocet = input ('Zadej pocet km:')
l_pocet = input ('Zadej pocet litru:')


kg_vysledek = int(kg_pocet) * (kg_lb)
km_vysledek = int(km_pocet) * (km_mile)
l_vysledek = int(l_pocet) * (l_gal)
print (kg_pocet, 'kg je' , kg_vysledek, 'liber')
print (km_vysledek)
print (l_vysledek)