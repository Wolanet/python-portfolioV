import random

misfortune_number = random.randint(1,15)

misfortune_text = ''

if misfortune_number == 1:
  misfortune_text = 'You will be extremely unlucky for the next two years!'
if misfortune_number == 2:
  misfortune_text = 'Your day will be terrible!'
if misfortune_number == 3:
  misfortune_text = 'You will forget your wallet somewhere...'
if misfortune_number == 4:
  misfortune_text = 'Today you will be fired!'
if misfortune_number == 5:
  misfortune_text = 'You will get a speed ticket today!'
if misfortune_number == 6:
  misfortune_text = 'Your close friend will betray you'
if misfortune_number == 7:
  misfortune_text = 'Give up already!'
if misfortune_number == 8:
  misfortune_text = 'You will forget to pay taxes'
if misfortune_number == 9:
  misfortune_text = 'The FBI wants to interrogate you...'
if misfortune_number == 10:
  misfortune_text = 'You are going to gain weight before summer!'
if misfortune_number == 11:
  misfortune_text = 'Your love life could not be worse!'
if misfortune_number == 12:
  misfortune_text = 'The NSA knows all your moves...'
if misfortune_number == 13:
  misfortune_text = 'Welcome to Hell!'
if misfortune_number == 14:
  misfortune_text = 'I hope your car has insurance...' 
if misfortune_number == 15:
  misfortune_text = 'Do not count on getting any help!'

print(f'{misfortune_text} , your (mis)fortune number is: {misfortune_number}')
