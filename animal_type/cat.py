#!/usr/bin/env python


import random
from animal_type.makenoise import FeNoise
from animal_parent.feline import Feline

fenoise = FeNoise()

class Cat(Feline):

    def __init__(self, name):
        super().__init__(name, fenoise)

    def wake(self):
        print("Cat " + self.name + " type " + self.type + " is waked up by the zookeper!!")
        super().roam()

    def call(self):
        print("Cat " + self.name + " type " + self.type + " is called up by the zookeper!!")

    def feed(self):
        print("Cat " + self.name + " type " + self.type + " is fed up by the zookeper!!")

    def exercise(self):
        print("Cat " + self.name + " type " + self.type + " is exercised by the zookeper!!")

    def sleep(self):
        print(super(Feline, self).sleep() + " Cat " + " with name " + self.name + " type " + self.type)

    def random(self):
        print("Invoking Random Cat Function")
        rand = random.randrange(4)
        if rand == 0:
            self.wake()
        elif rand == 1:
            self.call()
        elif rand == 2:
            self.feed()
        elif rand == 3:
            self.exercise()




