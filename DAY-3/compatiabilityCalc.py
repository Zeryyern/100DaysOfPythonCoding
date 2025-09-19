#DA Y 3 OF LEANING PYTHON 
#cOMPATIABILITY CALCULATOR
print("The love calculator is calculating your love score...")
num1 = input("what is your name? ")
num2 = input("What is their name? ")
combined_names = num1 + num2
lower_case_names = combined_names.lower()
t = lower_case_names.count("t")
r = lower_case_names.count("r")
u = lower_case_names.count("u")
e = lower_case_names.count("e")
true = t + r + u + e
l = lower_case_names.count("l")
o = lower_case_names.count("o")
v = lower_case_names.count("v")
e = lower_case_names.count("e")
love = l + o + v + e
love_score = int(true + love)
if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

