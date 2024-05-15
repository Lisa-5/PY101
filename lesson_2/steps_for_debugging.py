def process_student(student_data):
    name = student_data.get('name')
    grade = student_data.get('grade')
    return (name, grade)

def average_grade(grades_collection):
    total = sum(grades_collection)
    average = total / len(grades_collection)
    return average

students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob'},
    {'name': 'Jack', 'grade': 72},
    {'name': 'Jane', 'grade': 75},
]

def collect_grades(student_collection):
    grades = []
    for student in student_collection:
        name, grade = process_student(student)
        if grade:
            grades.append(grade)
    return grades

student_grades = collect_grades(students)
print(average_grade(student_grades))
# TypeError: unsupported operand type(s) for +: 'int'
# and 'NoneType'