cisla = [1, 2, 3, 4, 5, 6, 7, 8]
suda = []
licha = []
#vysledek = []
for pomoc in cisla:
    if pomoc % 2 == 0:
        (suda.append(pomoc))
    else:
        (licha.append(pomoc))
        
#print (sum (licha))
#print (sum(suda))

vysledek = sum (licha) - sum (suda)
print ('Rozdil je: ', (abs (vysledek)))


####################################################################################
# Jiny zpusob - dle reseni ze skoly
cisla = [1, 2, 3, 4, 5, 6, 7, 8]

licha = 0
suda= 0

for cislo in cisla:
    if cislo % 2 == 0:
        suda = suda + cislo
    else:
        licha = licha + cislo

vysledek = abs(suda - licha)
print('Rozdíl je:', vysledek)