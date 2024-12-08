jmeno = input('Zadej jmeno: ')
heslo = input('Zadej heslo: ') 
uzivatel = {'Marek':'1234'}

kontrola_jmena = uzivatel.get(jmeno)
if kontrola_jmena == heslo:
    print ('Ahoj',jmeno,'vitej v aplikaci! Pokracuj...')
else:
    print ('Uzivatelske heslo neni v poradku')