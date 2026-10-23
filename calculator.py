def divide(a, b):
    if b == 0:
        return "Ошибка: Деление на ноль невозможно!"
    return a / b

if __name__ == "__main__":
    print(divide(10, 2))  # Должно вывести 5.0
    print(divide(5, 0))   # Должно вывести сообщение об ошибке
