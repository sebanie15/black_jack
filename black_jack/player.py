"""
module contains class definitions for the player
"""

from abc import ABC, abstractmethod
from black_jack.card import Card

from black_jack.deck import Deck


class BasePlayer(ABC):
    """ Abstract class describes the player """

    def __init__(self, name: str) -> None:
        """
        Initialization of object

        Args:
            name (str): name of player
        """
        # self._point -> pivate propertise 
        # self._wins -> private propertise, number of wins

        self._name = name
        self._points = 0
        self._wins = 0

    @property
    def name(self) -> str:
        """ property returns name of palyer

        Returns:
            str: name of player
        """
        return self._name

    @abstractmethod
    def __str__(self) -> str:
        """ The special method is responsible for returning the text defined
            when displaying the object
            e.g. str(Player)

        Returns:
            str: text describing the object
        """

    @abstractmethod
    def __repr__(self) -> str:
        """The special method is responsible for returning the text defined
        during the representation of the object
            e.g. print(Player)

        Returns:
            str: text representation of a figure
        """

    @abstractmethod
    def win(self) -> None:
        """ method shoud increment the win's value
        """

    @abstractmethod
    def take_card(self, deck: Deck) -> None:
        """_summary_

        Returns:
            _type_: _description_
        """


class Player(BasePlayer):
    """
    Player class of abstract object BasePLayer
    """

    def __str__(self) -> str:
        return f'Player {self.name}'

    def __repr__(self) -> str:
        return f'Player {self.name}'

    def win(self) -> None:
        self._wins += 1

    def take_card(self, deck: Deck) -> Card:
        return deck.hit()
