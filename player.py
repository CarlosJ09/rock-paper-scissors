import random

class Player:
    def __init__(self, name, is_cpu=False):
        self.name = name
        self.is_cpu = is_cpu

    def make_choice(self):
        if self.is_cpu:
            return random.choice(["rock", "paper", "scissor"])
        else:
            return input(f"{self.name}, type rock, scissor, or paper: ").lower()

