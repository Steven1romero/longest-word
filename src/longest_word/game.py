# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods

import random
import string


class Game:
    def __init__(self, size: int = 9) -> None:
        """Attribute a random grid of size 9"""
        self.grid = random.sample(string.ascii_uppercase, size)

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        letters = self.grid.copy()

        for char in word.upper():
            if char not in letters:
                return False
            letters.remove(char)

        return True
