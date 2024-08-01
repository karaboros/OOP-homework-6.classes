class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def get_average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        num_grades = sum(len(grades) for grades in self.grades.values())
        return total_grades / num_grades if num_grades != 0 else 0
    
    def __str__(self):
        avg_grade = self.get_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade:.1f}\nКурсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}"
        
class Mentor:
    def __init__(self, name, surname): 
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor): 
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Lecturer(Mentor): 
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        num_grades = sum(len(grades) for grades in self.grades.values())
        return total_grades / num_grades if num_grades != 0 else 0
    
    def __str__(self):
        avg_grade = self.get_average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade:.1f}"
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()
    
def average_student_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0

def average_lecturer_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0

# Создаем студентов
student1 = Student('Алиса', 'Босоногова', 'female')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Git']

student2 = Student('Витя', 'Чеснок', 'male')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Java']

# Создаем лекторов
lecturer1 = Lecturer('Питер', 'Паркер')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Том', 'Харди')
lecturer2.courses_attached += ['Python']

# Создаем проверяющих
reviewer1 = Reviewer('Денис', 'Штырь')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Леха', 'Камень')
reviewer2.courses_attached += ['Python']

# Оценка домашних заданий
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 7)

# Оценка лекций
student1.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer2, 'Python', 10)
student2.rate_lecture(lecturer1, 'Python', 7)
student2.rate_lecture(lecturer2, 'Python', 8)

# Вывод средней оценки студентов
print(f"{student1.name} средняя оценка: {student1.get_average_grade()}")
print(f"{student2.name} средняя оценка: {student2.get_average_grade()}")

# Вывод средней оценки лекторов
print(f"{lecturer1.name} средняя оценка: {lecturer1.get_average_grade()}")
print(f"{lecturer2.name} средняя оценка: {lecturer2.get_average_grade()}")

# Применение функций для подсчета средней оценки:
students = [student1, student2]
lecturers = [lecturer1, lecturer2]

average_hw_grade = average_student_grade(students, 'Python')
average_lecture_grade = average_lecturer_grade(lecturers, 'Python')

print(f"Средняя оценка за домашние задания на курсе Python: {average_hw_grade}")
print(f"Средняя оценка за лекции на курсе Python: {average_lecture_grade}")