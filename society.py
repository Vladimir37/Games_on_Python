from random import randint
import time

# variables
names = ["Fidela","Alessandra","Frederick","Marlene","Londa","Neoma","Coreen","Nathan","Angelena","Cathern","Leeann",
         "Lisbeth","Rolando","Lyndsey","Krystyna","Bong","Petra","August","Graig","Lessie"]

# rand int from 1 to 10
def scale():
    return randint(1, 10)

def graded_scale(min, max):
    value = randint(min, max)
    return {
        'current': value,
        'max': value
    }

def fixed_graded_scale(current, max):
    return {
        'current': current,
        'max': max
    }

# human class
class human(object):
    def __init__(self):
        self.personal = {
            'addiction': scale(),
            'melancholy': scale(),
            'sociality': scale(),
            'aggression': scale(),
            'envy': scale(),
            'consumerism': scale(),
            'obduracy': scale(),
            'greed': scale()
        }
        self.changing = {
            'tranquility': graded_scale(30, 60),
            'contentment': fixed_graded_scale(randint(10, 15), 20),
            'comfort': fixed_graded_scale(randint(1, 10), 10),
            'offence': 0,
            'relation': {}
        }