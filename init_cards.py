# this is where we instantiate all the needed cards

# enchantments
Choke = Enchantment(3, My.deck, False, 'G', """Islands don't untap during their controllers'untap steps""", My.field)

Cloak_of_Invisibility = Enchantment(1, My.deck, False, 'U', """Enchanted creature gains phasing and cannot be blocked 
except by Walls.""", input(Creature()))

Dread_of_Night = Enchantment(1, My.deck, False, 'B', """White creatures get -1/-1.""", My.field)

Illusory_Gains = Enchantment(5, My.deck, False, 'U', """You control enchanted creature. Whenever a creature enters 
the battlefield under an opponents control, attach Illusory Gains to that creature.""", input(Creature()))

Power_Artifact_0 = Enchantment(2, My.deck, False, 'U', """Enchanted artifact's activated abilities cost 2 less to 
activate.""", input(Artifact()))
Power_Artifact_1 = Enchantment(2, My.deck, False, 'U', """Enchanted artifact's activated abilities cost 2 less to 
activate.""", input(Artifact()))
Power_Artifact_2 = Enchantment(2, My.deck, False, 'U', """Enchanted artifact's activated abilities cost 2 less to 
activate.""", input(Artifact()))
Power_Artifact_3 = Enchantment(2, My.deck, False, 'U', """Enchanted artifact's activated abilities cost 2 less to 
activate.""", input(Artifact()))

Prismatic_Omen = Enchantment(2, My.deck, False, 'G', """Lands you control are every basic land type in addition to 
their other types.""", My.field)

Privileged_Position = Enchantment(5, My.deck, False, 'WG', """Other permanents you control have hexproof.""", My.field)

Recycle = Enchantment(6, My.deck, False, 'G', """Skip your draw phase. Whenever you play a card, draw a card. During 
your discard phase, choose and discard all but two cards.""", My.field)

Shared_Triumph = Enchantment(2, My.deck, False, 'W', """Creatures of chosen type get +1/+1.""", My.field)

Steely_Resolve = Enchantment(2, My.deck, False, 'G', """Creatures of chosen type can't be the targets of spells or 
abilities.""", My.field)

Wheel_of_Sun_and_Moon = Enchantment(2, My.deck, False, 'WG', """If a card would be put into enchanted player's 
graveyard from anywhere, instead that card is revealed and put on the bottom og that player's library.""", input(Player()))

Wild_Evocation = Enchantment(6, My.deck, False, 'R', """At the beginning of each player's upkeep, that player reveals 
a card at random from his or her hand. If it's a land card, the player puts it onto the battlefield. Otherwise, 
the player casts it without paying its mana cost if able.""", My.field)

# planeswalkers
Karn_Liberated = Planeswalker(7, My.deck, False, 'V', '', 6)

# lands
Ancient_Tomb_0 = Land(0, My.deck, False, 'V', """Tap: Add two colorless mana to your mana pool. Ancient Tomb deals 2 
damage to you.""")
Ancient_Tomb_1 = Land(0, My.deck, False, 'V', """Tap: Add two colorless mana to your mana pool. Ancient Tomb deals 2 
damage to you.""")
Ancient_Tomb_2 = Land(0, My.deck, False, 'V', """Tap: Add two colorless mana to your mana pool. Ancient Tomb deals 2 
damage to you.""")
Ancient_Tomb_3 = Land(0, My.deck, False, 'V', """Tap: Add two colorless mana to your mana pool. Ancient Tomb deals 2 
damage to you.""")

# creatures

