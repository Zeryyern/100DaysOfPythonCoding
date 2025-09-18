#DAY - 2
#LEARNING ABOUT F-STRING

#f-string = formatted string
fname = "Zayyan"
lname = "Awwal"
print(f"Hello, {fname} {lname}, welcome aboard!") #f-string

num_1 = 20
num_2 = "Zayn"
print(f"{num_1} {num_2}")

#CHALLENGE --Write a program that tells us how many weeks we have left, if we live until 90 years old.
age = input("Enter your current age: ")
years_remaining = 90 - int(age)
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")


