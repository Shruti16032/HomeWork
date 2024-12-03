# 1 
s = 'learning'
for ch in range(len(s)):
    print(ch)
print(s[ch]) 
# 2
for i in range(5):
    print(i)
# 3
for i in range(10):
    if i%2 == 0:
     print(i)  

# 4
numbers = [1,2,3,4,5]
total = 0
for num in numbers:
    total += num
print(total)

#5
for char in "hello":
    print(char)
#6
fruits = ['apple','mango','banana'] 
for fruit in fruits:
    print(fruit)
# 7
data = {"name":"shruti","Age":"24"}
for key,value in data.items():
    print(key,value)

#8
for i in range (5,0,-1):
    print(i)

#9
for i in range(1, 6):
    print(i)
#10 printing character in string
word = "Hello"
for letter in word:
    print(letter)


grocery_list = ["Milk", "Orange", 1, 2, 3, True, 2+4j, 2.3]
grocery_list[-1]
