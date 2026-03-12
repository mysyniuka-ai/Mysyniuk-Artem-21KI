# Батьківський клас
class Human:
    def __init__(self, name, age):
        self.__name = name      # інкапсуляція (приватний атрибут)
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def speak(self):
        print("Людина говорить")

# Дочірній клас
class Student(Human):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    # поліморфізм (перевизначення методу)
    def speak(self):
        print("Студент навчається і говорить")

# використання
human1 = Human("Іван", 30)
student1 = Student("Андрій", 20, "ЛНУ")

human1.speak()
student1.speak()

print(student1.get_name(), student1.get_age())
