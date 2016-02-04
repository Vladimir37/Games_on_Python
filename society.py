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

def random_with_zero(num):
    if num > 0:
        one = 0
        two = num
    elif num < 0:
        one = num
        two = 0
    else:
        return 0
    return randint(one, two)

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

    # human make a choice and get bonus/penalty
    def choice(self):
        actual = {}
        actual['comfort'] = ((self.changing['comfort']['max'] - self.changing['comfort']['current']) *
                          (self.character['consumerism'] / 2) / ((self.character['melancholy'] / 2) + 1))
        actual['communication'] = ((self.changing['communication']['max'] - self.changing['communication']['current']) *
                                (self.character['sociality'] / 2) / ((self.character['melancholy'] / 2) + 1))
        complaints = []
        desires = []
        for elem in actual:
            if actual[elem] > 30:
                complaints.append(elem)
                print '%s suffers from a lack of %s' % (self.name, elem)
                self.changing['tranquility']['current'] -= randint(1, 8)
            elif 30 > actual[elem] > 15:
                desires.append(elem)
                print '%s wants to %s' % (self.name, elem)
                self.changing['tranquility']['current'] -= randint(0, 4)
            else:
                self.changing['tranquility']['current'] += randint(0, 3)
        return actual

    # select other human for dialog
    def select_human(self):
        if not len(self.changing['relation']):
            while True:
                new_human_num = randint(0, len(all_humans) - 1)
                if all_humans[new_human_num].name == self.name:
                    continue
                else:
                    break
            relation_result = 0
            selected = all_humans[new_human_num]
            social_max = max(self.character['sociality'], selected.character['sociality'])
            social_min = min(self.character['sociality'], selected.character['sociality'])
            social_difference = randint(0, social_max - social_min)
            consumer_max = max(self.character['consumerism'], selected.character['consumerism'])
            consumer_min = min(self.character['consumerism'], selected.character['consumerism'])
            consumer_difference = randint(0, consumer_max - consumer_min)

    # talk with other humans
    def talk(self):
        # human has no friends


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

for human in all_humans:
    human.choice()