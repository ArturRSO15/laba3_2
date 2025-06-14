class Person:
    def __init__(self, name: str, age: int):
        """Базовый класс для представления человека."""
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} лет"


class Teacher(Person):
    def __init__(self, name: str, age: int, subject: str):
        """Дочерний класс для представления преподавателя.

        Args:
            name (str): Имя преподавателя
            age (int): Возраст
            subject (str): Преподаваемый предмет
        """
        super().__init__(name, age)  # Инициализация атрибутов родительского класса
        self.subject = subject
        self.students = []  # Список для хранения студентов

    def add_student(self, student: 'Student') -> bool:
        """Добавляет студента в список.

        Args:
            student (Student): Объект класса Student

        Returns:
            bool: True если студент добавлен, False если уже существует
        """
        if student in self.students:
            print(f"Ошибка: студент {student.name} уже есть в списке.")
            return False
        self.students.append(student)
        print(f"Студент {student.name} добавлен к преподавателю {self.name}.")
        return True

    def remove_student(self, student_id: str) -> bool:
        """Удаляет студента по ID.

        Args:
            student_id (str): ID студента

        Returns:
            bool: True если студент удален, False если не найден
        """
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"Студент {student.name} удален.")
                return True
        print(f"Студент с ID {student_id} не найден.")
        return False

    def list_students(self):
        """Выводит список всех студентов."""
        print(f"\nСписок студентов преподавателя {self.name} ({self.subject}):")
        if not self.students:
            print("Нет студентов")
            return

        for i, student in enumerate(self.students, 1):
            print(f"{i}. {student.name} (ID: {student.student_id}), средний балл: {student.get_average():.2f}")


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