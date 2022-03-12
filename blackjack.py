
from black_jack.deck import Deck

my_deck = Deck()

print(my_deck.cards)
print(len(my_deck.cards))
my_deck.shuffle()
print(my_deck.cards)
