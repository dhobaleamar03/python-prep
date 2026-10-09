# OOP abstraction

# a program that requires every vehicle subclass to define its own start() method.
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):      #subclasses must implement this method
        pass


class Car(Vehicle):
    def start(self):         #provided the implementation for Car
        print("Car started")


car = Car()      # created a Car object
car.start()       #started the car