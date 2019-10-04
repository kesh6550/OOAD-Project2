import abc

class Animal(abc.ABC):
    def sleep(self):
        return "Animal going to sleep"


    @abc.abstractmethod
    def wake(self):
        pass


#NoiseBehaviour()
    def perform_noise(self):
        FeNoise()





    @abc.abstractmethod
    def call(self):
        pass

    @abc.abstractmethod
    def feed(self):
        pass

    @abc.abstractmethod
    def exercise(self):
        pass

    @abc.abstractmethod
    def make_noise(self):
        pass


class Strategy(Animal):

    @abc.abstractmethod
    def roam(self):
        pass



