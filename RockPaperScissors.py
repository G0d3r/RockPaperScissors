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
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

def get_user_choice():
    while True:
        user_input = input("What do you choose? Type 0 for Rock, Type 1 for Paper, Type 2 for Scissors. ")
        if user_input in ['0', '1', '2']:
            return int(user_input)
        else:
            print("Invalid choice. Please choose 0, 1, or 2.")

def main():
    rock_paper_scissors = [rock, paper, scissors]
    while True:
        random_choice = random.randint(0, 2)
        user_choice = get_user_choice()

        print("Your choice:", rock_paper_scissors[user_choice])
        print("Computer choice:", rock_paper_scissors[random_choice])

        if random_choice == user_choice:
            print("It's a tie!")
        elif (random_choice == 0 and user_choice == 2) or (random_choice == 1 and user_choice == 0) or (random_choice == 2 and user_choice == 1):
            print("Computer wins!")
        else:
            print("You win!")
            break # Finish the loop after the user wins.

if __name__ == "__main__":
    main()