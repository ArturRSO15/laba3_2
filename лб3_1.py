class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        if isinstance(grade, (int, float)) and 0 <= grade <= 10:
            self.grades.append(grade)
            print(f"Оценка {grade} добавлена.")
        else:
            print("Ошибка: оценка должна быть числом от 0 до 10.")

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        print(f"Студент: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Оценки: {self.grades if self.grades else 'Нет оценок'}")
        print(f"Средний балл: {self.get_average():.2f}")

# Пример использования:
student = Student("Иван Иванов", "12345")
student.add_grade(8)
student.add_grade(9.5)
student.add_grade(11)  # Ошибка
student.display_info()
