# Magic: The Gathering CPU: dubbed a MPU

# Required skills OOP: needs to __init__ cards(), to save time GUI: the users on the website need to navigate
# comfortably Files: import image files and the paper Magic: The Gathering Is Turing Complete A full sim game needs
# to be run. For this opponent cards before forced state can be arbitrary and fixed. Also the game should give you
# tips as you play

# Layout:
# Homepage {
# Welcome & description
# {MPU: Play}
# {Paper}
# {Contact}
# }

# Optional:
# Games played counter
# Security: not required but helpful



# project burn down
# estimated 3-5 months
# 1-5 hours a day
# total coding time should be 450 hours
# 30 lines an hour
# will be 2000 lines, this is very much on the high end in my view at this time

## indicates it is being worked on
### indicates it is finished

### define card parent
## define each card type
    ### land
        ### define mana usage
    ## creature
        ## combat
    # artifact
    # enchantment
    # sorcery
    # instant
    # planeswalker
## define game structure
    ## drawing cards
    ## define players
    # define the stack
    ## phases
        ## beginning a turn
        ## main
        ## combat
        # again
        # end
## define each card (this and the GUI should take the longest amount of time)
## develop GUI (either here or in the next stage is when I will add the guided assistant for players)
# create website
# finished
# add counter
# add security




#### Starting Hand: 1x Grim Monolith, 1x Power Artifact, 1x Ancient Tomb, 1x Staff of Domination, 2x Lotus Petal, 1x Any other card
#### Play Order:
#### Turn One
#### 1. Ancient Tomb. Tap for two mana.
#### 2. Grim Monolith.
#### 3. Two Lotus Petals. Sacrifice for two blue mana.
#### 4. Enchant Grim Monolith with Power Artifact.
#### 5. Go INFINITE
#### 6. Staff of Domination. Draw your whole deck.
#### 7. Gem Stone Array. This let's you fix your mana pool so you can play anything you want.

def duel(x, y):
    while x.health or y.health != 0:
        # odd enough the win condition for this deck is actually Coalition Victory and happens when the blue assassin comes into play

