# Vytovoreni mnoziny neboli setu
prvni_set = {'dama','zena','ruze','pisen','kost', 50, 16, 'Romana'}    # prazdnou mnozinu vytvorim jako prazdna_mnozina = set ()
print (prvni_set)
druhy_set = {'Milan','Romana','Honza','Matej', 16 }
print (druhy_set)
muj_slovnik = {'Honza': 18, 'Matej': 16}
muj_list = ['Dum','Zahrada']
muj_tuple = ('Pondeli','Utery')

prevod_z_listu_na_set = set (muj_list)
prevod_z_tuplu_na_set = set (muj_tuple)

# METOTA .union() , Datovy typ set, take se pouziva operator | 
# sjednoceni jednotlivych setu
sjednoceni_setu = prvni_set.union (druhy_set)                    # staci take jen prvni_set.union(druhy_set) 
#sjednoceni_setu = prvni_set | druhy_set                         # nebo misto metody pouzit |
print (sjednoceni_setu)

# METOTA .intersection() , Datovy typ set, take se pouziva operator &
# prunik jednotlivych setu
# prunik_setu = prvni_set.intersection(druhy_set)                  # staci take jen prvni_set.intersection(druhy_set) 
prunik_setu = prvni_set & druhy_set                                # nebo misto metody pouzit &
print (prunik_setu)

#METOTA .symmetric_difference() , Datovy typ set, take se pouziva operator ^
# Zobrazuje hodnotu, ktere jsou v jednom nebo druhem setu, ale nejsou v obojich!
# jedinecne_hodnoty = prvni_set.symmetric_difference(druhy_set)     # staci take jen prvni_set.symmetric_difference(druhy_set) 
jedinecne_hodnoty = prvni_set ^ druhy_set                           # nebo misto metody pouzit ^
print (jedinecne_hodnoty)

#METOTA .difference() , Datovy typ set, take se pouziva operator -
# Zobrazuje hodnoty, ktere se nachazi v mnnozine prvni, ale ne mnozine druhe
odlisnost_od_druheho_setu = prvni_set.difference (druhy_set)        # zobrazi hodnoty prvniho setu bez hodnot, ktere jsou v pruniku skupin
# odlisnost_od_druheho_setu = prvni_set - druhy_set                 # zobrazi hodnoty, ktere jsou JEN v mnozine prvni jedinecne tzn., ze vynecha spolecne hodnoty
print (odlisnost_od_druheho_setu)

#METOTA .add() , Datovy typ set
# vlozi jednu hodnotu do setu
prvni_set.add('nova')
print (prvni_set)

#METOTA .update() , Datovy typ set
# metoda pracuje jen s jednou hodnotou proto pokud chci pridat vice hodnot, tak je nutne je schovat do listu nebo tuplu
prvni_set.update(('prvni hodnota', 'druha hodnota'))
print (prvni_set)

#METOTA .discard() , Datovy typ set
# umoznuje vymazat hodnotu, kterou si vyberu
prvni_set.discard('druha hodnota')
print(prvni_set)

#METOTA .pop() , Datovy typ set
# hodnotu vymaze python bez zadani specificke hodnoty 
prvni_set.pop()
print(prvni_set)

#METOTA .isdisjoint() , Datovy typ set
# vraci True, pokud zadny prvek neni spolecny pro obe mnoziny, jinak vraci False
zadna_spolecna_hodnota = prvni_set.isdisjoint(druhy_set)
print (zadna_spolecna_hodnota)

#METOTA .issubset() , Datovy typ set
# vraci True, pokud VSECHNY hodnoty v setu existuji i ve specifikovanem setu
vse_ze_setu_1_v_setu_2 = prvni_set.issubset (druhy_set) 
print (vse_ze_setu_1_v_setu_2)

#METOTA .issuperset() , Datovy typ set
# vraci True, pokud VSECHNY hodnoty v setu 2 existuji i ve vychozim setu 1 
vse_ze_setu_2_v_setu_1 = prvni_set.issubset (druhy_set) 
print (vse_ze_setu_2_v_setu_1)
