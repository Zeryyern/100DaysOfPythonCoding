#DAY 3 OF LEARNING PYTHON
#CONDITIONAL STATEMENTS, LOGICAL OPERATORS, CODE BLOCKS AND SCOPE
#Treasure Island Game
print('''
******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to treasure Islad.")
print("Your mission is to find the treasure.")
print("You are at a cross road. Where do you want to go? Type 'left' or 'right'")
choice1 = input("Type left | right ").lower()
if choice1 == "left":
    choice2 = input("Swim or wait? Type 'swim' to swim across the lake or 'wait' to wait for a boat. ").lower()
    if choice2 == "wait":
        choice3 = input("which door?" ).lower()
        if choice3 == "red":
            print(f"You enter a room full of fire. Game over.")
        elif choice3 == "blue":
            print(f"You enter a room of beasts. Game over. ")
        elif choice3 == "yellow":
            print(f"You found the treasure! You win buddy!")
        else:
            print(f"You chose a door that doesn't exist. Game over.")
    else:
        print(f"You get attacked by an angry trout. Game over.")
else:
    print(f"You fell into a hole. Game over.")
    
