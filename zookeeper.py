#!/usr/bin/env python


class Zookeeper(object):

    def wake_animal(self, zoo):
        print("Wake the animals")
        for i in zoo.animals:
            i.wake()

    def call_animal(self,zoo):
        print("Roll call the animal")
        for i in zoo.animals:
            i.call()

    def noise_heard(self,zoo):
        print("Animals are making noise")
        for i in zoo.animals:
            i.make_noise()

    def feed_animal(self,zoo):
        print("Feed the animal")
        for i in zoo.animals:
            i.feed()

    def exercise_animal(self,zoo):
        print("Exercise the animal")
        for i in zoo.animals:
            i.exercise()

    def sleep_animal(self,zoo):
        print("The animal sleeps")
        for i in zoo.animals:
            i.sleep()
