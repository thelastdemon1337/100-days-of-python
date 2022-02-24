import random
ascii_rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
ascii_paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
ascii_scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

computer_hand = [ascii_rock, ascii_paper, ascii_scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice == 0:
  print(ascii_rock)
  print("Computer chose:")
  comp_choice = random.choice(computer_hand)
  print(comp_choice)
  if comp_choice == computer_hand[0]:
    print("Draw *_*")
  elif comp_choice == computer_hand[1]:
    print("Computer Won. $_$")
  else:
    print("You won! ^_^")

  
elif choice == 1:
  print(ascii_paper)
  print("Computer chose:")
  comp_choice = random.choice(computer_hand)
  print(comp_choice)
  if comp_choice == computer_hand[1]:
    print("Draw *_*")
  elif comp_choice == computer_hand[2]:
    print("Computer Won. $_$")
  else:
    print("You won! ^_^")
else:
  print(ascii_scissors)
  print("Computer chose:")
  comp_choice = random.choice(computer_hand)
  print(comp_choice)
  if comp_choice == computer_hand[2]:
    print("Draw *_*")
  elif comp_choice == computer_hand[0]:
    print("Computer Won. $_$")
  else:
    print("You won! ^_^")