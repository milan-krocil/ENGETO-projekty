#Frozenset je temer identicky jako obycejny set, akorat jej NELZE MENIT pote, co jej vytvorime
#Frozenset pouziva STEJNE METODY jako set
muj_prvni_frozenset = frozenset ()                      # nema smysl ho vytvaret, protoze do jeho promenne nelze nic vlozit!
muj_druhy_frozenset = frozenset ('Milan')               # vytvoreni mnoziny typu frozenset ze stringu 
muj_treti_frozenset = frozenset (['Romana','Milan'])    # vytvoreni mnoziny typu frozenset z listu
muj_ctvrty_frozenset = frozenset (('Milan','Romana'))   # vytvoreni mnoziny typu frozenset z tuple
print (muj_druhy_frozenset)          
print (muj_treti_frozenset)  
print (muj_ctvrty_frozenset)
                    
