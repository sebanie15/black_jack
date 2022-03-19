"""_summary_
"""

from abc import ABC, abstractmethod
from random import shuffle

from json import load

from .card import Card
from black_jack.exceptions import NoCardsInDeck


class BaseDeck(ABC):
    """This is an abstract class that describes a deck of cards.

    Arguments:
        ABC -- abstract class
    """
    def __init__(self, number_of_decks: int = 1) -> None:
        self._number_of_decks = number_of_decks
        self._cards = []
        self._prepare_deck()

    @property
    def cards(self) -> list:
        """This method returns list of cards

        Returns:
            list of cards
        """
        return self._cards

    @abstractmethod
    def _prepare_deck(self) -> None:
        """
            this is a private method that allows you to create all the cards
            in your deck. This method is always run when the object is initialized.
        """

    @abstractmethod
    def shuffle(self):
        """ this method shoud allows you to shuffle the deck of cards """

    @abstractmethod
    def hit(self) -> Card:
        """ method should return one card from list """


class Deck(BaseDeck):
    """This is classic deck class

    Arguments:
        BaseDeck -- abstract class of deck
        CARD_TEMPLATES -- localization of json file as a template of cards
    """
    CARD_TEMPLATES = "black_jack\cards.json"

    def _prepare_deck(self) -> None:
        """
            this is a private method that allows you to create all the cards
            in your deck. This method is always run when the object is
            initialized.

        """
        # 1. reset the list of cards
        # 2. load templates for cards
        # 3. create cards
        self._cards = []
        with open(self.CARD_TEMPLATES, 'r', encoding='utf-8') as f:
            cards = load(f)

        for _ in range(self._number_of_decks):
            for key, value in cards["figures"].items():
                for color in cards["colors"].values():
                    self._cards.append(Card(key, value, color))

    def shuffle(self) -> None:
        """ this method shoud allows you to shuffle the deck of cards """
        shuffle(self._cards)

    def hit(self) -> Card:
        """_summary_

        Returns:
            Its return one card or None
        """
        if self._cards:
            return self._cards.pop()
        else: 
            raise NoCardsInDeck('There is no more cards in deck!')
