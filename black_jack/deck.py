"""_summary_
"""

from abc import ABC, abstractmethod
from random import shuffle

from json import load, dump

from .card import Card


class BaseDeck(ABC):
    """This is an abstract class that describes a deck of cards.

    Arguments:
        ABC -- abstract class
    """
    
    def __init__(self) -> None:
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
            in your deck. This method is always run when the object is 
            initialized.
        """
        pass

    @abstractmethod
    def shuffle(self):
        """this method shoud allows you to shuffle the deck of cards
        """
        pass

    @abstractmethod
    def give_card(self) -> Card:
        pass


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
        with open(self.CARD_TEMPLATES, 'r') as f:
            cards = load(f)

        for key, value in cards["card"].items():
            for color in cards["color"].keys():
                self._cards.append(Card(key, value, color))
    
    def shuffle(self) -> None:
        """this method shoud allows you to shuffle the deck of cards
        """
        shuffle(self._cards)

    def give_card(self):
        """_summary_

        Returns:
            Its return one card or None
        """
        return self._cards.pop() if len(self._cards) > 0 else None
