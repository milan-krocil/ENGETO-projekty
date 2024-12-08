jmeno = 'Martin'
vaha = 100
vyska = 200
vyska_v_metrech = 0.01 * vyska
bmi = vaha / vyska_v_metrech ** 2
kategorie = ('Podvyziva','Zdrava vaha','Mirna nadvaha', 'Obezita', 'Tezka obezita') # datovzy typ tuple
if bmi < 18.5 :
    print (jmeno, 'tve BMI je ',bmi,'coz spada do kategorie',kategorie [0])
elif bmi > 18.5 and bmi <= 25 :
    print (jmeno, 'tve BMI je ',bmi,'coz spada do kategorie',kategorie [1])
elif bmi > 25 and bmi <= 30 : 
    print (jmeno, 'tve BMI je ',bmi,'coz spada do kategorie',kategorie [2])
elif bmi > 30 and bmi <= 40 :
    print (jmeno, 'tve BMI je ',bmi,'coz spada do kategorie',kategorie [3])
else :
    print (jmeno, 'tve BMI je ',bmi,'coz spada do kategorie',kategorie [4])