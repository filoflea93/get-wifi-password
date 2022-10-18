import threading
import time
import os

class Person:
    def __init__(self, name):
        self.name = name

    def sayHello(self):
        print("Hello i'm " + self.name)

person1 = Person("Marco")

# Creating three sample threads
worker_1 = threading.Thread(target=person1)


# Starting three threads
worker_1.start()




