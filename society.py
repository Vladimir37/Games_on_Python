from random import randint
import time

# variables
names = ["Fidela","Alessandra","Frederick","Marlene","Londa","Neoma","Coreen","Nathan","Angelena","Cathern","Leeann",
         "Lisbeth","Rolando","Lyndsey","Krystyna","Bong","Petra","August","Graig","Lessie"]

# rand funcs
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

# name generation
def select_name():
    number = randint(0, len(names) - 1)
    selected_name = names[number]
    del names[number]
    return selected_name

# human class
class Human(object):
    def __init__(self, name):
        self.name = name
        self.personal = {
            'addiction': scale(),
            'aggression': scale(),
            'envy': scale(),
            'obduracy': scale(),
            'greed': scale()
        }
        self.character = {
            'sociality': scale(),
            'consumerism': scale(),
            'melancholy': scale(),
        }
        self.changing = {
            'tranquility': graded_scale(30, 60),
            'contentment': fixed_graded_scale(randint(10, 15), 20),
            'comfort': fixed_graded_scale(randint(1, 10), 20),
            'communication': fixed_graded_scale(randint(1, 10), 20),
            'capital': randint(10, 100),
            'offence': 0,
            'relation': {}
        }
    def choise(self):
        actual = []


# number question
while True:
    human_num = raw_input('Enter humans num from 2 to 10: ')
    try:
        human_num = int(human_num)
    except:
        print 'Incorrect value!'
        continue
    if 1 < human_num < 11:
        print 'OK, %s humans' % (human_num)
        break
    else:
        print 'Incorrect value!'
        continue

# humans generation
all_humans = []
for num in range(human_num):
    all_humans.append(Human(select_name()))

print all_humans[0].personal
print all_humans[0].character
print all_humans[0].changing