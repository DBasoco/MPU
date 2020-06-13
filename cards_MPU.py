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

    def enchant(self, target): # enchantments modify the attributes of what they enchant
        target.att += self.att



class Planeswalker(Card):

    def __init__(self, cost, local, tapped, color, att, loyalty): # they act as a creature and a player, very strange
        super().__init__(cost, local, tapped, color, att)
        self.loyalty = loyalty

    def change_loyalty(self, nc=0):
        self.loyalty += nc


class Land(Card): # automatic __init__ from parent and builds up a pool

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
        super().__init__(cost, local, tapped, color, att) # they have damage and defense stats
        self.power = power
        self.toughness = toughness


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