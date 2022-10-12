import abc


class Event:
    def __init__(self, time, weight):
        self.t = time
        self.w = weight
        self.data = {}


class Events(list):
    pass


class Generator(abc.ABC):
    @abc.abstractmethod
    def generate(self):
        pass

    def pipe(self):
        pass
