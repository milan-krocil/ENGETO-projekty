#Overeni spravnost prvniho pismene kazdeho dne v tydnu
vstupni_cisla = [1, 2, 3, 4, 5, 6, 7,'Ivan']   #Jedna se o list
vstupni_slovnik = {'Jmeno': 'Milan', 'Vek': 50, 32:25}   # Jedna se o slovnik
# slovnik muzu take vytvorit nasledovne: vstupni slovnik = dict ('Jmeno'='Milan', 'Vek' = 50)
# slovnik muzu take vytvorit nasledovne vstupni slovnik = {
#                                                           'Jmeno' = 'Milan,
#                                                            'Vek' = 50
#                                                            }
list_kontaktu = {'email': 'Email 1', 'Telefon':'Telefon 1', 'Kontakt': 'Orechov', 'Osoba':'Matej'}   # Jedna se o slovnik
vstupni_pismena = ["p", "ú", "s", "č", "p", "s", "n"]  #Jedna se o list
tyden = ('pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle') #Jedna se o tuple

# METOTA .items() , Datovy typ SLOVNIK (disc)
vstupni_slovnik['list_kontaktu'] = list_kontaktu
print (vstupni_slovnik)
print (vstupni_slovnik ['list_kontaktu']['Telefon'])
print (vstupni_slovnik ['list_kontaktu']['email'])
print(vstupni_slovnik.items())                            # Pouziti Metody items ()
vstupni_slovnik ['email'] = 'Email 2'                     # Ve slovniku "vstupni_slovnik" dojde u klice 'email' k zamene na 'Email 2'  
list_kontaktu.items()                                     # Pouziti Metody items ()
list_kontaktu ['email'] = 'Email 5'                       # Ve slovniku "list_kontaktu" dojde u klice 'email' k zamene na 'Email 5'  
vstupni_slovnik ['Jmeno'] = 'Romana'                      # Ve slovniku "vstupni_slovnik" dojde u klice 'Jmeno' k zamene na 'Romana' (prepis). Nebo prida hodnotu Romana a klic Jmeno, pokud neexistuje   
print (vstupni_slovnik['email'])
print (vstupni_slovnik['Jmeno'])
print (vstupni_slovnik)

# METOTA .get() , Datovy typ SLOVNIK (disc)
# Vraci hodnotu zadaneho klice, pokud existuje
print (vstupni_slovnik.get('Jmeno'))                    
if vstupni_slovnik ['Jmeno'] == 'Romana':               # Klic 'Jmeno' ve slovniku 'vstupni_slovnik' existuje => vypise jeho hodnotu 'Romana' 
    print ('je tam')
else: 
    print ('neni tam')     
print (list_kontaktu.get('Jmeno'))                      # Klic 'Jmeno' ve skovniku 'list kontaktu' neexistuje => vypise 'None'

# METODA .pop()  Datovy typ SLOVNIK (disc)
# Odstrani zadany klic a jeho hodnotu
print (list_kontaktu.pop ('Kontakt'))                   # Vymazal klic 'Kontakt' a jeho hodnotu 'Orechov' ve slovniku 'list_kontaktu' 

# METODA .popitem()  Datovy typ SLOVNIK (disc)
# Odstrani posledni vlozeny klic a jeho hodnotu
list_kontaktu ['Dalsi kontakt'] = 'Brno'
print (list_kontaktu)
list_kontaktu.popitem()                                 # Vymazal posledni klic a jeho hodnotu ve sklovniku 'list_kontaktu'. Metoda se pise s prazdnyma zavorkama
print (list_kontaktu)

# METODA .copy()  Datovy typ SLOVNIK (disc)
# Zkopiruje slovnik do noveho slovniku napr. 'list_kontaktu_1
list_kontaktu_1 = list_kontaktu.copy()                  # Vytvori list_kontaktu_1 se stejnym obsahem jako list_kontaktu
print (list_kontaktu_1)

# METODA .clear()  Datovy typ SLOVNIK (disc)
# Odstrani vse ze slovniku
list_kontaktu.clear ()                                  # vymaze ze slovniku vsechny klice a hodnoty. Zustane jen prazdny slovnik 'list_kontaktu'
print (list_kontaktu)

# METODA .keys()  Datovy typ SLOVNIK (disc)
# Vytvori list klicu v konkretnim slovniku
list_klicu = list_kontaktu_1.keys ()                    # vypise seznam vsech pouzitych klicu ve slovniku
y= list (list_klicu)                                    # muzu to prevest na datovy typ list     
print (y[0])                                            # muzu vytisknout napr prvni klic tzn. umistene na indexu 0 

# METODA .values()  Datovy typ SLOVNIK (disc)
# Vytvori list hodnot v konkretnim slovniku
list_hodnot = list_kontaktu_1.values()                  # vypise seznam vsech pouzitych hodnot ve slovniku
print (list_hodnot)                                     
z = list (list_hodnot)                                  # muzu to prevest na datovy typ list a vytisknout napr treti hodnotu tzn. umistene na indexu 2
print (z [2])                                           # muzu vytisknout napr treti hodnotu tzn. umistene na indexu 2

# METODA .update()  Datovy typ SLOVNIK (disc)              
# Prida do slovniku dalsi par z jineho slovniku
list_kontaktu_1.update({'Dalsi osoba':'Honza'})         # Do listu kontaktu pridam dalsi klic s hodnotou. Nutne je dat do slozenych zavorek, protoze se jedna o slovnik
print (list_kontaktu_1)        

           
