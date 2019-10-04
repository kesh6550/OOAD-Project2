#!/usr/bin/env python
import abc
from animal import Animal


class Feline(Animal):

    def __init__(self, name, noise_strategy):
        self.name = name
        self.noise_behaviour = noise_strategy

    def make_noise(self):
        self.noise_behaviour.make_noise()

    type = "Feline"

    def make_noise(self):
        self.noise_behaviour.make_noise()

    def roam(self):
        print("Feline is roaming")

    @abc.abstractmethod
    def wake(self):
        pass

    @abc.abstractmethod
    def call(self):
        pass

    @abc.abstractmethod
    def feed(self):
        pass

    @abc.abstractmethod
    def exercise(self):
        pass

