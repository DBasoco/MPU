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
        self.tape = Location()
        self.turn = False


class Location:

    def __init__(self):
        self.items = []

    def draw(self, num=1):
        # to make the game easier I should find a way to draw an instantiated hand so that way the
        # user isn't pressing shuffle till they get the exact right hand.
        for i in range(num):
            if not len(self.items) == 0:
                q = self.items[len(self.items) - 1]
                My.hand.items.append(q)  # will adjust to make it turn based
                self.items.remove(q)

            else:
                print('GAME OVER')

    def play(self, id, target):
        if type(target) == Land:
            My.lands += self  # so we need a player quality that has lands as a instantiation

        num = self.reveal().index(id)
        if len(My.MANA[5]) >= self.items[num].cost:
            target.items.append(self.items[num])
            self.items.remove(self.items[num])
        else:
            print("Not enough mana... \nDon't miss those land drops.\n")

    def reveal(self, num=0):
        x = []
        if num == 0:
            for i in range(0, len(self.items)):
                x += [self.items[i].name]
            return x
        else:
            pass

    def move(self, id, target):
        num = self.reveal().index(id)
        target.items.append(self.items[num])
        self.items.remove(self.items[num])


class Card:

    def __init__(self, name, cost, local, tapped=False, color='', att=''):
        """

        :typr name: str
        :type local: object
        :type cost: int
        :type tapped: bool
        :type color: str
        :type att: str

        """
        self.name = name
        self.cost = cost
        self.local = local
        local.items.append(self)
        self.tapped = tapped
        self.color = color
        self.att = att

    def move_card(self, target): # is this even needed?
        target.items.append(self)
        self.local.items.remove(self)

    def tap(self):
        if not self.tapped:
            self.tapped = True
            if type(self) == Land:
                self.add_mana()
        else:
            self.tapped = False

    def read(self):
        if type(self) == Land:
            print('%s is a land that reads:\n"%s"' % (self.name, self.att))

        if type(self) == Creature:
            print(
                '%s is a %s/%s for %s, that reads:\n"%s"' % (self.name, self.power, self.toughness, self.cost, self.att))


class Land(Card):
    def __int__(self):
        super().__init__()

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

        :type power: int
        :type toughness: int

        """
        super().__init__(name, cost, local, tapped, color, att)
        self.power = power
        self.toughness = toughness


My = Player()
Opp = Player()

Swamp = Land('Swamp', 0, My.deck, color='B', att='Tap: Add one black mana to mana pool.')
Forest = Land('Forest', 0, My.deck, color='G', att='Tap: Add one green mana to mana pool.')
Plains = Land('Plains', 0, My.deck, color='W', att='Tap: Add one white mana to mana pool.')
Mountain = Land('Mountain', 0, My.deck, color='R', att='Tap: Add one red mana to mana pool.')
Token = Creature('Token', 0, My.deck, False, 'V', 'Tap: win the game.', 1, 1)

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

Fungus_Sliver = Creature('Fungus Sliver', 4, My.deck, False, 'G', """All Silver creatures have 'Whenever this           
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
GG = False

while not GG:
    print('\nYour hand has: %s' % My.hand.reveal())

    action = int(input('What would you like to do?\n1. Read a card in your hand\n2. Play a card from your hand\n3. Tap a card on you filed\n--> '))

    if action == 1:
        
    elif action == 2:

    elif action == 3:

    else:
        pass

    choice = input('Which card would you like to play? ')

    My.hand.play(choice, My.field)

    print('\nYour hand has: %s' % My.hand.reveal(), '\n')


    try:
        print('Your field has: %s' % My.field.reveal(), '\n')

        print(My.field.reveal(), My.field.items[0].tapped)
        if type() == Land: #######here currently
            answer = input(print('Want to tap the land? [Y/n] '))
            if answer == 'Y' or 'y':
                answer.tap()
                print(My.field.items[0].tapped)
                print(My.MANA)

    except IndexError:
        pass

    try:
        My.field.items[0].read()
        print('\n')
    except IndexError:
        pass

    My.deck.draw(3)

    while len(My.hand.items) > 7:
        print('\nYour hand has: %s' % My.hand.reveal(), '\n')

        discard = input('You have too many cards, please discard a card.\n'
                        'Which card will you discard? ')

        My.hand.move(discard, My.graveyard)


# print('Your hand has: %s' % My.hand.reveal())
# print('Your deck has: %s' % My.deck.reveal())
#
# choice = input('Which card would you like to play? ')
#
# My.hand.play(choice, My.field)
#
# print('Your hand has: %s' % My.hand.reveal())
# print('Your field has: %s' % My.field.reveal())
#
# print(My.field.reveal(), My.field.items[0].tapped)
#
# My.field.items[0].read()
