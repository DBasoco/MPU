# this is where we instantiate all the needed cards

# enchantments
Choke = Enchantment('Choke', 3, My.deck, False, 'G', """Islands don't untap during their comptroller's untap steps""",
                    My.field)

Cloak_of_Invisibility = Enchantment('Cloak of Invisibility', 1, My.deck, False, 'U', """Enchanted creature gains 
phasing and cannot be blocked except by Walls.""", input(Creature()))

Dread_of_Night = Enchantment('Dread of Night', 1, My.deck, False, 'B', """White creatures get -1/-1.""", My.field)

Illusory_Gains = Enchantment('Illusory Gains', 5, My.deck, False, 'U', """You control enchanted creature. Whenever a 
creature enters the battlefield under an opponents control, attach Illusory Gains to that creature.""",
                             input(Creature()))

Power_Artifact_0 = Enchantment('Power Artifact', 2, My.deck, False, 'U', """Enchanted artifact's activated abilities cost 2 less to 
activate.""", input(Artifact()))
Power_Artifact_1 = Enchantment('Power Artifact', 2, My.deck, False, 'U', """Enchanted artifact's activated abilities cost 2 less to 
activate.""", input(Artifact()))
Power_Artifact_2 = Enchantment('Power Artifact', 2, My.deck, False, 'U', """Enchanted artifact's activated abilities cost 2 less to 
activate.""", input(Artifact()))
Power_Artifact_3 = Enchantment('Power Artifact', 2, My.deck, False, 'U', """Enchanted artifact's activated abilities cost 2 less to 
activate.""", input(Artifact()))

Prismatic_Omen = Enchantment('Prismatic Omen', 2, My.deck, False, 'G', """Lands you control are every basic land type in addition to 
their other types.""", My.field)

Privileged_Position = Enchantment('Privileged Position', 5, My.deck, False, 'WG', """Other permanents you control 
have hexproof.""", My.field)

Recycle = Enchantment('Recycle', 6, My.deck, False, 'G', """Skip your draw phase. Whenever you play a card, draw a card. During 
your discard phase, choose and discard all but two cards.""", My.field)

Shared_Triumph = Enchantment('Shared Triumph', 2, My.deck, False, 'W', """Creatures of chosen type get +1/+1.""",
                             My.field)

Steely_Resolve = Enchantment('Steely Resolve', 2, My.deck, False, 'G', """Creatures of chosen type can't be the targets of spells or 
abilities.""", My.field)

Wheel_of_Sun_and_Moon = Enchantment('Wheel of Sun and Moon', 2, My.deck, False, 'WG', """If a card would be put into 
enchanted player's graveyard from anywhere, instead that card is revealed and put on the bottom og that player's 
library.""", input(Player()))

Wild_Evocation = Enchantment('Wild Evocation', 6, My.deck, False, 'R', """At the beginning of each player's upkeep, that player reveals 
a card at random from his or her hand. If it's a land card, the player puts it onto the battlefield. Otherwise, 
the player casts it without paying its mana cost if able.""", My.field)

# planeswalkers
Karn_Liberated = Planeswalker('Karn Liberated', 7, My.deck, False, 'V', '', 6)

# lands
Ancient_Tomb_0 = Land('Ancient Tomb', 0, My.deck, False, 'V', """Tap: Add two colorless mana to your mana pool. Ancient Tomb deals 2 
damage to you.""")
Ancient_Tomb_1 = Land('Ancient Tomb', 0, My.deck, False, 'V', """Tap: Add two colorless mana to your mana pool. Ancient Tomb deals 2 
damage to you.""")
Ancient_Tomb_2 = Land('Ancient Tomb', 0, My.deck, False, 'V', """Tap: Add two colorless mana to your mana pool. Ancient Tomb deals 2 
damage to you.""")
Ancient_Tomb_3 = Land('Ancient Tomb', 0, My.deck, False, 'V', """Tap: Add two colorless mana to your mana pool. Ancient Tomb deals 2 
damage to you.""")

# creatures
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

# sorcery
Coalition_Victory = Sorcery('Coalition Victory', 10, My.deck, False, 'WUBRG', 'You win the game if control a land of '
                                                                              'each basic land type and a creature '
                                                                              'of each color.')

Donate = Sorcery('Donate', 3, My.deck, False, 'U', 'Target player gains control of target permanent you control.')

Infest = Sorcery('Infest', 3, My.deck, False, 'B', 'All creatures get -2/-2 until end of turn.')

Stolen_Identity = Sorcery('Stolen Identity', 6, My.deck, False, 'U', "Create a token that's a copy of target artifact "
                                                                     "or creature. Cipher (Then you may exile this "
                                                                     "spell card encoded on a creature you control. "
                                                                     "Whenever that creature deals combat damage to a "
                                                                     "player, its controller may cast a copy of the "
                                                                     "encoded card without paying its mana cost.)")

# artifact
Claws_of_Gix = Artifact('Claws of Gix', 0, My.deck, False, 'V', '(V), Sacrifice a permanent: You gain 1 life.')

Gemstone_Array_0 = Artifact('Gemstone Array', 4, My.deck, False, 'V', '(VV): Put a charge counter on Gemstone '
                                                                      'Array. Remove a charge counter from '
                                                                      'Gemstone Array: Add one mana of any color '
                                                                      'to your mana pool.')
Gemstone_Array_1 = Artifact('Gemstone Array', 4, My.deck, False, 'V', '(VV): Put a charge counter on Gemstone '
                                                                      'Array. Remove a charge counter from '
                                                                      'Gemstone Array: Add one mana of any color '
                                                                      'to your mana pool.')
Gemstone_Array_2 = Artifact('Gemstone Array', 4, My.deck, False, 'V', '(VV): Put a charge counter on Gemstone '
                                                                      'Array. Remove a charge counter from '
                                                                      'Gemstone Array: Add one mana of any color '
                                                                      'to your mana pool.')
Gemstone_Array_3 = Artifact('Gemstone Array', 4, My.deck, False, 'V', '(VV): Put a charge counter on Gemstone '
                                                                      'Array. Remove a charge counter from '
                                                                      'Gemstone Array: Add one mana of any color '
                                                                      'to your mana pool.')

Grim_Monolith_0 = Artifact('Grim Monolith', 2, My.deck, False, 'V', 'Grim Monolith does not untap during your '
                                                                    'untap phase. (tap): Add three colorless mana '
                                                                    'to your mana pool. Play this ability as a '
                                                                    'mana source. (VVVV): Untap Grim Monolith.')
Grim_Monolith_1 = Artifact('Grim Monolith', 2, My.deck, False, 'V', 'Grim Monolith does not untap during your '
                                                                    'untap phase. (tap): Add three colorless mana '
                                                                    'to your mana pool. Play this ability as a '
                                                                    'mana source. (VVVV): Untap Grim Monolith.')
Grim_Monolith_2 = Artifact('Grim Monolith', 2, My.deck, False, 'V', 'Grim Monolith does not untap during your '
                                                                    'untap phase. (tap): Add three colorless mana '
                                                                    'to your mana pool. Play this ability as a '
                                                                    'mana source. (VVVV): Untap Grim Monolith.')
Grim_Monolith_3 = Artifact('Grim Monolith', 2, My.deck, False, 'V', 'Grim Monolith does not untap during your '
                                                                    'untap phase. (tap): Add three colorless mana '
                                                                    'to your mana pool. Play this ability as a '
                                                                    'mana source. (VVVV): Untap Grim Monolith.')

Mesmeric_Orb = Artifact('Mesmeric Orb', 2, My.deck, False, 'V', "Whenever a permanent becomes untapped, that "
                                                                "permanent's controller mills a card.")

Reito_Lantern = Artifact('Reito Lantern', 2, My.deck, False, 'V', "(VVV): Put target card from a graveyard on the "
                                                                  "bottom of its owner's library.")

Riptide_Replicator = Artifact('Riptide Replicator', int(input('X: ')) + 4, My.deck, False, 'V', 'As Riptide '
                                                                                                'Replicator comes '
                                                                                                'into play, '
                                                                                                'choose a color and a '
                                                                                                'creature type. '
                                                                                                'Riptide Replicator '
                                                                                                'comes into play with '
                                                                                                'X charge counters on '
                                                                                                'it. (VVVV), '
                                                                                                '(tap): Put an X/X '
                                                                                                'creature toked of '
                                                                                                'the chosen color and '
                                                                                                'type into play, '
                                                                                                'where X is the '
                                                                                                'number of charge '
                                                                                                'counters on Riptide '
                                                                                                'Replicator.')

Staff_of_Domination_0 = Artifact('Staff of Domination', 3, My.deck, False, 'V', '(V): Untap Staff of Domination. ('
                                                                                'VV), (tap): You gain 1 life. ('
                                                                                'VVV), (tap): Untap target '
                                                                                'creature. (VVVV), (tap): Tap '
                                                                                'target creature. (VVVVV), '
                                                                                '(tap): Draw a card.')
Staff_of_Domination_1 = Artifact('Staff of Domination', 3, My.deck, False, 'V', '(V): Untap Staff of Domination. ('
                                                                                'VV), (tap): You gain 1 life. ('
                                                                                'VVV), (tap): Untap target '
                                                                                'creature. (VVVV), (tap): Tap '
                                                                                'target creature. (VVVVV), '
                                                                                '(tap): Draw a card.')
Staff_of_Domination_2 = Artifact('Staff of Domination', 3, My.deck, False, 'V', '(V): Untap Staff of Domination. ('
                                                                                'VV), (tap): You gain 1 life. ('
                                                                                'VVV), (tap): Untap target '
                                                                                'creature. (VVVV), (tap): Tap '
                                                                                'target creature. (VVVVV), '
                                                                                '(tap): Draw a card.')
Staff_of_Domination_3 = Artifact('Staff of Domination', 3, My.deck, False, 'V', '(V): Untap Staff of Domination. ('
                                                                                'VV), (tap): You gain 1 life. ('
                                                                                'VVV), (tap): Untap target '
                                                                                'creature. (VVVV), (tap): Tap '
                                                                                'target creature. (VVVVV), '
                                                                                '(tap): Draw a card.')

# instant
Artificial_Evolution = Instant('Artificial Evolution', 1, My.deck, False, 'U', "Change the text of target spell or "
                                                                               "permanent by replacing all instances "
                                                                               "of one creature type with another. "
                                                                               "The new creature type can't be Legend "
                                                                               "or Wall. (This effect doesn't end at "
                                                                               "end of turn.)")

Capsize = Instant('Capsize', 3, My.deck, False, 'U', "Buyback(VVV) (You may pay an additional (VVV) when you play "
                                                     "this spell. If you do, put it into your hand instead of your "
                                                     "graveyard as part of the spell's effect.) Return target "
                                                     "permanent to owner's hand. ")

Cleansing_Beam = Instant('Cleansing Beam', 5, My.deck, False, 'R', 'Radiance -- Cleansing Beam deals 2 damage to '
                                                                   'target creature and each other creature that '
                                                                   'shares a color with it.')

Glamerdye = Instant('Glamerdye', 2, My.deck, False, 'U', 'Change the text of target spell or permanent by replacing '
                                                         'all instances of one color word with another. Retrace (You '
                                                         'may play this card from your graveyard by discarding a land '
                                                         'card in addition to paying its other costs.)')

Prismatic_Lace = Instant('Prismatic Lace', 1, My.deck, False, 'U', 'Target permanent becomes the color(s) of your '
                                                                   'choice. Costs to tap, maintain, or use an ability'
                                                                   ' of that permanent remain unchanged.')

Reality_Ripple = Instant('Reality Ripple', 2, My.deck, False, 'U', 'Target artifact, creature, or land phases out.')
