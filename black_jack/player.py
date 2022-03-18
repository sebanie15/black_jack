"""_summary_

Returns:
    _type_: _description_
"""

from abc import ABC, abstractmethod


class BasePlayer(ABC):
    """ Abstract class describes the player """

    def __init__(self, name: str) -> None:
        """Initialization of object

        Args:
            name (str): name of player
        """
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
        """_summary_

        Returns:
            str: _description_
        """

    @abstractmethod
    def __repr__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """

    @abstractmethod
    def win(self) -> None:
        """ method shoud increment the win's value
        """


class Player(BasePlayer):
    """ Player class of abstract object BasePLayer
    """

    def __str__(self) -> str:
        return f'Player {self.name}'

    def __repr__(self) -> str:
        return f'Player {self.name}'

    def win(self) -> None:
        self._wins += 1
