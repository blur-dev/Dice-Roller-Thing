import random;

roll_again='Yes'

while roll_again=='Yes':
  print("We rolling it")
  print('This is what you got')
  dice1=random.randint(1,6)
  dice2=random.randint(1,6)
  print(dice1,dice2)
  roll_again=input("Wanna go again Yes or No: ")