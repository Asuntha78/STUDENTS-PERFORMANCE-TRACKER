# Students Performance Tracker

while True:
    number_of_students = int(input("Enter the number of students:"))
    if number_of_students > 0:
        break


student_name = [] # An empty list named "student_name" is created to record the names of students
maths_marks = [] # An empty list named "maths_marks" is created
physics_marks = [] # An empty list named "Physics_marks" is created
chemistry_marks = [] # an empty list named "Chemisty_marks" is created
mean = []
grades = []

number = 1
while number <= number_of_students:
    print()
    name = str(input("Please enter students name:"))
    student_name.append(name)

    while True:
        maths = int(input(f"Plese enter {name}'s Maths marks:"))
        if  0 <= maths <= 100:
            break
    maths_marks.append(maths)

    while True:
        physics = int(input(f"Plese enter {name}'s Physics marks:"))
        if 0 <= physics <= 100:
            break
    physics_marks.append(physics)

    while True:
        chemistry = int(input(f"Plese enter {name}'s chemistry marks:"))
        if 0 <= chemistry <= 100:
            break
    chemistry_marks.append(chemistry)

    print()

    total = maths + physics + chemistry
    average = total/3

    mean.append(average)

    if 75 <= average <= 100:
        grade = "A"
    elif  65 <= average <= 74.99:
        grade = "B"
    elif 50 <= average <= 64.99:
        grade = "C"
    elif 35 <= average <= 49.99:
        grade = "S"
    else:
        grade = "F"

    grades.append(grade)

    number += 1

class_average = sum(mean)/number_of_students

highest_average = max(mean)
lowest_average = min(mean)

highest_index = mean.index(highest_average)
first = student_name[highest_index]

lowest_index = mean.index(lowest_average)
last = student_name[lowest_index]

A_grades = grades.count("A")
B_grades = grades.count("B")
C_grades = grades.count("C")
S_grades = grades.count("S")
F_grades = grades.count("F")


index = 0
while index <= number_of_students-1:
    print()
    print(f"Student Name: {student_name[index]}")
    print(f"Maths Marks: {maths_marks[index]}") 
    print(f"Physics Marks: {physics_marks[index]}") 
    print(f"Chemistry Marks: {chemistry_marks[index]}") 
    print(f"Average: {mean[index]}")
    print(f"Grade: {grades[index]}")
    print()

    index += 1

print()
print(f"Class average: {class_average}")
print(f"Highest average:{highest_average} - {first} ")
print(f"Lowest average:{lowest_average} - {last}  ")
print(f"Number of 'A' grades - {A_grades}")
print(f"Number of 'B' grades - {B_grades}")
print(f"Number of 'C' grades - {C_grades}")
print(f"Number of 'S' grades - {S_grades}")
print(f"Number of 'F' grades - {F_grades}")