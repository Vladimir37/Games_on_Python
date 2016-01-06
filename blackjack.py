from random import randint

# variables
# gamers name
players_name = ['Bryant', 'Kalyna', 'Nadine', 'Alison', 'Rachel', 'Alysa', 'Natalie', 'Dion', 'Walt', 'Sage']
players = []
suits = ['heart', 'diamond', 'club', 'spade']
faces = [('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9),
         ('ten', 10), ('jack', 10), ('queen', 10), ('king', 10), ('ace', 11)]
all_cards = []

game = False

#classes
class Player(object):
    def __init__(self, name):
        self.name = name
    cards = []
    def decision(self):
        card_sum = 0
        for card in self.cards:
            card_sum += card.price

class Card(object):
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face[0]
        self.price = face[1]

# card generation
for suit in suits:
    for face in faces:
        all_cards.append(Card(suit, face))

while True:
    start = raw_input('If you need help - "help". If you ready to play enter "play": ')
    if start == 'help':
        print 'To display your cards enter "cards". To ask more card enter "more". Enter "stop" for stay with your cards.'
    elif start == 'play':
        game = True
        break
    else:
        print 'Incorrect command'
while game:
    players_num = raw_input('Enter gamers num (min - 2, max: 10): ')
    if type(players_num) != int or players_num > 10 or players_num < 2:
        print 'Incorrect value'
        continue
    for num in range(players_num - 1):
        players.append(Player(players_name[num]))