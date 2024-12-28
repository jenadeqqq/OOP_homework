class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.lecturers_grades = {}
    
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}                        # слвоарь с оценками


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

student = Student('Руслан', 'Еманов', 'мужской')
student.courses_in_progress += ['Python']

lecturer = Lecturer('Иван', 'Иванов')
lecturer.courses_attached += ['Python']

reviewer = Reviewer('Петр', 'Петров')
reviewer.courses_attached += ['Python']

# Оценка экспертом
reviewer.rate_hw(student, 'Python', 9)
reviewer.rate_hw(student, 'Python', 8)
reviewer.rate_hw(student, 'Python', 7)

# Оценка  студентом
student.rate_lecturer(lecturer, 'Python', 10)
student.rate_lecturer(lecturer, 'Python', 9)
student.rate_lecturer(lecturer, 'Python', 8)

print(f'Оценки студента {student.name}: {student.grades}')
print(f'Оценки лектора {lecturer.name}: {lecturer.grades}')