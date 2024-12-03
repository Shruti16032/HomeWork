# if_else
a = True
b = False
c = "shruti"
print(type(a))
# relational
a = 10 
b = 20

print(a<b)
print(a>b)
print(a>=b)
print(a<=b)
print(a!=b)
print(a==b)

# logical operator
c1 = a > 10
c2 = b > 10

r1 = c1 and c2
r2 = c1 or c2
r3 = not(c1)
print(r1)
print(r2)
print(r3)

# if else
a = True or False
if a:
    print("If Block")
    print("Whohh")
else:
    print("Else block")

#odd even 
n = int(input())
if(n % 2 == 0):
   print("Even number")
else:
   print("Else Block")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
# check if the number is between 1 to 10
s = 15
if s >= 1 and s <= 10:
    print("too low")
elif s >= 10 and s <= 20:
    print("medium")  
else:
    print("too large")

# 
x = 5
if x < 6:
    print("hello")
if x == 5:
    print("hii")
else:
    print("hey") 

#
x = 15
if x <= 15:
    print("inside if")
else:
    print("inside else") 

# Numbers
a1 = 2
a2 = 3.5
a3 = 4 +6j
print(type(a1))
print(type(a2))
print(type(a3))

a = 10
id1 = id(a)
b = a + 2-2
id2 = id(b)

print(id1)
print(id2)

#Arithmatic operation

#simple inrest to tow interger
p = 100
r = 12
t = 2
si = (p*r*t)/100
print(si)

f = 97.6
c = (f-32) * 5/9
print(c)

# simple intrest 
print("enter the principal")
p = float(input())
print("enter time ")
t = float(input())
print("enter rate")
r = float(input())
si = (p*r*t)/100
print(si)

a = input()
b = input()
c = a+b
print(c)

a = int(input())
b = int(input())
c = int(input())
average = (a + b+ c)/3
print(average)

s = int(input())
e = int(input())
w = int(input())

F = s
while(F <= e):
    c = (F -32) *(5/9)
    print(F,"\t",int(c))
    F = F + w

#calculator
while True:
    n = int(input())
    if(n == 1):
      a = int(input())
      a = int(input())
      print(a+b)
    if(n == 2):
        a = int(input())
        b = int(input())
        print(a-b)
    if(n == 3):  
        a = int(input())
        b = int(input())
        print(a*b)
    if(n == 4):  
        a = int(input())
        b = int(input())
        print(a/b)
    if(n == 5):  
        a = int(input())
        b = int(input())
        print(a%b)
    if(n == 6):  
        sys.exit(0)
    if(n < 1 and n > 6):
        print("Invalid ")   
#Revers of number 
def revers(n):
    rev = 0
    while(n > 0):
        rem = n%10
        rev = (rev * 10) +rem
        n = n//10
        return rev 
n = int(input())
result = revers(n) 
print(result) 

