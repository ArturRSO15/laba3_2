class Student: #создание класса student 
    def __init__(self, name, student_id):# конструктор класса-специальный метод который вызывается для создании нового объекта 
        self.name = name#сохранение имени в атрибуте объекта 
        self.student_id = student_id#сохранение id в атрибуте объекта 
        self.grades = []#инициализация пустого списка 

    def __str__(self):#метод для строкового представления объекта 
        return f"Student {self.name} (ID: {self.student_id})"#возвращает форматированную строку с информацией о студенте 

    def __eq__(self, other):#метод для сравнения объектов на равенство 
        return self.student_id == other.student_id#сравнивает студентов по их id 

    def __len__(self):#метод для получения длинны объекта 
        return len(self.grades)#возвращает количество оценок у студента 


# Пример использования
s1 = Student("Иван", "123")
s1.grades = [5, 4, 3]
s2 = Student("Петр", "123")

print(s1)  # Student Иван (ID: 123)
print(s1 == s2)  # True (сравниваем по ID)

print(len(s1))  # 3 (количество оценок)
