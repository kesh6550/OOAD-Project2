import abc
from animal_parent.feline import Feline
from animal_parent.pachyderm import Pachyderm
from animal_parent.canine import Canine


class NoiseBehaviour(abc.ABC):

    @abc.abstractmethod
    def make_noise(self):
        pass


class FeNoise(NoiseBehaviour):
    def make_noise(self):
        print("Feline is growling")


class PaNoise(NoiseBehaviour):
    def make_noise(self):
        print("Pachyderm is roaring")


class CanNoise(NoiseBehaviour):
    def make_noise(self):
        print("Canine is grunting")
