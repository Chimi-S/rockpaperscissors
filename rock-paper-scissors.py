import random

print("WELCOME TO ROCK PAPER SCISSORS GAME!")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)_____
        _________)
       (_________          
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
gamers_hand = [rock, paper, scissors]

gamer_choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))
print(f"You chose {gamer_choice}\n {gamers_hand[gamer_choice]}")

computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice} \n {gamers_hand[computer_choice]}")

if gamer_choice >= 3 or gamer_choice < 0:
    print("You typed an invalid number, you lose!")
elif gamer_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice > gamer_choice:
    print("You lose!")
elif computer_choice == gamer_choice:
    print("It's draw")
elif computer_choice == 0 and gamer_choice == 2:
    print("You lose!")
elif gamer_choice > computer_choice:
    print("You win!")