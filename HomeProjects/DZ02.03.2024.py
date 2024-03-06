def task3(leng: int, way: str, symbol: str):
    if way == "Horizontal":
        for i in range(leng):
            print(symbol, end="")
    elif way == "Vertical":
        for i in range(leng):
            print(symbol)
    else:
        print("Такого варианта нет")


def task4(a: int, b: int, c: int, d: int):
    return max(a, b, c, d)


def task5(minn: int, maxn: int):
    lst = [i for i in range(minn, maxn + 1)]
    return sum(lst)


def task6(num: int):
    if num == 2:
        return True
    d = 0
    for i in range(2, num):
        if not num % i:
            d += 1
    d = not bool(d)
    return d


def task7(num: int):
    return sum(list(map(int, list(str(num))))[:int((len(list(str(num))) / 2))]) == sum(
        list(map(int, list(str(num))))[int((len(list(str(num))) / 2)):])
