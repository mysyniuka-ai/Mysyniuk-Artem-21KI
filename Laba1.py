age = 16              # зберігаємо вік
height = 1.78         # зберігаємо зріст
name = "Artem"        # зберігаємо ім’я
is_student = True     # чи студент (так/ні)
grades = [12, 11, 10, 9]   # список оцінок
coordinates = (50.45, 30.52)  # координати міста
person = {"name": "Artem", "age": 16}  # словник з даними про людину
unique_numbers = {1, 2, 3, 3}  # множина унікальних чисел (дублікат зникне)

variables = {          # створюємо словник зі всіма змінними
    "age": age,
    "height": height,
    "name": name,
    "is_student": is_student,
    "grades": grades,
    "coordinates": coordinates,
    "person": person,
    "unique_numbers": unique_numbers
}

for var_name, value in variables.items():   # перебираємо всі змінні
    print(f"{var_name}, {type(value).__name__} : {value}")  # виводимо назву, тип і значення

print("\n--- Оператори ---")  # робимо розділ для операторів

a = 10          # число 10
b = 3           # число 3
print("Додавання:", a + b)       # додаємо числа
print("Віднімання:", a - b)      # віднімаємо числа
print("Множення:", a * b)        # множимо числа
print("Ділення:", a / b)         # ділимо числа (звичайно)
print("Цілочисельне ділення:", a // b)  # ділення без дробу
print("Остача від ділення:", a % b)     # залишок після ділення
print("Піднесення до степеня:", a ** b) # підносимо до степеня

print("a == b:", a == b)   # чи рівні числа
print("a != b:", a != b)   # чи різні числа
print("a > b:", a > b)     # чи більше a
print("a < b:", a < b)     # чи менше a
print("a >= b:", a >= b)   # чи більше або дорівнює
print("a <= b:", a <= b)   # чи менше або дорівнює

x = True        # правда
y = False       # неправда
print("x and y:", x and y)   # обидва мають бути True
print("x or y:", x or y)     # хоча б один True
print("not x:", not x)       # заперечення (True -> False)

c = 5           # число 5
c += 2          # додаємо 2 до c
print("c після += 2:", c)  # виводимо результат
c *= 3          # множимо c на 3
print("c після *= 3:", c)  # виводимо результат

print("Чи є 12 у списку grades?", 12 in grades)   # перевіряємо, чи є число 12 у списку
print("Чи є 15 у списку grades?", 15 in grades)   # перевіряємо, чи є число 15 у списку
