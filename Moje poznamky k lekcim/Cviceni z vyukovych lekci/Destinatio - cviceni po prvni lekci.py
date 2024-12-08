mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
cara = "=" * 35
nabidka = """
1 - Praha   | 150,-Kč
2 - Viden   | 200,-Kč
3 - Olomouc | 120,-Kč
4 - Svitavy | 120,-Kč
5 - Zlin    | 100,-Kč
6 - Ostrava | 180,-Kč
"""

print ('Vitejte v nasi aplikaci DESTINATIO')
cara = len ('Vitejte v nasi aplikaci DESTINATIO')
print('=' * cara)
print('Podivejte se na nasi nabidku:',end='')
print (nabidka,end='')
print('=' * cara)

cislo_destinace = input ('vyber cislo destinace: ')
Jmeno = input ('Zadej sve jmeno: ')
Prijmeni = input ('Zadej sve prijmeni: ')
Email = input ('Zadej svoji emailovou adresu: ')

print ('Vitejte v nasi aplikaci DESTINATIO')
cara = len ('Vitejte v nasi aplikaci DESTINATIO')
print('=' * cara)
print('Podivejte se na nasi nabidku:',end='')
print (nabidka,end='')
print('=' * cara)
print ('Cislo_destinace: ', cislo_destinace)

print('=' * cara)
print ('Finalni destinace> ', mesta[int(cislo_destinace)-1])
print('=' * cara)
print ('Finalni cena je: ' , ceny [int(cislo_destinace)-1])
print('=' * cara)

print ('Cestujici: ',Jmeno + ' ' + Prijmeni)
print ('Cilova destinace: ', mesta[int(cislo_destinace)-1])
print ('Cena jizdneho: ', ceny [int(cislo_destinace)-1])
print ('Jizdenku jsme odeslali na email:',Email+'.')