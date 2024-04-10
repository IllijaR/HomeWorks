from random import randint


class Student:

    def __init__(self, name):
        self.name = name
        self.progress = 0
        self.happiness = 50
        self.money = 0
        self.alive = True

    def to_study(self):
        print("Study..")
        self.progress += 0.3
        self.happiness -= 5
        if self.money < 10:
            self.to_work()

    def to_sleep(self):
        print("Sleep..")
        self.progress -= 0.2
        self.happiness += 3

    def to_chill(self):
        print("Chill..")
        self.progress -= 0.1
        self.happiness += 3
        self.money -= 5

    def to_work(self):
        print("Work..")
        self.money += randint(10, 50)
        self.happiness -= 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Dead by parents")
            self.alive = False
        elif self.happiness < 0:
            print("Dead inside")
            self.alive = False
        elif self.progress > 5:
            print("Year passed, but there is death because of real life")
            self.alive = False

    def summary(self):
        print(f"Happiness: {round(self.happiness)}\n"
              f"Progress: {round(self.progress, 1)}\n"
              f"Money: {self.money} ")

    def live(self, day):
        action = randint(1, 4)
        print(f"Day {day} of {self.name}'s life")

        if self.happiness < 20:
            self.to_chill()
        elif self.progress < 1:
            self.to_study()
        elif self.money < 20 and action != 4:
            self.to_work()
        else:
            if action == 1:
                self.to_study()
            elif action == 2:
                self.to_sleep()
            elif action == 3:
                self.to_chill()
            elif action == 4:
                self.to_work()

        self.summary()
        self.is_alive()


X1337 = Student("X1337")
for i in range(365):
    if not X1337.alive:
        break
    X1337.live(i)
else:
    print("Year passed, but there is death because of real life")
