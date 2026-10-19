def greetings(name="Student"):
    print("Hello", name , "!")
greet("Haris")
greet()


def introduction(name, age):
    print("My name is:", name, "and I am:", age)
introduction(age=20, name="Akif")

def add(x, y):
    return x + y
result = add(5, 15)
print(result)





def check_pass(marks):
    if marks >=40:
        return("Student has passed")
    else: 
        return("Student has failed")
print(check_pass(90))
print(check_pass(45))
