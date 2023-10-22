def sort_students(students):
    students.sort(key=lambda x: x.cgpa, reverse=True)
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

students = [
    Student("Jimin", "A001", 3.8),
    Student("Taehyung", "A002", 3.5),
    Student("Jungkook", "A003", 3.9),
]

sort_students(students)

for student in students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
