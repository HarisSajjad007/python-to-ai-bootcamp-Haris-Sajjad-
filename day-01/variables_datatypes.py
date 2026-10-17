print("Hello, GDG WAH!!!")
print("My name is Haris sajjad")

name = "Haris Sajjad"
Print("Hello my name is:",name)

Age = 20
Cgpa = 3.59
is_student = True
Print("Name:",name," ","Age:",Age," ","cgpa:",Cgpa," ",Student_status:",is_student)
Print(type(name))
print(type(Age))

num = int(input("Enter a number:"))
print(num)
print(type(num))

# # += // pre 
# # =+ // post 

# Conditional Statements:
# (positive or negative num):
num = int(input("Enter a value: "))
if num > 0:
    print("positive")
elif num < 0:
    print("negitive number")
else:
    print("the number is ZERO!")

# (Even or Odd)
num1 = int(input("Enter a number:"))
if num1 % 2 == 0:
    print("The number is even")
else num1 % 2 == 1:
    print ("The number is odd")

# (ID card)
num2 = int(input("Enter your Age"))
if num2 < 0 or num2 > 150:
    print("Invalid age")
elif num2 >= 18 and num2 <= 150:
    print("Can get ID card")
else:
    print("no")
    
# for i in range(1,6,2):
#     print(i)

for number in range(1,10):
    if number == 3 or number == 6:
        continue
    if number == 9:
        break
    print(number)

# (Even or odd)
for number in range(1,50):
    if number % 2 == 0:
        print("Number is even")
    elif number % 2 == 1:
        print("Number is odd")
    else:
        print("Invalid number")

# (pass or fail)
for number1 in range (1,5):
    number2 = float(input("Enter a number"))
    if number2 >= 50:
        print("Passed")
    else:
        print("Failed")

# is divisible by 2?
num3 = int(input("Enter a number:"))
while num3 % 2 == 0:
    print("The number is divisible by 2")
    num3 = int(input("Enter the number again:")
print("The number is not divisible by 2 and is odd")







