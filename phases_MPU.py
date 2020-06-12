# the module containing the needed game structure for play

# needed phases: begin, main, combat, again, end

import random


class Location:

    def __init__(self):
        self.items = []

    def draw(self, num=1):
        for i in range(num):
            if not len(self.items) == 0:
                q = self.items[len(self.items) - 1]
                My.hand.items.append(q)  # will adjust to make it turn based
                self.items.remove(q)

            else:
                print('GAME OVER')

    def play(self, num, target):
        if len(My.MANA[5]) >= self.items[num - 1].cost:  # will adjust to make turn based
            target.items.append(self.items[num - 1])
            self.items.remove(self.items[num - 1])


class Player:  # so the player is the one with health, mana, and has all the locations

    def __init__(self, health=20):
        self.health = health
        self.deck = Location()
        self.hand = Location()
        self.field = Location()
        self.graveyard = Location()
        self.exile = Location()
        self.MANA = [[], [], [], [], [], []]
        self.turn = False


My = Player()
Opp = Player()


def start(mull=0):  # starts the game off
    shuffle(My.deck)
    shuffle(Opp.deck)
    My.deck.draw(7-mull)
    if mull == 7:
        return print('You lose!')


def mulligan():
    mull += 1
    start(mull)


def shuffle(target): # shuffles target: can be deck, hand, graveyard
    random.shuffle(target.items)


def begin():
    for each in lands:
        each.tap()
        deck.draw()
