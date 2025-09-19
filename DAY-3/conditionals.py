#DAY 3 OF LEARNING PYTHON
#CONDITIONALS STATEMENTS
print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("what's your age? "))
    if age < 12:
        bill = 5
        print("You will pay $5")
    elif age<=18:
        bill = 7
        print("You will pay $7")
    else:
        bill = 12
        print("You will pay $12")
    want_photo = input("Do you want a photo taken? Y or N. ")
    if(want_photo == "Y"):
        bill += 3
        print(f"Your final bill is ${bill}")
    else:
        print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")  
#CHALLENGE
#write a program that interprets the body mass index (BMI) based on a user's weight and height.
height = float (input("Enter your height in m: "))
weight = (int(input("Enter your weight in kg: ")))
bmi = weight /(height**2)
bmi_as_int = int(bmi)
if bmi_as_int < 18.5:
    print(f"{bmi_as_int}, you are underweight. ")
elif bmi_as_int < 25:
    print(f"{bmi_as_int}, you have a normal weight. ")
elif bmi_as_int < 30:
    print(f"{bmi_as_int}, you are slightly overweight. ")
else:
    print(f"{bmi_as_int}, you are obese.")
#write a program that works out wheather if a given number is odd or even number
number = int(input("Which number do you wanna check? "))
if number%2==0:
    print("This is an even number.")
else:
    print("This is an odd number.")
   