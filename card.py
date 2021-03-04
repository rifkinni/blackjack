import random

class Card:
  """A card represents a single card in the game, and is uniquely identified by a suit and a value"""
  suits = ['hearts', 'clubs', 'spades', 'diamonds']
  values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace']

  def __init__(self, suit, value):
    self.suit = suit
    self.raw_value = value

  #draw a random card
  @staticmethod
  def draw(): 
    return Card(random.choice(Card.suits), random.choice(Card.values))

  def value(self):
    if (type(self.raw_value) == int):
      return self.raw_value
    elif (self.raw_value == 'ace'):
      return 11
    else:
      return 10

  def updateAceValue(self):
    if self.raw_value == 'ace':
      self.raw_value = 1










if __name__ == "__main__":
  # all face cards have a value of 10
  assert Card('hearts', 'jack').value() == 10

  # all numbered cards have their numbered value
  assert Card('spades', 5).value() == 5

  ace = Card('clubs', 'ace')

  # aces have a value of 11
  assert ace.value() == 11

  # I can update an aces value to 1
  ace.updateAceValue()
  assert ace.value() == 1
