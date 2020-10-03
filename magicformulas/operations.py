from abc import ABCMeta, abstractmethod


class Operation(metaclass=ABCMeta):
    def __init__(self, func, *args):
        self.func = func
        self.args = args

    @abstractmethod
    def compute(self):
        pass
