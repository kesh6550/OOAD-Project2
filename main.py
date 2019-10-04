#!/usr/bin/env python

from animal_type.cat import Cat
from animal_type.dog import Dog
from animal_type.elephant import Elephant
from animal_type.hippo import Hippo
from animal_type.lion import Lion
from animal_type.rhino import Rhino
from animal_type.tiger import Tiger
from animal_type.wolf import Wolf

from zoo import Zoo
from zookeeper import Zookeeper


def main():
    zoo = Zoo()
    zookeeper = Zookeeper()

    zoo.openZoo()
    print("Zoo is getting populated")

    cat = Cat("Charlie")

    zoo.add_animal(cat)
    zoo.add_animal(Cat("Chloe"))

    zoo.add_animal(Dog("Darwin"))
    zoo.add_animal(Dog("Dale"))

    zoo.add_animal(Lion("Lionel"))
    zoo.add_animal(Lion("Liam"))

    zoo.add_animal(Elephant("Ellen"))
    zoo.add_animal(Elephant("Eric"))

    zoo.add_animal(Rhino("Rihaana"))
    zoo.add_animal(Rhino("Rikin"))

    zoo.add_animal(Wolf("Wolfson"))
    zoo.add_animal(Wolf("Wandera"))

    zoo.add_animal(Tiger("Taara"))
    zoo.add_animal(Tiger("Tarzan"))

    zoo.add_animal(Hippo("Harsh"))
    zoo.add_animal(Hippo("Hossam"))

    zookeeper.wake_animal(zoo)
    zookeeper.call_animal(zoo)
    zookeeper.noise_heard(zoo)
    zookeeper.feed_animal(zoo)
    zookeeper.exercise_animal(zoo)
    zookeeper.sleep_animal(zoo)

    cat.random()
    zoo.closeZoo()


main()





