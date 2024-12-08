zamestnanci = ['František', 'Bruno', 'Anna' , 'Jakub', 'Klára', 'Anežka','Anežka', 'Anežka']
posledni_index = zamestnanci [-1] #print (posledni_index) je Anezka
kolikaty_je_posledni_index = len (zamestnanci) - 1
print ('Na indexu 2 je: ',zamestnanci [2])
print ('Na poslednim indexu je: ',posledni_index, ' .Cislo posledniho indexu je:',kolikaty_je_posledni_index) 
print ('V intervalu od 2 do 5 je: ', zamestnanci [2:6]) #jedna se o otevreny interval na konci tzn., ze nezahrnuje hranice intervalu.. proto konci 6stkou
print ('Kazdy treti clen je: ', zamestnanci [::3])
