# test class and object interactions
import random


class Player:  # so the player is the one with health, turn counter, and has all the locations

    def __init__(self, health=20):
        self.health = health
        self.deck = Location()
        self.hand = Location()
        self.field = Location()
        self.graveyard = Location()
        self.exile = Location()
        self.MANA = [[], [], [], [], [], []]
        self.turn = False

    def defend(self, wall, mark): # combat is so annoying,
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


class Card:

    def __init__(self, cost, local, tapped=False, color='', att=''):
        """

        :type local: object
        :type cost: enumerate
        :type tapped: bool
        :type color: str

        """
        self.cost = cost
        self.local = local
        local.items.append(self)
        self.tapped = tapped
        self.color = color
        self.att = att

    def move_card(self, target):
        target.items.append(self)
        self.local.items.remove(self)

    def tap(self):  # this needs some kind of stopper to prevent a card from being tapped multiple times
        if not self.tapped:
            self.tapped = True
        else:
            self.tapped = False


class Land(Card):

    def add_mana(self):
        COLORS = 'WUBRGV'
        self.tap()
        if self.tapped:
            for i in COLORS:
                if self.color == i:
                    My.MANA[COLORS.index(i)] += i  # will change to make turn based
                    if not self.color == 'V':
                        My.MANA[5] += 'V'


class Creature(Card):

    def __init__(self, cost, local, tapped, color, att, power, toughness):
        """

        :type power: enumerate
        :type toughness: enumerate
        :type att: str

        """
        super().__init__(cost, local, tapped, color, att)
        self.power = power
        self.toughness = toughness

    def attack(self, mark_a):  # attacking taps but doesn't have a set mark
        self.mark_a = mark_a
        self.tap()


My = Player()
Opp = Player()

Swamp = Land(0, My.deck, color='B')
Forest = Land(0, My.deck, color='G')
Plains = Land(0, My.deck, color='W')
Mountain = Land(0, My.deck, color='R')
Token = Creature(0, My.deck, False, 'V', '', 1, 1)


def shuffle(target):
    random.shuffle(target.items)


shuffle(My.deck)
My.deck.draw(3)

print('Your hand has: %s' % My.hand.items)
print('Your deck has: %s' % My.deck.items)

choice = int(input('Which card would you like to play? '))

My.hand.play(choice, My.field)

print('Your hand has: %s' % My.hand.items)
print('Your field has: %s' % My.field.items)

print(My.field.items[0].local, My.field.items[0].tapped)

print(My.MANA)
