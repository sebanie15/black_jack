"""_summary_
"""

from abc import ABC, abstractmethod
from random import shuffle

from json import load

from .card import Card
from .exceptions import (
    NoCardsInDeck,
    NumberOfDecksOutOfRange
)


class BaseDeck(ABC):
    """This is an abstract class that describes a deck of cards.

    Arguments:
        ABC -- abstract class
        CARD_TEMPLATES -- localization of json file as a template of cards
        MAX_NUMBER_OF_DECKS -- maximum number of decks
    """
    CARD_TEMPLATES = "black_jack\cards.json"

    def __init__(self) -> None:
        self._cards = []
        self._prepare_deck()

    @property
    @abstractmethod
    def cards(self) -> list:
        """This property returns list of cards

        Returns:
            List: list of cards
        """

    @abstractmethod
    def _prepare_deck(self) -> None:
        """
            this is a private method that allows you to create all the cards
            in your deck. This method is always run when the object is initialized.
        """

    @abstractmethod
    def __len__(self) -> int:
        """_summary_

        Returns:
            _description_
        """

class Deck(BaseDeck):
    """This is classic deck class

    Arguments:
        BaseDeck -- abstract class of deck
        
    """

    @property
    def cards(self):
        # return list of cards
        return self._cards

    def _prepare_deck(self) -> None:
        # reset the list of cards
        self._cards = []
        # load templates for cards
        with open(self.CARD_TEMPLATES, 'r', encoding='utf-8') as f:
            cards = load(f)
        # create cards
        for key, value in cards["figures"].items():
            for color in cards["colors"].values():
                self._cards.append(Card(key, int(value), color))

    def __len__(self) -> int:
        # return len of cards list
        return len(self._cards)

    def __iter__(self):
        self.n = 0
        return self._cards.__iter__()

    def __next__(self) -> Card:
        if self.n < len(self._cards) - 1:
            result = self._cards[self.n]
            self.n += 1
            return result
        raise StopIteration
