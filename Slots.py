'''
Programmer: Edward Allington
Program: Slots
'''
import random
fruit = ["Cherry", "Orange", "Plum", "Bell", "Melon", "Bar"]
money = 100
player = input("Hello. What's your name? ")
print(f"Nice to meet you {player}. Welcome to the Slots Game. You start with $100.")
running = str(input("Would you like to play slots? Type yes, or no: "))
while running == "yes":
    bet = int(input("Enter your bet. Anything that's at least $25 "))
    if bet < 25:
        print("Sorry, but bets must be a minimum of $25.")
        running = "no"
    item = random.choice(fruit)
    item2 = random.choice(fruit)
    item3 = random.choice(fruit)
    print(f"Slot 1: {item}, Slot 2: {item2}, Slot 3: {item3}.")
    if item == item2 and item == item3 and item2 == item3:
        print("Nice! All three slots matched! You win $75.")
        money += 75
        print(f"Your current balance is: {money}.")
    elif item == item2 or item2 == item3 or item == item3:
        print("Two of your two slots matched, you won $25.")
        money += 25
        print(f"Your current balance is: {money}.")
    else:
        money -= bet
        print(f"Ohh... sorry, but none of the slots matched. You lost the ${bet} you betted")
        print(f"Your current balance is: {money}")
    running = str(input("Would you like to play again? "))
print(f"Oh, okay. Well you walk away with ${money} left. Thanks for playing, and we hope to see you again soon!")