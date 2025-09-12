class Person:#создание базового класса человек 
    def __init__(self, name: str, age: int):#конструктор класса: параметр имени, парметр возраста 
        """Базовый класс для представления человека."""
        self.name = name#сохранение имени в атребуте объект 
        self.age = age#сохранение возраста в атребуте объект

    def __str__(self):#метод для строкового представления объекта 
        return f"{self.name}, {self.age} лет"#возвращает формативную строку с именем и возрастом 


class Teacher(Person):#создание дочернего класса Teacher 
    def __init__(self, name: str, age: int, subject: str):#конструктор класса teacher с дополнительным параметром subject 
        """Дочерний класс для представления преподавателя.

        Args:
            name (str): Имя преподавателя
            age (int): Возраст
            subject (str): Преподаваемый предмет
        """
        super().__init__(name, age)  # вызов конструктора родительского класса 
        self.subject = subject #сохранения предмета преподования 
        self.students = []  # Список для хранения студентов

    def add_student(self, student: 'Student') -> bool: #метод добавления студента 
        """Добавляет студента в список.

        Args:
            student (Student): Объект класса Student

        Returns:
            bool: True если студент добавлен, False если уже существует 
        """
        if student in self.students: # проверка есть ли студент уже в списке 
            print(f"Ошибка: студент {student.name} уже есть в списке.") # вывод сообщения об ошибке если студент уже существует 
            return False #операция не выполнена 
        self.students.append(student) #добавления студента в список 
        print(f"Студент {student.name} добавлен к преподавателю {self.name}.") # вывод сообщения об успешном добавлении 
        return True#опрация выполнена 

    def remove_student(self, student_id: str) -> bool:# метод удаления студента по id 
        """Удаляет студента по ID.

        Args:
            student_id (str): ID студента

        Returns:
            bool: True если студент удален, False если не найден
        """
        for student in self.students: # цикл по всем студентам в списке 
            if student.student_id == student_id: # проверка совпадает ли id студента с исковым 
                self.students.remove(student)#удаление студента из списка 
                print(f"Студент {student.name} удален.")#вывод об успешно удалений 
                return True #студент найден и удален 
        print(f"Студент с ID {student_id} не найден.") #вывод сообщения если студент не найден 
        return False #студент не найден 

    def list_students(self): #метод вывода списка из всех студентов 
        """Выводит список всех студентов."""
        print(f"\nСписок студентов преподавателя {self.name} ({self.subject}):") #заголовок списка с именем преподователя и предметом 
        if not self.students:#проверка пуст ли список студентов 
            print("Нет студентов")
            return

        for i, student in enumerate(self.students, 1): #цикл по студентом с нумерацией 
            print(f"{i}. {student.name} (ID: {student.student_id}), средний балл: {student.get_average():.2f}")# вывод информаций о каждом студенте 


# Пример использования
if __name__ == "__main__":
    # Создаем преподавателя
    math_teacher = Teacher("Мария Петровна", 45, "Математика")

    # Создаем студентов
    student1 = Student("Иван Иванов", "S001")
    student1.add_grade(8)
    student1.add_grade(9)

    student2 = Student("Елена Смирнова", "S002")
    student2.add_grade(7)
    student2.add_grade(6.5)

    # Добавляем студентов к преподавателю
    math_teacher.add_student(student1)
    math_teacher.add_student(student2)

    # Выводим список студентов
    math_teacher.list_students()

    # Пробуем добавить существующего студента
    math_teacher.add_student(student1)

    # Удаляем студента
    math_teacher.remove_student("S001")

    # Выводим обновленный список

    math_teacher.list_students()
