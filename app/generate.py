import random
import string
import json

img_dict = {letter: letter + ".png"
            for letter in string.ascii_uppercase}

class Dice:
    def __init__(self,
                 letters: str
                 ):
        self._letters = letters
    def roll(self):
        return random.choice(list(self._letters))

def generate_tiles():
    letters = []
    letters = [Dice("AAEEGN").roll(),
               Dice("ABBJOO").roll(),
               Dice("ACHOPS").roll(),
               Dice("AFFKPS").roll(),
               Dice("AOOTTW").roll(),
               Dice("CIMOTU").roll(),
               Dice("DEILRX").roll(),
               Dice("DELRVY").roll(),
               Dice("DISTTY").roll(),
               Dice("EEGHNW").roll(),
               Dice("EEINSU").roll(),
               Dice("EHRTVW").roll(),
               Dice("EIOSST").roll(),
               Dice("ELRTTY").roll(),
               Dice("HIMNQU").roll(),
               Dice("HLNNRZ").roll()]

    letters = [img_dict[letter] for letter in letters]
    return {"a1": letters.pop(random.randint(0, len(letters) - 1)),
            "a2": letters.pop(random.randint(0, len(letters) - 1)),
            "a3": letters.pop(random.randint(0, len(letters) - 1)),
            "a4": letters.pop(random.randint(0, len(letters) - 1)),
            "b1": letters.pop(random.randint(0, len(letters) - 1)),
            "b2": letters.pop(random.randint(0, len(letters) - 1)),
            "b3": letters.pop(random.randint(0, len(letters) - 1)),
            "b4": letters.pop(random.randint(0, len(letters) - 1)),
            "c1": letters.pop(random.randint(0, len(letters) - 1)),
            "c2": letters.pop(random.randint(0, len(letters) - 1)),
            "c3": letters.pop(random.randint(0, len(letters) - 1)),
            "c4": letters.pop(random.randint(0, len(letters) - 1)),
            "d1": letters.pop(random.randint(0, len(letters) - 1)),
            "d2": letters.pop(random.randint(0, len(letters) - 1)),
            "d3": letters.pop(random.randint(0, len(letters) - 1)),
            "d4": letters.pop(random.randint(0, len(letters) - 1))}
