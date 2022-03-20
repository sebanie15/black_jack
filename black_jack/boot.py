"""_summary_
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from random import shuffle

from black_jack.deck import Deck
from black_jack.card import Card
from black_jack.exceptions import (
    NumberOfDecksOutOfRange,
    IsNotInstanceOfDeckClass,
    NoCardsInBoot
)


class BaseBoot(ABC):
    """_summary_

    Arguments:
        ABC -- abstract class
        MAX_NUMBER_OF_DECKS -- maximum number of decks
    """
    MAX_NUMBER_OF_DECKS = 8

    def __init__(self) -> None:
        """Initialization of object
        """
        self._cards = []

    @abstractmethod
    def shuffle(self) -> None:
        """this method should allows you to shuffle the deck of cards
        """

    @abstractmethod
    def add_cards(self, deck: Deck, number_of_decks: int = 1) -> None:
        """_summary_

        Args:
            deck (Deck): The deck

        Keyword Args:
            number_of_decks (int): The number of decks (default: {1})
        """

    @abstractmethod
    def pop(self) -> Card:
        """_summary_

        Returns:
            _description_
        """

    @abstractmethod
    def __str__(self) -> str:
        """_summary_

        Returns:
            _description_
        """

    @abstractmethod
    def __len__(self) -> int:
        """_summary_

        Returns:
            int: length of list of cards
        """

    @abstractmethod
    def __contains__(self, card: Card) -> bool:
        """_summary_

        Arguments:
            card (Card): object of card

        Returns:
            bool: True if card is on the list of cards otherwise False
        """

    @abstractmethod
    def __iter__(self) -> Card:
        """_summary_

        Returns:
            iterator
        """

    @abstractmethod
    def __next__(self) -> Card:
        """_summary_

        Returns:
            Card: object of card
        """


class Boot(BaseBoot): 
    """_summary_

    Arguments:
        BaseBoot -- _description_
    """
    def shuffle(self): 
        # shuffle the list of cards
        shuffle(self._cards)

    def  add_cards(self, deck: Deck, number_of_decks: int = 1) -> None:
        # check if the number of decks is not out of range
        if 1 < number_of_decks > self.MAX_NUMBER_OF_DECKS:
            raise NumberOfDecksOutOfRange(
                f'You must add at least one deck and maximum ' + 
                f'{self.MAX_NUMBER_OF_DECKS} decks.'
            )
        # check if the deck is instance of a Deck
        if not isinstance(deck, Deck):
            raise IsNotInstanceOfDeckClass('Deck must be instance of Deck')
        # fill the list of cards
        for _ in range(number_of_decks):
            for card in deck:
                self._cards.append(card)

    def pop(self) -> Card:
        # if there is any card in the list of cards
        # pop and return card
        # else raise an exception
        if self._cards:
            return self._cards.pop()
        
        raise NoCardsInBoot('There is no more cards in boot!')

    def __str__(self) -> str:
        return f'{self._cards}'

    def __repr__(self) -> str:
        return f'{self._cards}'

    def __len__(self) -> int:
        # return length of the list of cards
        return len(self._cards)

    def __contains__(self, card: Card) -> bool:
        # returns a card object that is in the list
        return card in self._cards

    def __iter__(self) -> Card:
        self.n = 0
        return self._cards.__iter__()

    def __next__(self) -> Card:
        if self.n < len(self._cards) - 1:
            result = self._cards[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration