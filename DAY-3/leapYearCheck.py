#DAY 3 OF LEARNING PYTHON
#CHECKING IF A YEAR IS A LEAP YEAR
#write a program that works out wheather if a given year is a leap year.
year = int(input("Which year do you want to check? "))
if (year%4==0 and year%100!=0) or year%400==0:
    print(f"{year}, is a leap year.")
else:
    print(f"{year}, is not a leap year.")