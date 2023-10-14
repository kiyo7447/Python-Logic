# -*- coding: utf-8 -*-

# class Car(object):
#     pass

# class ToyotaCar(Car):
#     pass


class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class ToyotaCar(Car):
    pass


class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False):
        # self.model = model
        super().__init__(model)
        self.enable_auto_run = enable_auto_run
        
    def run(self):
        print('super fast')
    def auto_run(self):
        print('auto run')


car = Car()
car.run()
print('###############')
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()
# toyota_car.auto_run() # AttributeError: 'ToyotaCar' object has no attribute 'auto_run'
print('###############')
tesla_car = TeslaCar('Model S')
print(tesla_car.model)
tesla_car.run()
tesla_car.auto_run()


