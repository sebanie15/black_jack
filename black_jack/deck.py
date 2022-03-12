"""_summary_
"""

from abc import ABC, abstractmethod
from random import shuffle

from json import load, dump

from .card import Card


_cards_DIR = "black_jack\cards.json"

def load__cards():
    with open(_cards_DIR, 'r') as f:
        return load(f)

CARD_FIGURES = load__cards()['card']
CARD_COLORS = load__cards()['color']


class BaseDeck(ABC):
    """_summary_

    Arguments:
        ABC -- _description_
    """
    
    def __init__(self) -> None:
        self._cards = [Card]
        self._prepare__cards()

    @property
    def cards(self) -> list[Card]:
        """This method returns list of cards

        Returns:
            list of cards
        """
        return self._cards

    @abstractmethod
    def _prepare__cards(self) -> None:
        """_summary_
        """
        pass

    @abstractmethod
    def shuffle(self):
        pass

    @abstractmethod
    def give_card(self) -> Card:
        pass


class Deck(BaseDeck):
    """_summary_

    Arguments:
        BaseDeck -- _description_

    Returns:
        _description_
    """
    CARD_TEMPLATES = "black_jack\cards.json"

    def _prepare__cards(self) -> None:
        """_summary_
        """
        with open(self.CARD_TEMPLATES, 'r') as f:
            cards = load(f)

        for key, value in cards["card"].items():
            for color in cards["color"].keys():
                self._cards.append(Card(key, value, color))
    
    def shuffle(self) -> None:
        """_summary_
        """
        shuffle(self._cards)

    def give_card(self):
        """_summary_

        Returns:
            Its return one card or None
        """
        return self._cards.pop() if len(self._cards) > 0 else None
