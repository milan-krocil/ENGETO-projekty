mercedes = 150000
rolls_royce = 400000
vybava = 50000
sleva_Merc = 5000

cena_2_merc = 2 * sleva_Merc
cena_merc_a_rolls = mercedes + rolls_royce
cena_2_rolls_s_vybavou = 2 * (rolls_royce + vybava)
merc_se_slevou = mercedes - sleva_Merc

print ('Cena za 2 Mercedesy je: ', cena_2_merc)
print('Cena za Mercedes a rolls je: ',cena_merc_a_rolls)
print('Cena za 2 rolls je: ', cena_2_rolls_s_vybavou)
print('Cena za Mercedes se slevou je: ',merc_se_slevou)