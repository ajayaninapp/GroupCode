'''
Problem Statement

Create a Class Pet. Each instance of the class will be one electronic pet for the user to take care of. Each instance will have a current state, consisting of three Instance variables:

Hunger - integer

Boredom -  an integer

Sounds - a list of strings, each a word that the pet has been taught to say

Methods

In the __init__ method of the class, hunger and boredom are initialized to random values between 0 and the threshold for being hungry or bored. Initialize the sounds instance variable appropriately so that teaching a sound to any of the pets would not teach it to all instances of the class!

There is a clock_tick method which just increments the boredom and hunger instance variables, simulating the idea that as time passes, the pet gets more bored and hungry.

The __str__ method produces a string representation of the pet’s current state, notably whether it is bored or hungry or whether it is happy. It’s bored if the boredom instance variable is larger than the threshold, which is set as a class variable.

To relieve boredom, the pet owner can either teach the pet a new word, using the teach() method, or interact with the pet, using the hi() method. In response to teach(), the pet adds the new word to its list of words. In response to the hi() method, it prints out one of the words it knows, randomly picking one from its list of known words. Both hi() and teach() cause an invocation of the reduce_boredom() method. It decrements the boredom state by an amount that it reads from the class variable boredom_decrement. The boredom state can never go below 0.

To relieve hunger, we call the feed() method which will cause an invocation of the reduce_hunger() method.

Features

Interact with the user. At each iteration, display a text prompt reminding the user of what commands are available.

The user will have a list of pets, each with a name. The user can issue a command to adopt a new pet, which will create a new instance of Pet. Or the user can interact with an existing pet, with a Greet, Teach, or Feed command.

Teach new words to pets so that each pet knows a different set of words.

No matter what the user does, with each command entered, the clock ticks for all their pets.

basic requirements
>classes -> Pet
>states -> happy , hungry , bored
>methods -> teach() , hi() --> reducing boredom and feed() --> reducing hunger
'''

import random
import numpy as np


class Pet:
    # global setup
    boredom_threshold = 5
    boredom_decrement = 4
    hunger_threshold = 10
    hunger_decrement = 6
    sounds = ['\t teach me!!']

    def __init__(self, name='simba'):  # kitty for default purpose
        self.name = name
        self.hunger = random.randrange(self.hunger_threshold)
        self.boredom = random.randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def states(self):
        if self.boredom <= self.boredom_threshold and self.hunger <= self.hunger_threshold:
            return 'HAPPY!!'

        elif self.boredom > self.hunger_threshold:
            return 'BORED!!'

        else:
            return 'HUNGRY!!'

    def __str__(self):
        return f"I am {self.name} and I feel {self.states()}!"

    def hi(self):
        print(self.sounds[random.randrange(0, len(self.sounds))])
        self.reduce_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()
        print('Ok got it!')

    def feed(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)


class Dog(Pet):
    boredom_threshold = 8
    boredom_decrement = 4
    hunger_threshold = 10
    hunger_decrement = 5

    sounds = ['woof!']

    def states(self):
        if self.boredom <= self.boredom_threshold and self.hunger <= self.hunger_threshold:
            return 'HAPPY!!'

        elif self.boredom > self.hunger_threshold:
            return 'BORED!!'

        else:
            return 'HUNGRY!!'

    def feed(self):
        Pet.feed(self)
        print("woof! yummy!")

    def hi(self):
        Pet.hi(self)

    def teach(self, word):
        Pet.teach(self, word)



class Cat(Pet):
    boredom_threshold = 4
    boredom_decrement = 2
    hunger_threshold = 8
    hunger_decrement = 5
    sounds = ['meow!']

    def states(self):
        if self.boredom <= self.boredom_threshold and self.hunger <= self.hunger_threshold:
            return 'HAPPY!!'

        elif self.boredom > self.hunger_threshold:
            return 'BORED!!'

        else:
            return 'HUNGRY!!'

    def feed(self):
        Pet.feed(self)
        print("meow! yummy!")

    def hi(self):
        Pet.hi(self)

    def teach(self, word):
        Pet.teach(self, word)

class Bird(Pet):
    boredom_threshold = 4
    boredom_decrement = 2
    hunger_threshold = 8
    hunger_decrement = 5
    sounds = ['chirp!']

    def states(self):
        if self.boredom <= self.boredom_threshold and self.hunger <= self.hunger_threshold:
            return 'HAPPY!!'

        elif self.boredom > self.hunger_threshold:
            return 'BORED!!'

        else:
            return 'HUNGRY!!'

    def feed(self):
        Pet.feed(self)
        print("Tweet tweet! yummy!")

    def hi(self):
        Pet.hi(self)

    def teach(self, word):
        Pet.teach(self, word)

def whichone(petlist, name):
    for pet in petlist:
        if pet.name == name:
            return pet
    return None # no pet matched

pet_types = {'dog': Dog, 'cat': Cat, 'bird': Bird}

def category(pet_type):
    return pet_types.get(pet_type, Pet)



