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

    def get_average_grade(self):
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
        average_grade = self.get_average_grade()
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

    def get_average_grade(self):
        total_sum = 0
        grades_count = 0
        for course, grades in self.grades.items():
            total_sum += sum(grades)
            grades_count += len(grades)
        if grades_count == 0:
            return 0
        return round(total_sum / grades_count, 1)

    def __str__(self):
        average_grade = self.get_average_grade()
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


def calculate_students_average_grade(students, course):
    total_sum = 0
    grades_count = 0
    for student in students:
        if course in student.grades:
            total_sum += sum(student.grades[course])
            grades_count += len(student.grades[course])
    if grades_count == 0:
        return 0
    return round(total_sum / grades_count, 1)


def calculate_lecturers_average_grade(lecturers, course):
    total_sum = 0
    grades_count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_sum += sum(lecturer.grades[course])
            grades_count += len(lecturer.grades[course])
    if grades_count == 0:
        return 0
    return round(total_sum / grades_count, 1)



student1 = Student('Руслан', 'Еманов', 'мужской')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Анна', 'Андреева', 'женский')
student2.courses_in_progress += ['Python', 'C++']
student2.finished_courses += ['Основы программирования']

lecturer1 = Lecturer('Иван', 'Иванов')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Ольга', 'Петрова')
lecturer2.courses_attached += ['C++']

reviewer1 = Reviewer('Петр', 'Петров')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Светлана', 'Светлова')
reviewer2.courses_attached += ['C++']


reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Python', 7)

reviewer2.rate_hw(student2, 'C++', 10)
reviewer2.rate_hw(student2, 'C++', 9)
reviewer2.rate_hw(student2, 'C++', 8)


student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Python', 8)

student2.rate_lecturer(lecturer2, 'C++', 9)
student2.rate_lecturer(lecturer2, 'C++', 9)
student2.rate_lecturer(lecturer2, 'C++', 9)


print(reviewer1)
print(lecturer1)
print(student1)

print(reviewer2)
print(lecturer2)
print(student2)


if student1 < student2:
    print("Студент 2 имеет более высокую среднюю оценку.")
else:
    print("Студент 1 имеет более высокую среднюю оценку.")

if lecturer1 > lecturer2:
    print("Лектор 1 имеет более высокую среднюю оценку.")
else:
    print("Лектор 2 имеет более высокую среднюю оценку.")


students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

avg_student_grade_python = calculate_students_average_grade(students_list, 'Python')
avg_lecturer_grade_python = calculate_lecturers_average_grade(lecturers_list, 'Python')

print(f"Средняя оценка за домашние задания по Python: {avg_student_grade_python}")
print(f"Средняя оценка за лекции по Python: {avg_lecturer_grade_python}")