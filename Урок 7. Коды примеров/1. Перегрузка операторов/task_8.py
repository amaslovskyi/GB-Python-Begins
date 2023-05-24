"""__call__"""


class MyClass:
    def __init__(self, param):
        self.param = param

    def __call__(self, *args, **kwargs):
        print("!")


obj = MyClass('!')
obj()
