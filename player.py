from hand import Hand
from card import Card

class Player:
  """ A player is identified by a unique name and has one hand containing two or more cards"""
  def __init__(self, name):
    self.name = name

  # decide to hit or not
  def shouldContinue(self):
    return self.hand.total() <= 16

  # deals a new hand with two random cards
  def dealNew(self):
    self.hand = Hand.new([Card.draw(). Card.draw()])




if __name__ == "__main__":
  player = Player('Nicole')
  player.hand = Hand([Card('hearts', 10), Card('clubs', 2)])

  assert player.shouldContinue() == True

  player.hand.hit(Card('hearts', 8))
  assert player.shouldContinue() == False


