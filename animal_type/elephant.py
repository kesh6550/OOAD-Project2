#!/usr/bin/env python

from animal_parent.pachyderm import Pachyderm
from animal_type.makenoise import PaNoise


panoise = PaNoise()

class Elephant(Pachyderm):
    def __init__(self, name):
        super().__init__(name, panoise)

    def wake(self):
        print("Elephant " + self.name + " type " + self.type + " is waked up by the zookeeper")
        super().roam()

    def call(self):
        print("Elephant " + self.name + " type " + self.type + " is called by the zookeeper")

    def feed(self):
        print("Elephant " + self.name + " type " + self.type + " is fed by the zookeeper")

    def exercise(self):
        print("Elephant " + self.name + " type " + self.type + " is exercised by the zookeeper")

    def sleep(self):
        print(super(Pachyderm, self).sleep() + " Elephant " + "with name " + self.name + " type " + self.type)

