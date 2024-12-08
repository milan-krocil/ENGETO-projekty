zamestnanci = ['František','Anna','Jakub','Klára']
zamestnanci_a = zamestnanci
print('Zamestnanci na zacatku: ', zamestnanci_a)
nova_jmena = ['Bruno', 'Anezka']
zamestnanci_a.extend(nova_jmena)                  # metoda pro pridani vice hodnot nez jedne 
print ('Nova jmena pridana:',zamestnanci_a)
zamestnanci_a.append('Bruno')
print (zamestnanci_a)                             # metoda pro pridani jede hodnoty na konec seznamu 
zamestnanci_b = zamestnanci
zamestnanci_b.insert(1,'Bruno')                   # metoda pro pridani jedne hodnoty na specificke misto (index 1) 
print ('Nova jmena vlozena:',zamestnanci_b )