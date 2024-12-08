slova = []
slovo = input('Zadej slovo se 4 znaky: ')

while slova != 3:
  if len(slovo) != 4:
    print('Slovo musi byt se 4 znaky')
    slovo = input('Zadej slovo se 4 znaky: ')
    continue
  if slovo in slova:
    print('Slovo ',slovo ,'uz mam ulozene')
    slovo = input('Zadej slovo se 4 znaky: ')
    continue
  slova.append(slovo)
  if len(slova) == 3:
    print('Uz mam ulozene 3 slova') 
    break
  slovo = input('Zadej slovo se 4 znaky: ')
print('Ulozena slova jsou: ', slova)

###############################################################################
# RESENI z ENGETA
###############################################################################

# Proměnná, kam budeš ukládat slova
slova = set()

# zadávej slova tak dlouho, dokud proměnná neobsahuje tři hodnoty
while len(slova) != 3:
    slovo = input("zadej slovo ze čtyř: ".upper())

    # .. pokud je již zadané slovo uložené, upozorni uživatele
    if slovo in slova:
        print("Slovo", slovo, "už je uložené")

    # .. pokud má slovo délku 4 znaky, ulož jej do proměnné
    elif len(slovo) == 4:
        slova.add(slovo)

    # .. pokud nemá slovo délku 4 znaky, upozorni uživatele
    else:
        print("Slovo není dlouhé čtyři znaky")

# Jakmile má objekt uložené tři hodnoty, cyklus ukonči a vypiš oznámení
else:
    print("Už mám uložené tři slova.")