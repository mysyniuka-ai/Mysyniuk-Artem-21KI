def add():
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    print(f"Сума: {a + b}")

def mul():
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    print(f"Добуток: {a * b}")

def main():
    add()
    mul()
    add()

if __name__ == '__main__':
    main()
