import math

lst_1 = [10, 12, 41, 1]
lst_2 = [2, 12, 13, 10]
lst_3 = [3, 12, 45, 0]


def hypotenuse(a: float, b: float) -> float:
    return math.sqrt(a ** 2 + b ** 2)


def lst_obsh(lst1: list, lst2: list) -> list:
    lst3 = []
    for i in lst1:
        if lst2.count(i) != 0:
            lst3.append(i)
    return lst3


def korlstret(posl: str) -> tuple:
    return posl.split(","), tuple(posl.split(","))


def lst_neobsh(lst1: list, lst2: list) -> None:
    lst3 = []
    for i in lst1:
        if lst2.count(i) == 0:
            lst3.append(i)
    print(lst3)


def lst_unik(lst1: list) -> bool:
    lst3 = []
    for i in lst1:
        if lst1.count(i) == 1:
            lst3.append(i)
    return len(lst3) == len(lst1)


def visok(num: int) -> None:
    if (num % 4 == 0 and num % 100 != 0 or num % 400 == 0) and num > 1562:
        print("YES")
    else:
        print("NO")


def zifra(x: float) -> None:
    print(int(x % 1 * 10))


def podstava(str2word: str) -> None:
    str2word = str2word.split(" ")
    prtword = "" + str2word[1] + " " + str2word[0]
    print(prtword)


def fword(strinf: str) -> None:
    strt = strinf.find("f")
    if strinf.find("f", strt + 1) != -1:
        print(strinf.find("f", strt + 1))
    else:
        if strt != -1:
            print("-1")
        else:
            print("-2")


def bilshzapop(lst) -> int:
    cnt = 0
    for i in range(len(lst)):
        if i < len(lst) - 1:
            if lst[i] < lst[i + 1]:
                cnt += 1
        else:
            break
    return cnt


print(hypotenuse(3, 4))
print(lst_obsh(lst_1, lst_2))
print(korlstret("1,6,45,671"))
lst_neobsh(lst_1, lst_2)
print(lst_unik(lst_1))
visok(1564)
zifra(4.61)
podstava("Trollik Komik")
fword("Horffog")
print(bilshzapop(lst_3))
