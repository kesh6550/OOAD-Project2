#!/usr/bin/env python
from animal_type.makenoise import FeNoise
from animal_parent.feline import Feline

fenoise = FeNoise()

class Lion(Feline):

    def __init__(self, name):
        super().__init__(name, fenoise)

    def wake(self):
        print("Lion " + self.name + " type " + self.type + " is waked up by the zookeeper!!")
        super().roam()

    def call(self):
        print("Lion " + self.name + " type " + self.type + " is called by the zookeeper!!")

    def feed(self):
        print("Lion " + self.name + " type " + self.type + " is fed by the zookeeper!!")

    def exercise(self):
        print("Lion " + self.name + " type " + self.type + " is exercised by the zookeeper!!")

    def sleep(self):
        print(super(Feline, self).sleep() + " Lion" + " with name " + self.name + " type " + self.type)
