import random
def is_russian_letter(char):
    russian_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    russian_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    return char in russian_lower or char in russian_upper


def input_positive_int(prompt):
    while True:
        s = input(prompt)
        try:
            n = int(s)
        except ValueError:
            print("Ошибка: нужно ввести целое число (без букв и точки).")
            continue

        if n <= 0:
            print("Ошибка: число должно быть больше нуля.")
            continue

        return n


def task1():
    text = input("Введите текст: ")

    print("\nИсходный текст:")
    print(text)

    count_a = 0
    for ch in text:
        if ch == 'А' or ch == 'а' or ch == 'A' or ch == 'a':
            count_a += 1

    print("Буква 'А' встретилась", count_a, "раз(а).\n")


def task2():
    line = input("Введите строку из русских слов: ")

    print("\nИсходная строка:")
    print(line)


    for ch in line:
        if ch != ' ' and not is_russian_letter(ch) :
            print(f"Ошибка: символ '{ch}' не является русской буквой или пробелом!")
            return
    word_count = 0
    in_word = False
    for ch in line:
        if ch != ' ':
            if not in_word:
                word_count +=1
                in_word = True
        else:
            in_word = False

    print("Количество слов в строке:", word_count, "\n")


def generate_list(n):
    """Создаёт список из n случайных целых чисел от -10 до 10."""
    a = [0] * n
    i = 0
    while i < n:
        a[i] = random.randint(-10, 10)
        i += 1
    return a


def print_list(a, message):
    """Печатает список без использования готовых функций."""
    print(message, end='')
    i = 0
    while i < len(a):
        print(a[i], end=' ')
        i += 1
    print()


def task_list():
    n = input_positive_int("Введите размер списка n: ")

    a = generate_list(n)

    print_list(a, "\nИсходный список: ")

    # 1) сумма отрицательных элементов
    sum_negative = 0
    i = 0
    while i < len(a):
        if a[i] < 0:
            sum_negative += a[i]
        i += 1
    print("Сумма отрицательных элементов списка:", sum_negative)

    max_index = 0
    min_index = 0

    i = 1
    while i < len(a):
        if a[i] > a[max_index]:
            max_index = i
        if a[i] < a[min_index]:
            min_index = i
        i += 1

    print("Максимальный элемент:", a[max_index], " (индекс", max_index, ")")
    print("Минимальный элемент:", a[min_index], " (индекс", min_index, ")")

    if max_index > min_index:
        left = min_index + 1
        right = max_index
    else:
        left = max_index + 1
        right = min_index

    if left >= right:
        print("Между минимальным и максимальным элементами нет элементов.\n")
    else:
        prod = 1
        i = left
        while i < right:
            prod *= a[i]
            i += 1
        print("Произведение элементов между минимальным и максимальным:", prod, "\n")


def main():
    while True:
        print("Меню:")
        print("1 - Сколько раз в тексте встречается буква 'А'")
        print("2 - Количество слов в строке")
        print("3 - Работа со списком (сумма отрицательных, произведение между max и min)")
        print("0 - Выход")

        choice = input("Ваш выбор: ")

        if choice == '1':
            task1()
        elif choice == '2':
            task2()
        elif choice == '3':
            task_list()
        elif choice == '0':
            break
        else:
            print("Нет такого пункта меню.\n")


if __name__ == "__main__":
    main()