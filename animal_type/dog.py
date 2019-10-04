#!/usr/bin/env python

from animal_parent.canine import Canine
from animal_type.makenoise import CanNoise

cannoise = CanNoise()


class Dog(Canine):
    def __init__(self, name):
        super().__init__(name, cannoise)

    def wake(self):
        print("Dog " + self.name + " type " + self.type + " waked up the zookeeper!!")
        super().roam()

    def call(self):
        print("Dog " + self.name + " type " + self.type + " called by the zookeeper!!")

    def feed(self):
        print("Dog " + self.name + " type " + self.type + " feed by the zookeeper!!")

    def exercise(self):
        print("Dog " + self.name + " type " + self.type + " exercise by the zookeeper!!")

    def sleep(self):
        print(super(Canine, self).sleep() + " Dog " + " with name " + self.name + " type " + self.type)
