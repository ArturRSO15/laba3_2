class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def __str__(self):
        return f"Student {self.name} (ID: {self.student_id})"

    def __eq__(self, other):
        return self.student_id == other.student_id

    def __len__(self):
        return len(self.grades)


# Пример использования
s1 = Student("Иван", "123")
s1.grades = [5, 4, 3]
s2 = Student("Петр", "123")

print(s1)  # Student Иван (ID: 123)
print(s1 == s2)  # True (сравниваем по ID)
print(len(s1))  # 3 (количество оценок)