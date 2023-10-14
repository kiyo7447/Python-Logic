# -*- coding: utf-8 -*-

class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class ToyotaCar(Car):
    pass


class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False, passwd='123'):
        # self.model = model
        super().__init__(model)
        self._enable_auto_run = enable_auto_run
        self.passwd = passwd

# ■ プロパティーを使った属性の設定 Start
    @property
    def enable_auto_run(self):
        """Get the auto run status."""
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        """Set the auto run status."""
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

        self._enable_auto_run = is_enable
# ■ プロパティーを使った属性の設定 End

    def run(self):
        print('super fast')
    def auto_run(self):
        print('auto run')

tesla_car = TeslaCar('Model S', passwd='456')
# tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)

tesla_car = TeslaCar('Model S', passwd='123')
# tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)
# パスワードがミスっているからValueErrorが発生する
#ValueErrorが発生すると、tesla_car.enable_auto_run = Trueは実行されない
try:
    tesla_car.enable_auto_run = True
except ValueError:
    print('ValueError')
else:
    print(tesla_car.enable_auto_run)

# __始まりのクラス変数はエラーになる。
# print(tesla_car.__enable_auto_run)
# tesla_car._enable_auto_run = False
# print(tesla_car._enable_auto_run)
