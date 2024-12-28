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

    def avg_grade(self):
        total_sum = 0
        grades_count = 0
        for course, grades in self.grades.items():
            total_sum += sum(grades)
            grades_count += len(grades)
        if grades_count == 0:
            return 0
        return round(total_sum / grades_count, 1)

    def __str__(self):
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        average_grade = self.avg_grade()
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {average_grade}\n' \
               f'Курсы в процессе изучения: {courses_in_progress_str}\n' \
               f'Завершенные курсы: {finished_courses_str}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Невозможно сравнить объекты разных типов")
            return False
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            print("Невозможно сравнить объекты разных типов")
            return False
        return self.get_average_grade() <= other.get_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            print("Невозможно сравнить объекты разных типов")
            return False
        return self.get_average_grade() > other.get_average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            print("Невозможно сравнить объекты разных типов")
            return False
        return self.get_average_grade() >= other.get_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print("Невозможно сравнить объекты разных типов")
            return False
        return self.get_average_grade() == other.get_average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grade(self):
        total_sum = 0
        grades_count = 0
        for course, grades in self.grades.items():
            total_sum += sum(grades)
            grades_count += len(grades)
        if grades_count == 0:
            return 0
        return round(total_sum / grades_count, 1)

    def __str__(self):
        average_grade = self.avg_grade()
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {average_grade}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Невозможно сравнить объекты разных типов")
            return False
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print("Невозможно сравнить объекты разных типов")
            return False
        return self.get_average_grade() <= other.get_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print("Невозможно сравнить объекты разных типов")
            return False
        return self.get_average_grade() > other.get_average_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            print("Невозможно сравнить объекты разных типов")
            return False
        return self.get_average_grade() >= other.get_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print("Невозможно сравнить объекты разных типов")
            return False
        return self.get_average_grade() == other.get_average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'



student = Student('Руслан', 'Еманов', 'мужской')
student.courses_in_progress += ['Python', 'Git']
student.finished_courses += ['Введение в программирование']

lecturer = Lecturer('Иван', 'Иванов')
lecturer.courses_attached += ['Python']

reviewer = Reviewer('Петр', 'Петров')
reviewer.courses_attached += ['Python']

# Оценка 1
reviewer.rate_hw(student, 'Python', 9)
reviewer.rate_hw(student, 'Python', 8)
reviewer.rate_hw(student, 'Python', 7)

# Оценка 2
student.rate_lecturer(lecturer, 'Python', 10)
student.rate_lecturer(lecturer, 'Python', 9)
student.rate_lecturer(lecturer, 'Python', 8)

print(reviewer)
print(lecturer)
print(student)

another_student = Student('Алексей', 'Александров', 'мужской')
another_student.courses_in_progress += ['Python', 'JavaScript']
another_student.finished_courses += ['Алгоритмы и структуры данных']
reviewer.rate_hw(another_student, 'Python', 10)
reviewer.rate_hw(another_student, 'Python', 10)
reviewer.rate_hw(another_student, 'Python', 10)

if student < another_student:
    print("Другой студент имеет более высокую среднюю оценку.")
else:
    print("Первый студент имеет более высокую среднюю оценку.")

another_lecturer = Lecturer('Сергей', 'Сергеев')
another_lecturer.courses_attached += ['JavaScript']
student.rate_lecturer(another_lecturer, 'JavaScript', 9)
student.rate_lecturer(another_lecturer, 'JavaScript', 9)
student.rate_lecturer(another_lecturer, 'JavaScript', 9)

if lecturer > another_lecturer:
    print("У первого лектора средняя оценка выше.")
else:
    print("У второго лектора средняя оценка выше.")