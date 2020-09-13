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

    def defend(self, wall, mark): # combat is so annoying, this has to be the last thing to get done
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

    def play(self, id, target):
        num = self.reveal().index(id)
        if len(My.MANA[5]) >= self.items[num].cost:
            target.items.append(self.items[num])
            self.items.remove(self.items[num])

        if type(target) == Land:
            My.lands += self  # so we need a player quality that has lands as a instantiation

    def reveal(self, num=0):
        x = []
        if num == 0:
            for i in range(0, len(self.items)):
                x += [self.items[i].name]
            return x
        else:
            pass


class Card:

    def __init__(self, name, cost, local, tapped=False, color='', att=''):
        """

        :type local: object
        :type cost: enumerate
        :type tapped: bool
        :type color: str

        """
        self.name = name
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

    def __init__(self, name, cost, local, tapped, color, att, power, toughness):
        """

        :type power: enumerate
        :type toughness: enumerate
        :type att: str

        """
        super().__init__(name, cost, local, tapped, color, att)
        self.power = power
        self.toughness = toughness

    def attack(self, mark_a):  # attacking taps but doesn't have a set mark
        self.mark_a = mark_a
        self.tap()


My = Player()
Opp = Player()

Swamp = Land('Swamp', 0, My.deck, color='B')
Forest = Land('Forest', 0, My.deck, color='G')
Plains = Land('Plains', 0, My.deck, color='W')
Mountain = Land('Mountain', 0, My.deck, color='R')
Token = Creature('Token', 0, My.deck, False, 'V', '', 1, 1)


# actual cards from the deck
Ancient_Tomb_0 = Land('Ancient Tomb', 0, My.deck, False, 'V', """Tap: Add two colorless mana to your mana pool. 
Ancient Tomb deals 2 damage to you.""")
Ancient_Tomb_1 = Land('Ancient Tomb', 0, My.deck, False, 'V', """Tap: Add two colorless mana to your mana pool. 
Ancient Tomb deals 2 damage to you.""")
Ancient_Tomb_2 = Land('Ancient Tomb', 0, My.deck, False, 'V', """Tap: Add two colorless mana to your mana pool. 
Ancient Tomb deals 2 damage to you.""")
Ancient_Tomb_3 = Land('Ancient Tomb', 0, My.deck, False, 'V', """Tap: Add two colorless mana to your mana pool. 
Ancient Tomb deals 2 damage to you.""")

Blazing_Archon = Creature('Blazing Archon', 9, My.deck, False, 'W', """Flying. Creatures can't attack you.""", 5, 6)

Djinn_Illuminatus = Creature('Djinn Illumination', 7, My.deck, False, 'UR', """Flying. Each instant and sorcery spell   
you cast has replicate. The replicate cost is equal to its mana cost.""", 3, 5)

Fathom_Feeder = Creature('Fathom Feeder', 2, My.deck, False, 'V', """Deathtouch. Ingest. VVVUB: Draw """, 1, 1)

Fungus_Silver = Creature('Fungus Silver', 4, My.deck, False, 'G', """All Silver creatures have 'Whenever this           
creature is dealt damage, put a +1/+1 counter on is.'""", 2, 2)

Memnarch = Creature('Memnarch', 7, My.deck, False, 'V', """(VBB): Target permanent becomes an artifact in addition to   
its other types. (VVVB): Gain control of target artifact.""", 4, 5)

Olivia_Voldaren = Creature('Olivia Voldaren', 4, My.deck, False, 'BR', 'Flying. (VR): Olivia Voldaren deals 1 damage '
                                                                       'to another target creature. That creature '
                                                                       'becomes a Vampire in addition to its other '
                                                                       'types. Put a +1/+1 counter on Olivia '
                                                                       'Voldaren. (VVVBB): Gain control of target '
                                                                       'Vampire for as as you control Olivia '
                                                                       'Voldaren.', 3, 3)

Rotlung_Reanimator = Creature('Rotlung Reanimator', 3, My.deck, False, 'B', 'Whenever Rotlung Reanimator or another '
                                                                            'Cleric is put into a graveyard from '
                                                                            'play, put a 2/2 black Zombie creature '
                                                                            'token into play.', 2, 2)

Soul_Snuffers = Creature('Soul Snuffers', 4, My.deck, False, 'B', 'When Soul Snuffers comes into play, put a -1/-1 '
                                                                  'counter on each creature.', 3, 3)

Vigor = Creature('Vigor', 6, My.deck, False, 'G', 'Trample. If damage would be dealt to another creature you control, '
                                                  'prevent that damage. Put a +1/+1 counter on that creature for each '
                                                  '1 damage prevented this way. When Vigor is put into a graveyard '
                                                  'from anywhere, shuffle it into its owners library.', 6, 6)

Xathrid_Necromancer = Creature('Xathrid Necromancer', 3, My.deck, False, 'B', 'Whenever Xathrid Necromancer or '
                                                                              'another Human creature you control '
                                                                              'dies, create a tapped 2/2 black Zombie '
                                                                              'creature token.', 2, 2)


def shuffle(target):
    random.shuffle(target.items)


shuffle(My.deck)
My.deck.draw(7)

print('Your hand has: %s' % My.hand.reveal())
print('Your deck has: %s' % My.deck.reveal())

choice = input('Which card would you like to play? ')

My.hand.play(choice, My.field)

print('Your hand has: %s' % My.hand.reveal())
print('Your field has: %s' % My.field.reveal())

print(My.field.reveal(), My.field.items[0].tapped)

print(My.MANA)





