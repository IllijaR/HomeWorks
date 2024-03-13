def task1(lst: list) -> float:  # типо мы не знаем прилетит целое или нет
    prod = 1
    for i in lst:
        if i != 0:
            prod = prod * i
    return prod


print((lambda lst: min(lst))([10, -31, 31, 51]))  # лямбда функции - тоже функции


def task3(lst: list[int]) -> int:
    ctn = 0
    for i in lst:
        for j in range(2, i):
            if not i % j:
                break
        else:
            ctn += 1
    return ctn


def task4(lst: list[int], numb) -> int:
    ctn = 0
    for i in lst[:]:
        if i == numb:
            lst.remove(i)
            ctn += 1
        print(lst)
    return ctn


def task5(lst1: list, lst2: list) -> list:
    lst1.extend(lst2)
    return lst1


def task6(lst: list[int], pwr: int) -> list:
    return [eval((("i*" * pwr)[:-1])) for i in lst]
