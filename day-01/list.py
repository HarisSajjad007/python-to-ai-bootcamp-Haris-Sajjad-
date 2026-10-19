#list
skills = ["Ml", "Python", "Numpy", "OP", "DSA" , "ML"]

print(skills[2])
print(skills[5])

skills[2] = "Deep Learning"
print(skills[2])

print(len(skills))

print("maths" not in skills)

skills.append("Maths")
print(skills)
skills.insert(3, "List")
skills.extend(["Calculus", "Stats", "Prob"])
print(skills)

num = [10,30,20]
sorted_num = sorted(num)
print(sorted_num)

# tuples:
axis = (25, 35)
a, b = axis
print(a)
print(axis[1])
print(len(axis))

print(axis.index(35))

# sets:
skills = {"C++" , "JAvascript" , "Python" , "Web devp"}
print(skills)
skills.add("AI")
skills.update(["ML" , "SQL" , "Deep learning"])
skills.remove("Javascript")
print(skills)

# dictiionaries:
student = {
    "name": "Haris",
    "age": 20,
    "gpa": 3.94
}
print(student["gpa"])
print(student.get("age"))

for key, value in student.items():
    print(key, ":", value)
    
print(student.get("age"))
print(student.keys())
print(student.values())
print(student.items())
print(student.update({"gpa": 3.95})
