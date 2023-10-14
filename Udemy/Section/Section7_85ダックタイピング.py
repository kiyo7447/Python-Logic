# -*- coding: utf-8 -*-
# IDE : PyCharm

# ダックタイピング

class Persion(object):
    def __init__(self, name, age = 1):
        self.name = name
        self.age = age
    
    def drive(self):
        if self.age >= 18:
            print("drive ok")
        else:
            raise Exception("No drive")

class Baby(Persion):
    def __init__(self, name, age = 1):
        if age < 18:
            super().__init__(name, age)
        else:
            raise ValueError

class Adult(Persion):
    def __init__(self, name, age = 18):
        if age >= 18:
            super().__init__(name, age)
        else:
            raise ValueError

baby = Baby("baby", 1)
adult = Adult("adult", 18)

class Car(object):
    def run(self):
        print("run")
    def drive(self, person):
        try:
            person.drive()
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)


car = Car()

print("drive baby")
car.drive(baby)
    
print("drive adult")
car.drive(adult)

