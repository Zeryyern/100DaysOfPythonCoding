#DAY 4 OF LEARNING PYTHON
#Python Lists
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey" "Georgia", "Connecticut", "Massachusetts",
#                      "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
#                      "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
#                      "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada",
#                      "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
# print(states_of_america)
# #modifying an item in the list
# states_of_america[0] = "Malware"
# print(states_of_america)
# #appending to the list
# states_of_america.append("Puerto Rico")
# print(states_of_america) 
#CHALLENGE
#write a program that will select a random name from a list of names.
import random
user_input = input("Give me everybody's names, seperated by a space. ")
names = user_input.split()
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(f"{person_who_will_pay} is going to buy the meal today!")
#OR
# person_who_will_pay = random.choice(names)



