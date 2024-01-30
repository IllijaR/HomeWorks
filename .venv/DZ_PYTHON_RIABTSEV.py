import string


def task1(size, symbol, choose):
    if choose == 0:
        print("Фигура 1:")
        for i in range(size, 0, -1):
            print(' ' * (size - i) + symbol * i)
    elif choose == 1:
        print("\nФигура 2:")
        for i in range(1, size + 1):
            print(symbol * i)
    elif choose == 2:
        print("\nФигура 3:")
        for i in range(size, 0, -1):
            print(" " * (size - i), end="")
            print(symbol * (2 * i - 1))
    elif choose == 3:
        print("\nФигура 4:")
        for i in range(1, size + 1):
            print(" " * (size - i), end="")
            print(symbol * (2 * i - 1))
    elif choose == 4:
        print("\nФигура 5:")
        for i in range(size, 0, -1):
            print(" " * (size - i), end="")
            print(symbol * (2 * i - 1))
        for i in range(2, size):
            print(" " * (size - i), end="")
            print(symbol * (2 * i - 1))
        print(symbol * ((size * 2) - 1))
    elif choose == 5:
        print("\nФигура 6:")
        for i in range(1, size + 1):
            print(symbol * i)
        for i in range(size - 1, 0, -1):
            print(symbol * i)
    elif choose == 6:
        print("\nФигура 7:")
        for i in range(size):
            print(" " * (size - i - 1) + symbol * (i + 1))
        for i in range(size):
            print(" " * i + symbol * (size - i))
    elif choose == 7:
        print("\nФигура 8:")
        for i in range(size * 2 // 2):
            print(symbol * (i + 1) + " " * (size * 2 - 2 * (i + 1)) + symbol * (i + 1))
        print(symbol * size * 2)
        for i in range(size * 2 // 2 - 1, -1, -1):
            print(symbol * (i + 1) + " " * (size * 2 - 2 * (i + 1)) + symbol * (i + 1))
    elif choose == 8:
        print("\nФигура 9:")
        for i in range(size, 0, -1):
            print(symbol * i)
    elif choose == 9:
        print("\nФигура 10:")
        for i in range(1, size + 1):
            print(" " * (size - i) + symbol * i)
    else:
        print("Я не знаю таких цифр...")


# обводку не сделал(выходит непонятная каша)

def task2(palindrom):
    check = palindrom.replace(" ", "")
    for i in range(len(string.punctuation)):
        check = check.replace(string.punctuation[i], "")
    check = check.lower()
    check_rev = ''.join(reversed(check))
    if check == check_rev:
        print("Это палиндром")
    else:
        print("Это не палиндром")


def task3(text, reserved_words):
    reserved_words = reserved_words[::-1]
    reserved_words = reserved_words.split()
    print(reserved_words)
    for i in text.split():
        if i.lower() in reserved_words:
            text = text.replace(i, i.upper())

    print(text)


def task4(text):
    n = 0
    for i in range(len(text)):
        if text[i - 1] in ".?!" and text[i] not in ".?!":
            n += 1
    print(n)


"""sizinput = int(input("Введи размер: "))
symbinput = input("Выбери символ фигуры: ")
choseinput = int(input("Введи цифру(это если что от 0-9): "))
task1(sizinput, symbinput, choseinput)"""
