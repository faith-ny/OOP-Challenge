# -*- coding: utf-8 -*-

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print("{} ate some food. 🍗".format(self.name))

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print("{} took a nap. 😴".format(self.name))

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print("{} had fun playing! 🐾".format(self.name))
        else:
            print("{} is too tired to play. 💤".format(self.name))

    def get_status(self):
        print("\n📝 {}'s Status:".format(self.name))
        print("Hunger: {}/10".format(self.hunger))
        print("Energy: {}/10".format(self.energy))
        print("Happiness: {}/10\n".format(self.happiness))

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        print("{} learned a new trick: {}! 🐶".format(self.name, trick))

    def show_tricks(self):
        if self.tricks:
            print("{} knows these tricks: {}".format(self.name, ", ".join(self.tricks)))
        else:
            print("{} hasn't learned any tricks yet.".format(self.name))
