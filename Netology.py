class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            print("Ошибка: студент или лектор не прикреплены к курсу.")

    def average_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg_grade = self.average_grade()
        courses_in_progress = ", ".join(self.courses_in_progress)
        finished_courses = ", ".join(self.finished_courses)
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
            f"Курсы в процессе изучения: {courses_in_progress}\n"
            f"Завершенные курсы: {finished_courses}"
        )

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() == other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg_grade = self.average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade:.1f}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() == other.average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, grade):
        if course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            print("Ошибка: студент или эксперт не прикреплены к курсу.")

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"



lecturer1 = Lecturer("John", "Doe")
lecturer2 = Lecturer("Jane", "Smith")
reviewer1 = Reviewer("Alice", "Johnson")
reviewer2 = Reviewer("Bob", "Brown")
student1 = Student("Bob", "Davis")
student2 = Student("Carol", "Miller")


lecturer1.courses_attached.append("Python")
lecturer2.courses_attached.append("Python")
reviewer1.courses_attached.append("Python")
reviewer2.courses_attached.append("Python")


student1.courses_in_progress.append("Python")
student2.courses_in_progress.append("Python")
student1.finished_courses.append("Math")
student2.finished_courses.append("History")


reviewer1.rate_student(student1, "Python", 8)
reviewer2.rate_student(student2, "Python", 9)


student1.rate_lecturer(lecturer1, "Python", 9)
student2.rate_lecturer(lecturer2, "Python", 8)


print(reviewer1)
print(lecturer1)
print(student1)


print(lecturer1 > lecturer2)


print(student1 == student2)


def average_grade_students(students, course):
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades.extend(student.grades[course])
    if all_grades:
        return sum(all_grades) / len(all_grades)
    else:
        return 0

def average_grade_lecturers(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])
    if all_grades:
        return sum(all_grades) / len(all_grades)
    else:
        return 0


students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print("Средняя оценка студентов по курсу Python:", average_grade_students(students, "Python"))
print("Средняя оценка лекторов по курсу Python:", average_grade_lecturers(lecturers, "Python"))
