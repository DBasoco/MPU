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

    def play(self, id, target):
        num = self.reveal().index(id)
        if len(My.MANA[5]) >= self.items[num].cost:
            target.items.append(self.items[num])
            self.items.remove(self.items[num])

        if type(target) == Land:
            My.lands += self

    def reveal(self, num=0):
        x = []
        if num == 0:
            for i in range(0, len(self.items)):
                x += [self.items[i].name]
            return x
        else:
            pass


class Player:  # so the player is the one with health, mana, and has all the locations

    def __init__(self, health=20):
        self.health = health
        self.deck = Location()
        self.hand = Location()
        self.field = Location()
        self.graveyard = Location()
        self.exile = Location()
        self.MANA = [[], [], [], [], [], []]
        self.lands = []
        self.turn = False
        self.mull = 0

    def defend(self, wall, mark):  # combat is so annoying, and needs to be turn based, AND ACCOUNT FOR OTHER SPELLS!!!
        if not 'Fly' in mark.att:
            if not 'First Strike' in mark.att:
                wall.toughness = wall.toughness - mark.power
                mark.toughness = mark.toughness - wall.power

                if wall.toughness <= 0:
                    wall.move_card(My.graveyard)
                if mark.toughness <= 0:
                    mark.move_card(Opp.graveyard)
                if mark.trait == 'Deathtouch':
                    wall.move_card(My.graveyard)
            else:
                wall.toughness = wall.toughness - mark.power
                if wall.toughness <= 0:
                    wall.move_card(My.graveyard)
                else:
                    mark.toughness = mark.toughness - wall.power
                    if mark.toughness <= 0:
                        mark.move_card(Opp.graveyard)
        else:
            self.health = self.health - mark.toughness

    def next_turn(self):
        if not self.turn:
            self.turn = True
        else:
            self.turn = False

    def mulligan(self):
        self.mull += 1
        for i in My.hand.items:
            My.hand.items.remove(i)
            My.deck.items.append(i)
        shuffle(My.deck)
        My.deck.draw(7 - My.mull)
        if My.mull == 7:
            return print('You lose!')


My = Player()
Opp = Player()


def start():  # starts the game off
    shuffle(My.deck)
    shuffle(Opp.deck)
    My.deck.draw(7)
    Opp.deck.draw(7)
    My.next_turn()


def shuffle(target):  # shuffles target: can be deck, hand, graveyard, etc
    random.shuffle(target.items)


def begin():
    phase = ''
    phase = ''.join('Begin')
    for each in lands:
        each.tap()
    My.deck.draw()


def main():
    phase = 'Main'


def combat():
    phase = 'Combat'
