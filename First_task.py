class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Создаем экземпляры объектов
best_student = Student('Руслан', 'Еманов', 'мужской')
best_student.courses_in_progress += ['Python']

lecturer = Lecturer('Иван', 'Иванов')
lecturer.courses_attached += ['Python']

reviewer = Reviewer('Петр', 'Петров')
reviewer.courses_attached += ['Python']

# Оцениваем студента через лектора
lecturer.rate_hw(best_student, 'Python', 9)
lecturer.rate_hw(best_student, 'Python', 8)
lecturer.rate_hw(best_student, 'Python', 7)

# Оцениваем студента через эксперта
reviewer.rate_hw(best_student, 'Python', 6)
reviewer.rate_hw(best_student, 'Python', 5)
reviewer.rate_hw(best_student, 'Python', 4)

# Выводим оценки студента
print(f'Оценки студента {best_student.name}: {best_student.grades}')