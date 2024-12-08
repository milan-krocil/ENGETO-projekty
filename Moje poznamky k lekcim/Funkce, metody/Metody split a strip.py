veta = 'milan a romana bydli v Orechove na Bakesove 4, na konci. Maji se dobre. Asi...'
#veta.split()
ocisteny_seznam = []
for slovo in veta.split():
  #ciste_slovo = slovo.strip('.,')
  ocisteny_seznam.append(slovo.strip('.,'))

print(ocisteny_seznam)