from card import Card
import pdb

class Hand:
  """A hand should be initialized with two Cards. More cards may be added to a hand as the game progresses."""
  def __init__(self, cards):
    if (len(cards) != 2):
      raise Exception('A hand should be initialized with two cards')
    self.cards = cards

  def total(self):
    if self._calculateSum() > 21:
      for card in cards:
        if card.value() == 11:
          card.updateAceValue()
          break
    return self._calculateSum()

  def hit(self, newCard):
    self.cards.append(newCard)

  def _calculateSum(self):
    return sum(map(lambda card: card.value(), self.cards))










if __name__ == "__main__":
  # I can create a hand with two cards
  cards = [Card('hearts', 'ace'), Card('clubs', 2)]
  hand = Hand(cards)

  # I can get the total blackjack value for that hand
  assert hand.total() == 13

  # I can add a new card to my hand ('hit')
  newCard = Card('hearts', 9)
  hand.hit(newCard)

  # I will update the ace value if I go over 21
  assert hand.total() == 12

  # I cannot create a hand with more than two cards
  try: 
    Hand(cards +[newCard])
    raise Exception('uhoh')
  except Exception as e:
    assert e.message == 'A hand should be initialized with two cards'






