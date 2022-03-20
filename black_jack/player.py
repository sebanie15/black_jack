"""
module contains class definitions for the player
"""
from __future__ import annotations, absolute_import
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .blackjack import BlackJack

from .exceptions import (
    TooManyCardsToHit
)


class BasePlayer(ABC):
    """ Abstract class describes the player """

    def __init__(self, name: str) -> None:
        """
        Initialization of object

        Args:
            name (str): name of player
        """
        # self._cards -> list of cards, only for one game
        # self._wins -> number of wins
        # self.blackjack -> assignment to blackjack game
        self._name = name
        self._cards = []
        self._wins = 0
        self.blackjack: BlackJack = None

    @property
    @abstractmethod
    def name(self) -> str:
        """ property returns name of player

        Returns:
            str: name of player
        """

    @property
    @abstractmethod
    def wins(self) -> int:
        """ Property returns number of wins

        Returns:
            int: number of wins
        """

    @property
    @abstractmethod
    def cards(self) -> list:
        """ Property returns list of cards of player

        Returns:
            List: list of cards of player
        """

    @property
    @abstractmethod
    def points(self) -> int:
        """ Property returns number of points of player

        Returns:
            int: number of points of player
        """

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
        """ method should increment the win's value
        """

    @abstractmethod
    def hit(self, number_of_cards: int = 1) -> None:
        """drawing a card to get a score close to 21

        Args:
            number_of_cards (int): number of cards that player hit

        Returns:
            _type_: _description_
        """

    @abstractmethod
    def stand(self):
        """no move if the cards score close to 21
        """
    
    # @abstractmethod
    # def double_down(self):
    #     """doubling the stake (possible with two cards)
    #     """

    # @abstractmethod
    # def split(self):
    #     """ doubling cards of the same value and adding a second stake equal\
    #         to the value of the first
    #     """

    # @abstractmethod
    # def insurance(self):
    #     """insurance (possible when the dealer's face up card is an ace)
    #     """

    @abstractmethod
    def clear_cards(self) -> None:
        """ It's clearing the cards list before next move in the game
        """


class Croupier(BasePlayer):
    """_summary_

    Arguments:
        BasePlayer -- _description_
    """
    @property
    def name(self) -> str:
        # return the name of the player
        return self._name

    @property
    def wins(self) -> int:
        # return the number of wins
        return self._wins

    @property
    def cards(self) -> list:
        # return list of cards
        return self._cards

    @property
    def points(self) -> int:
        # return points
        number_of_cards = len(self._cards)
        points = 0

        # if player has only two cards
        if number_of_cards == 2:
            if self.cards[0].figure == 'Ace' or self.cards[1].figure == 'Ace':
                if self.cards[0].value == 10 or self.cards[1].value == 10:
                    points = 21
                    return points
        
        # if player has more then two cards
        for card in self.cards:
            points += card.value
        return points

    def __str__(self) -> str:
        return f'{self.name}'

    def __repr__(self) -> str:
        return f'{self.name}'

    def win(self) -> None:
        # increment the player's win value
        self._wins += 1

    def clear_cards(self) -> None:
        # clear cards before next game
        self._cards.clear()

    def hit(self, number_of_cards: int = 1) -> None:
        # if player has more or equal two cards
        if len(self._cards) >= 2 and number_of_cards > 1:
            raise TooManyCardsToHit(f'You\'ve got {len(self._cards)} cards.\
                 You cannot hit more than one card.')
        # add card(s) to list of player's cards
        for _ in range(number_of_cards):
            self._cards.append(self.blackjack.boot.pop())

    def stand(self):
        # the player stand, next player is selected
        self.blackjack.next_player()


class Player(Croupier):
    """
    Player class of abstract object BasePLayer
    """
    def __str__(self) -> str:
        return f'(Player) {self.name}'

    def __repr__(self) -> str:
        return f'(Player) {self.name}'

    def hit(self, number_of_cards: int = 1) -> None:
        # if player has more or equal two cards
        if len(self._cards) >= 2 and number_of_cards > 1:
            raise TooManyCardsToHit(f'You\'ve got {len(self._cards)} cards.\
                 You cannot hit more than one card.')
        # add card(s) to list of player's cards
        for _ in range(number_of_cards):
            self._cards.append(self.blackjack.boot.pop())

    def stand(self):
        # the player stand, next player is selected
        self.blackjack.next_player()
    
    def double_down(self):
        pass

    def split(self):
        pass

    def insurance(self):
        pass
