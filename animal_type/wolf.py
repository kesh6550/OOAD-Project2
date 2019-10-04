#!/usr/bin/env python

from animal_parent.canine import Canine
from animal_type.makenoise import CanNoise


cannoise = CanNoise()

class Wolf(Canine):
    def __init__(self, name):
        super().__init__(name, cannoise)

    def wake(self):
        print("Wolf " + self.name + " type " + self.type + " is waked up by the zookeeper")
        super().roam()

    def call(self):
        print("Wolf " + self.name + " type " + self.type + " is called by the zookeeper")

    def feed(self):
        print("Wolf " + self.name + " type " + self.type + " is fed by the zookeeper")

    def exercise(self):
        print("Wolf " + self.name + " type " + self.type + " is exercised up by the zookeeper")

    def sleep(self):
        print(super(Canine, self).sleep() + "Wolf " + "with name " + self.name + " type " + self.type)
