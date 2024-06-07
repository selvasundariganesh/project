class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def remove_grade(self, grade):
        if grade in self.grades:
            self.grades.remove(grade)
            return True
        return False

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def __str__(self):
        return f"Name: {self.name}, Grades: {self.grades}, Average: {self.average_grade():.2f}"

class GradeSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                return True
        return False

    def list_students(self):
        for student in self.students:
            print(student)

    def student_with_highest_average(self):
        return max(self.students, key=lambda student: student.average_grade(), default=None)

    def student_with_lowest_average(self):
        return min(self.students, key=lambda student: student.average_grade(), default=None)


grades_system = GradeSystem()
student1 = Student("Alice")
student1.add_grade(90)
student1.add_grade(80)
grades_system.add_student(student1)

student2 = Student("Bob")
student2.add_grade(70)
student2.add_grade(60)
grades_system.add_student(student2)

print("All students and their grades:")
grades_system.list_students()

print("\nStudent with highest average:")
print(grades_system.student_with_highest_average())

print("\nStudent with lowest average:")
print(grades_system.student_with_lowest_average())
