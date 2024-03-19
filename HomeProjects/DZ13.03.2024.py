from tkinter import *


def task1(name1: str, name2: str):
    with open(file=name1, mode="r", encoding="UTF-8") as file1:
        result1 = file1.readlines()
        result1 = [i.strip('\n') for i in result1]
    with open(file=name2, mode="r", encoding="UTF-8") as file2:
        result2 = file2.readlines()
        result2 = [i.strip('\n') for i in result2]
    for i in range(len(result1)):
        if result2[i]:
            if result1[i] != result2[i]:
                print(f"Не совпали: \n{result1[i]}\nА ТАКЖЕ\n{result2[i]}\n\n")
        else:
            break
    return True if result1 == result2 else False


def task2(name1: str, newname: str) -> None:
    conlst = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч',
              'ш', 'щ', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x',
              'y', 'z']
    vowlst = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'a', 'e', 'i', 'o', 'u']
    strin = 0
    symb = 0
    vowels = 0
    consonants = 0
    digits = 0
    with open(file=name1, mode="r", encoding="UTF-8") as file:
        result = file.readlines()
        result = [i.strip('\n') for i in result]
    for i in result:
        strin += 1
        for j in i:
            symb += 1
            if j in vowlst:
                vowels += 1
            elif j in conlst:
                consonants += 1
            elif j.isdigit():
                digits += 1
    text = f"Символов: {symb}\nСтрок: {strin},\nГласных: {vowels},\nСогласных: {consonants},\nЧисла: {digits}."
    with open(file=newname, mode="w", encoding="UTF-8") as file1:
        file1.write(text)


def task3(name1: str, newname: str) -> None:
    with open(file=name1, mode="r", encoding="UTF-8") as file:
        result = file.readlines()
        result.pop(-1)
    res = "".join(result)
    with open(file=newname, mode="w", encoding="UTF-8") as file1:
        file1.write(res)


def task4(name1: str) -> int:
    with open(file=name1, mode="r", encoding="UTF-8") as file:
        result = file.readlines()
        result = [i.strip('\n') for i in result]
    return len(max(result, key=len))


def task5(name1: str, word: str) -> int:
    cnt = 0
    with open(file=name1, mode="r", encoding="UTF-8") as file:
        result = file.readlines()
        result = [i.strip('\n') for i in result]
    for i in result:
        cnt += i.count(word)
    return cnt


def task6(name1: str, word: str, replace: str) -> None:
    with open(file=name1, mode="r", encoding="UTF-8") as file:
        result = file.readlines()
    for i in range(len(result)):
        result[i] = result[i].replace(word, replace)
    res = "".join(result)
    with open(file=name1, mode="w", encoding="UTF-8") as file1:
        file1.write(res)


def task7(rowncol: int) -> None:
    root = Tk()
    W = 1000
    H = 1000
    root.geometry(f"{W}x{H}")
    root.resizable(False, False)
    background = Frame(root, bg="brown")
    background.grid()
    ctn = 0
    for i in range(rowncol):
        for j in range(rowncol):
            if ctn % 2 == 0:
                cell = Frame(background, bg="white", width=W / rowncol, height=H / rowncol)
            else:
                cell = Frame(background, bg="black", width=W / rowncol, height=H / rowncol)
            cell.grid(row=i + 1, column=j + 1, padx=5, pady=10)
            ctn += 1
        ctn += 1
    mainloop()
