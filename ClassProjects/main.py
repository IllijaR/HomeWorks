def task1(n):
    x = 0
    for i in range(n):
        for j in range(i):
            x += 1
            print(x, end=" ")
        print("")


def task2(n):
    for i in range(n):
        for j in range(i):
            print(j + 1, end="")
        for k in range(i - 1, 0, -1):
            print(k, end="")
        print("")


def task3(a, b):
    if a <= b:
        lst = [i for i in range(a, b + 1)]
        maxx = 0
        n = 0
        maxdilnik = 0
        for i in range(len(lst)):
            x = 0
            sdilnik = 0
            for j in range(1, lst[i] + 1):
                if lst[i] % j == 0:
                    x += 1
                    sdilnik += j
            if x >= maxx:
                maxx = x
                maxdilnik = sdilnik
                n = lst[i]
        print(f"Число {n} колво дільників {maxx} сумма дільників {maxdilnik}")
    else:
        print("a>b!!!!")
# В этой задачи нету условий про делитель равен 1 и
# число которое делиться само на себя,
# а также включает ли диапозон числа(я сделал что включает)


task1(5)
task2(5)
task3(10, 100)
