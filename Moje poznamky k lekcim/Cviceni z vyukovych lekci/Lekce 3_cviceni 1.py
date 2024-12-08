user_1 = dict ()
user_1 ['name'] = 'Marek'
user_1 ['surname'] = 'Parek'
user_email = {'Email':'marek.parek@gmail.com'}

user_1.update(user_email)     # pokud bych nechtel vytvaret slovnik 'user_email tak to muzu napsat rovnou do metody update ... user_1.update({'Email':'marek.parek@gmail.com'}) 
               
print ('User #1', user_1)
