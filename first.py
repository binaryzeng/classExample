from abc import  ABC, abstractmethod

class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def set_price(self, price):
        if price > 0:
            self.__price = price

class Stream(ABC):
    def __init__(self):
        self.opened = False

    @abstractmethod
    def read(self):
        pass


    def open(self):
        if not self.opened:
            print("Already opened")
        else:
            print("open stream")
            self.opened = True

    def close(self):
        if self.opened:
            print("close stream")
            self.opened = False
        else:
            print("stream already")


class fileStream(Stream):
    def read(self):
        print("read from file stream")

class MemoryStream(Stream):
    def read(self):
        print("read from memory stream")  

class NetworkStream(Stream):
    def read(self):
        print("read from network stream")


class Flyer:
    def fly(self):
        pass
class Fish:
    def swim(self):
        pass 

class FlyingFilsh(Flyer, Fish):
    pass 

flyingfish = FlyingFilsh()
flyingfish.fly()
flyingfish.swim()

