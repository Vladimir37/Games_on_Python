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

# classes
class Player(object):
    def __init__(self, name):
        self.name = name
        self.cards = []
    def card_sum(self):
        card_sum = 0
        for card in self.cards:
            card_sum += card.price
        return card_sum
    def adding_card(self, card):
        self.cards.append(card)
    def decision(self):
        card_sum = self.card_sum()
        if card_sum <= 14:
            return True
        elif card_sum >= 20:
            return False
        else:
            return bool(randint(0, 1))

class Card(object):
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face[0]
        self.price = face[1]

# card generation
for suit in suits:
    for face in faces:
        all_cards.append(Card(suit, face))

# card transfer
def card_transfer(player, num):
    for n in range(num):
        card_num = randint(0, len(all_cards) - 1)
        player.adding_card(all_cards[card_num])
        del all_cards[card_num]

# card view
def card_view(player):
    for card in player.cards:
        print card.suit, card.face, '-', card.price
    print 'Sum: ', player.card_sum()

# main menu
while True:
    start = raw_input('If you need help - "help". If you ready to play enter "play": ')
    if start == 'help':
        print 'To ask more card enter "more". Enter "stop" for stay with your cards.'
    elif start == 'play':
        game = True
        break
    else:
        print 'Incorrect command'

# playing
while game:
    players_num = int(raw_input('Enter gamers num (min - 2, max: 10): '))
    if type(players_num) != int or players_num > 10 or players_num < 2:
        print 'Incorrect value'
        continue
    players.append(Player('You'))
    for num in range(players_num - 1):
        players.append(Player(players_name[num]))
    # card distribution
    for player in players:
        card_transfer(player, 2)
    card_view(players[0])
    # main player actions
    while True:
        if players[0].card_sum() == 21:
            print 'You have 21'
            break
        elif players[0].card_sum() > 21:
            print 'You have too much'
            break
        next_action = raw_input('You action? (more/stop) ')
        if next_action == 'more':
            card_transfer(players[0], 1)
            card_view(players[0])
            continue
        elif next_action == 'stop':
            break
        else:
            print 'Incorrect command'
            continue
    # other player actions
    for player_num in range(1, len(players)):
        while True:
            if players[player_num].decision():
                card_transfer(players[player_num], 1)
                continue
            break
    # winners
    while True:
        winners = []
        final = raw_input('All ready. Open cards? (Yes) ')
        if final != 'Yes':
            print 'Incorrect command'
            continue
        else:
            break
    for player in players:
        print player.name, '-'
        card_view(player)
        if player.card_sum() <= 21:
            winners.append([player.name, player.card_sum()])
    players = []
    winners.sort(key=lambda a: a[1])
    if len(winners) > 0:
        print winners[-1][0], 'win!'
        if winners[-1][0] != 'You':
            print 'You lose'
    else:
        print 'All loses'
    final_choice = raw_input('Play again? (Yes/No)')
    if final_choice == 'Yes':
        continue
    else:
        print 'Bue'
        game = False