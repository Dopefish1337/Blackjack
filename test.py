#-*-coding:utf8;-*-
#qpy:2
#qpy:console

print """
This is Blackjack counting.
The card values are as follows: 
2-6 = +1, 7-9 = 0, 10-Ace= -1 
At the end, your running count should
be zero. Happy counting!
"""

from random import randint 
from random import shuffle
from itertools import product

cards = [['ace', '2', '3', '4', '5',
          '6', '7', '8', '9', '10',
          'Jack', 'Queen', 'King', 
          'Ace'], ['Spades', 'Hearts',
          'Clubs', 'Diamonds']]
      
running_count = 0

class Card(object):

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def draw(self):
        print self.value, "of", self.suit
                

twoS = Card ('2', 'Spades')
twoH = Card ('2', 'Hearts')
twoC = Card ('2', 'Clubs')
twoD = Card ('2', 'Diamonds')
threeS = Card ('3', 'Spades')
threeH = Card ('3', 'Hearts')
threeC = Card ('3', 'Clubs')
threeD = Card ('3', 'Diamonds')
fourS = Card ('4', 'Spades')
fourH = Card ('4', 'Hearts')
fourC = Card ('4', 'Clubs')
fourD = Card ('4', 'Diamonds')
fiveS = Card ('5', 'Spades')
fiveH = Card ('5', 'Hearts')
fiveC = Card ('5', 'Clubs')
fiveD = Card ('5', 'Diamonds')
sixS = Card ('6', 'Spades')
sixH = Card ('6', 'Hearts')
sixC = Card ('6', 'Clubs')
sixD = Card ('6', 'Diamonds')
sevenS = Card ('7', 'Spades')
sevenH = Card ('7', 'Hearts')
sevenC = Card ('7', 'Clubs')
sevenD = Card ('7', 'Diamonds')
eightS = Card ('8', 'Spades')
eightH = Card ('8', 'Hearts')
eightC = Card ('8', 'Clubs')
eightD = Card ('8', 'Diamonds')
nineS = Card ('9', 'Spades')
nineH = Card ('9', 'Hearts')
nineC = Card ('9', 'Clubs')
nineD = Card ('9', 'Diamonds')
tenS = Card ('10', 'Spades')
tenH = Card ('10', 'Hearts')
tenC = Card ('10', 'Clubs')
tenD = Card ('10', 'Diamonds')
JS = Card ('Jack', 'Spades')
JH = Card ('Jack', 'Hearts')
JC = Card ('Jack', 'Clubs')
JD = Card ('Jack', 'Diamonds')
QS = Card ('Queen', 'Spades')
QH = Card ('Queen', 'Hearts')
QC = Card ('Queen', 'Clubs')
QD = Card ('Queen', 'Diamonds')
KS = Card ('King', 'Spades')
KH = Card ('King', 'Hearts')
KC = Card ('King', 'Clubs')
KD = Card ('King', 'Diamonds')
AS = Card ('Ace', 'Spades')
AH = Card ('Ace', 'Hearts')
AC = Card ('Ace', 'Clubs')
AD = Card ('Ace', 'Diamonds')

deck_of_cards = [
        twoS, twoH, twoC, twoD,
        threeS, threeH, threeC, threeD,
        fourS, fourH, fourC, fourD,
        fiveS, fiveH, fiveC, fiveD,
        sixS, sixH, sixC, sixD,
        sevenS, sevenH, sevenC, sevenD,
        eightS, eightH, eightC, eightD,
        nineS, nineH, nineC, nineD,
        tenS, tenH, tenC, tenD,
        JS, JH, JC, JD, QS, QH, QC, QD,
        KS, KH, KC, KD,
        AS, AH, AC, AD
        ]



shuffle(deck_of_cards)

def drawcard():

    
    print """
    press Enter to draw card
        """
        
    action = raw_input('> ')
        
    if action == '' and len(deck_of_cards)>0:
        deck_of_cards.pop().draw()
        drawcard()
    elif action == '' and len(deck_of_cards)==0:
        print """
        That was that! Hope you arrived
        at 0. If not, you fucked up.
        """
    else:
        print "Wrong"
        drawcard()
        
drawcard()

