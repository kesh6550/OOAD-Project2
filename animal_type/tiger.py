#!/usr/bin/env python

from animal_parent.feline import Feline
from animal_type.makenoise import FeNoise

fenoise = FeNoise()

class Tiger(Feline):

    def __init__(self, name):
        super().__init__(name, fenoise)

    def wake(self):
        print("Tiger " + self.name + " type " + self.type + " is waked up by the zookeeper!!")
        super().roam()

    def call(self):
        print("Tiger " + self.name + " type " + self.type + " is called by the zookeeper!!")

    def feed(self):
        print("Tiger " + self.name + " type " + self.type + " is fed by the zookeeper!!")

    def exercise(self):
        print("Tiger " + self.name + " type " + self.type + " is exercised by the zookeeper!!")

    def sleep(self):
        print(super(Feline, self).sleep() + " Tiger" + " with name " + self.name + " type " + self.type)
