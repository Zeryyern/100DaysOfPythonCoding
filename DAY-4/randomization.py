#DAY 4 OF LEARNING PYTHON
#Randomization
import random
# import my_module
# print(my_module.pi)
# random_integer = random.randint(1, 100)
# print(random_integer) #Integer between 1 and 100
# print(random.random()) #float between 0 and 1
# random_float = random.random() * 5

#CODE CHALLENGE
#write a virtual coin toss program. it will randomly tell the user "Heads" or "tails"
random_side = random.randint(0,1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")
  
