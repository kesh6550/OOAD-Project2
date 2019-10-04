#!/usr/bin/env python

from animal import Animal


class Zoo(object):
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def openZoo(self):
        print("Opening the zoo")
        
    def closeZoo(self):
        print("Closing the zoo")
