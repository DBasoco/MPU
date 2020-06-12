# this is the module containing all the class information for the cards

class Card:

    def __init__(self, cost, local, tapped=False, color='', att=''):  # creates the parent class for cards, with each having a mana cost to play, whether it enters tapped or not, and color
        """

        :type local: list
        :type cost: enumerate
        :type tapped: bool
        :type color: str

        """
        self.cost = cost # cost to play card
        self.local = local # the location of the card
        local += self.card # puts card in that location
        self.tapped = tapped # is the carded tapped
        self.color = color # what color is the card
        self.att = att # what special ability the card has

    # color options: green, blue, black, white, red, void

    def move_card(self, target):
        target.items.append(self)
        self.local.items.remove(self)

    def tap(self):  # defines a function to change the tapped state of a card
        if not self.tapped:
            tapped = True
        else:
            tapped = False
        return tapped


class Enchantment(Card):

    def __init__(self, cost, local, tapped, color, att, target):
        super().__init__(cost, local, tapped, color, att)
        self.target = target

    def enchant(self, target):
        target.att += self.att



class Planeswalker(Card):

    def __init__(self, cost, local, tapped, color, att, loyalty):
        super().__init__(cost, local, tapped, color, att)
        self.loyalty = loyalty

    def cl(self, nc=0):
        self.loyalty += nc


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

    def defend(self, mark):  # there is so much to unpack in combat, mad respect for those that coded the real game
        if not 'Fly' in mark.att:
            self.toughness = self.toughness - mark.power
            mark.toughness = mark.toughness - self.power

            if self.toughness <= 0:
                self.local = graveyard
                self.local += self.creature
            if mark.toughness <= 0:
                self.local = graveyard
                self.local += self.creature
            if mark.trait == 'Deathtouch':  # do I even need to worry about these traits?
                self.local = graveyard
                self.local += self.creature

        else:
            Player.health = Player.health - mark.toughness


class Sorcery(Card):

    def __init__(self, cost, local, tapped, color, att, target):
        super().__init__(cost, local, tapped, color, att)
        self.target = target
        if not phase == 'main' or 'again':
            # card can't be played


class Instant(Card):

    def __init__(self, cost, local, tapped, color, att, target):
        super().__init__(cost, local, tapped, color, att)
        self.target = target


class Artifact(Card):

    def __init__(self, cost, local, tapped, color, att):
        super().__init__(cost, local, tapped, color, att)