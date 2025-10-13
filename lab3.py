# Створюємо порожній словник, де:
# ключ — ім’я студента (str)
# значення — його оцінка (int)
students = {}

# Безкінечний цикл для введення даних
while True:
    # Користувач вводить ім’я студента
    name = input("Ім'я студента (stop - завершити): ")
    # Якщо введено "stop", цикл переривається
    if name.lower() == "stop":
        break
    # Інакше запитуємо оцінку
    grade = int(input("Оцінка (1-12): "))
    # Додаємо ім’я та оцінку до словника
    students[name] = grade

# Виводимо список усіх студентів і їх оцінок
print("\nСписок студентів:")
for n, g in students.items():
    print(f"{n}: {g}")

# Якщо список не порожній, проводимо підрахунки
if students:
    # Розрахунок середнього бала по групі
    avg = sum(students.values()) / len(students)
    print(f"\nСередній бал: {avg:.2f}")

    # Формуємо списки студентів за рівнями успішності
    exc = [n for n, g in students.items() if g >= 10]        # Відмінники (10–12)
    good = [n for n, g in students.items() if 7 <= g <= 9]   # Хорошисти (7–9)
    bad = [n for n, g in students.items() if 4 <= g <= 6]    # Відстаючі (4–6)
    fail = [n for n, g in students.items() if g <= 3]        # Не здали (1–3)

    # Виводимо результати
    print(f"Відмінники ({len(exc)}): {', '.join(exc) or 'немає'}")
    print(f"Хорошисти ({len(good)}): {', '.join(good) or 'немає'}")
    print(f"Відстаючі ({len(bad)}): {', '.join(bad) or 'немає'}")
    print(f"Не здали ({len(fail)}): {', '.join(fail) or 'немає'}")
