marks = 90
if marks >= 90:
    print("you got an A grade")

number = 42 
if number % 2 == 0:
    print('the number is even ')

tempreture = 25 
if tempreture > 25:
    print('its warm day')
    
age = 18
if age >= 18:
    print('your an adult')
else:
    print('your not adult')
    
score = 75
passing_score = 70
if score >= passing_score:
    print("congratulation, you passed")
else:
    if score >= passing_score - 5:
        print("you almost passed")
    else:
        print("you didnt pass")
        
# if elif-else statment

course = "DataScience"
if course == "DataScience":
    print("You are in azad's course.")
elif course == "Physics":
    print("You are in Physics Wallah's course.")
else:
    print("You are not enrolled in any course.")
     

grades = 5

if grades >= 7:
    print("Impressive skills!")
elif grades >= 5:
    print("You're doing well at Physics Wallah!")
else:
    print("Keep working on your skills.")
     

marks = 75
if marks >= 90:
    print("You got an 'A' grade!")
elif marks >= 80:
    print("You got a 'B' grade.")
else:
    print("You got a grade lower than 'B'.")
     

grade = "A"
if grade == "A":
    print("Excellent!")
elif grade == "B":
    print("Good job.")
else:
    print("Try harder.")

     

num = 0
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

     

age = 30
if age < 18:
    print("You are a minor.")
elif 18 <= age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

#'if-else' Statement

course = "DataScience"

if course == "DataScience":
    print("You are studying Data Science.")
else:
    print("You are not in the Data Science course.")
     

azad = 8

if azad >= 7:
    print("Impressive azad!")
else:
    print("You're making progress at Physics Wallah!")
     

is_raining = True
if is_raining:
    print("Take an umbrella.")
else:
    print("Enjoy the sunshine.")

     

num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

     

score = 85
result = "Pass" if score >= 70 else "Fail"
print(f"You {result}.")

     
# Nested 'if-else' Statement

course = "DataScience"

grades = 7
if course == "DataScience":
    if grades >= 7:
        print("Impressive skills in Data Science at azad!")
     

marks = 88
if marks >= 80:
    if marks >= 90:
        print("You got an 'A' grade!")
    else:
        print("You got a 'B' grade.")
     

is_weekend = False
is_sunny = True

if is_weekend:
    if is_sunny:
        print("Go for a picnic.")
    else:
        print("Stay in and relax.")
else:
    print("It's a workday.")

     

is_student = True
is_teacher = False

if is_student:
    if is_teacher:
        print("You are both a student and a teacher.")
    else:
        print("You are a student but not a teacher.")
else:
    if is_teacher:
        print("You are a teacher but not a student.")
    else:
        print("You are neither a student nor a teacher.")

     

is_vip = True
age = 30

if is_vip:
    if age >= 18:
        if age < 65:
            print("Welcome, VIP customer!")
        else:
            print("You're a VIP, but you qualify for senior discounts.")
    else:
        print("VIP status is for adults only.")
else:
    print("Regular pricing applies.")    