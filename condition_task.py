 # 1. Check a number Write a program to check if a number is positive, negative, or zero.
number = 2
if number > 0:
        print("The number is positive.")
if number < 0:
        print("The number is negative.")
if number == 0:
        print("The number is zero.")
# 2. Check even or odd  Write a program to check if a given number is even or odd.
number = 10
if number %2 == 0:
        print('number is even')
else:
       print('number is odd')

# 3.Grade Checker  Write a program to display grades based on a percentage:
percentage = 77
if 90 <= percentage <= 100:
    print("Grade: A")
elif 70 <= percentage < 90:
    print("Grade: B")
elif 50 <= percentage < 70:
    print("Grade: C")
elif 0 <= percentage < 50:
    print("Grade: F")

# 4. Check divisibility  Check if a given number is divisible by 3, 5, or both.    

number = 20
if number % 3 == 0 and number % 5 == 0:
      print('Number is divisibile by 3 and 5')
if number % 3 == 0:
      print('number is divisible by 3')
if number % 5== 0:
      print('number is divisible by 5')
# 5.  Minimum of two numbers  Find the smaller number between two given numbers.
num1 = 20
num2 = 5
if num1 < num2:
    print("The smaller number is {num1}.")
if num2 < num1:
    print("The smaller number is {num2}.")


### Nested Conditional Questions
#6. Find the largest of three numbers Given three numbers, find the largest using nested if statements.
num1 =20
num2 = 30
num3 = 40
if num1 >= num2:
    if num1 >= num3:  
        print("The largest number is {num1}.")
    else:
        print("The largest number is {num3}.")
else:  
    if num2 >= num3:  
        print("The largest number is {num2}.")
    else: 
        print("The largest number is {num3}.")

#7. Check leap yearWrite a program to check if a given year is a leap year or not- Divisible by 4 and not 100, or divisible by 400.

#Nested temperature check  Categorize temperature
temperature = 40
if temperature < 15:
    print("The weather is cold.")
else:
    if temperature <= 30:
        print("The weather is warm.")
    else: 
        print("The weather is hot.")

# 9 Vowel or consonantCheck if a given character is a vowel or consonant.

#10  Driving eligibility  Check if a person is eligible to drive
is_eligible = True
age = 20

if is_eligible:
    if age >= 18:
       print('elegible to drive')
    else:
        print('not eligible to drive not have valid licen') 
else:
    print('driving licen is for adult only')

#11.Triangle validation  Check if three sides can form a triangle:
side1 = 10
side2 = 20
side3 = 30
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("The sides can form a triangle.")
else:
    print("The sides cannot form a triangle.")

#12.Calculate tax based on salary Determine the tax rate:

salary = 10000

if salary <= 500000:
    tax = salary * 0.05  
elif salary <= 1000000:
    tax = salary * 0.10
else:
    tax = salary * 0.20

print("The tax on your salary is:{tax}")

#13.Categorize age Categorize a person's age:
age = 20

if age >= 0 and age <= 12:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teen")
elif age >= 20 and age <= 59:
    print("Adult")
elif age >= 60:
    print("Senior")
else:
    print("Invalid")

#14. Logical AND Check if a number is greater than 10 and divisible by 2.    

num = 20
if num > 10 and num %2 == 0:
     print("number is grater then 10 and divisible by 2")
else:
     print("the number is not grater then 10 and not divisible by 2")

#15. Logical OR check  Check if a number is less than 5 or greater than 20.
num = 4
if num < 5 or num > 20:
     print("less then 5 or grater then 20")
else:
     print("the number is not less then 5 or not grater then 20")

#16.units = int(input("Enter electricity usage in units: "))
units =100
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 10 
else:
    bill = units * 15

print("The total electricity bill is: {bill}")   

# 17. Season finder Find the season based on the month:

month = 'December'

if month in ["December", "January", "February"]:
    print("Winter")
elif month in ["March", "April", "May"]:
    print("Spring")
elif month in ["June", "July", "August"]:
    print("Summer")
elif month in ["September", "October", "November"]:
    print("Autumn")
else:
    print("Invalid month entered.")

# 18.  Password validation  Check if a password meets these conditions:
password = input("Enter your password: ")
if len(password) >= 8:
    if '@' in password: 
        print("Password is valid.")
    else:
        print("Password must contain '@'.")
else:
    print("Password must be at least 8 characters long.") 

# 19. Categorize BMI  Categorize Body Mass Index (BMI):
bmi = 52

if bmi < 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal")
elif bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")

# 20.Character type checkerCheck if a given character is:
char = input('enter the character')
if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
    print("Alphabet")
elif '0' <= char <= '9':
    print("Digit")
else:
    print("Special character")
    
