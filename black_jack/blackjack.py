"""
module contains class definitions for the blackjack game

"""

from abc import ABC, abstractmethod
import imp

from black_jack.player import Player
from black_jack.exceptions import (
    NotAvailablePlayersException, 
    PlayerIsNotInstanceOfPlayerClass,
    MaxNumbersOfPlayersExceptions
)


class BaseBlackJack(ABC):
    """
    Abstract class of blackjack game.

    """

    def __init__(self) -> None:
        self._players = []
        self._player_number = 0
        self._cards = []

    @property
    def players(self) -> list:
        """
        method returns list of players

        Returns:
            list: list of players
        """
        return self._players

    @abstractmethod
    def next_player(self) -> Player:
        """
        _summary_

        Returns:
            Player: _description_
        """

    @abstractmethod
    def add_player(self, player: Player) -> None:
        """
        Method shoud add new player to list of players
        e.g. self._players.append(player)

        Args:
            player (Player): Player object
        """
    @abstractmethod
    def play(self) -> None:
        """_summary_
        """

    @abstractmethod
    def summary(self) -> dict:
        """_summary_

        Returns:
            dict: _description_
        """
    
    @abstractmethod
    def shuffle(self) -> None:
        """_summary_

        Raises:
            PlayerIsNotInstanceOfPlayerClass: _description_
            NotAvailablePlayersException: _description_

        Returns:
            _type_: _description_
        """


class BlackJack(BaseBlackJack):
    """
    _summary_

    """

    def add_player(self, player: Player) -> None:
        # check if player is instance of Player class
        # check if numbers of players is not maximum
        # append new player
        if not isinstance(player, Player):
            raise PlayerIsNotInstanceOfPlayerClass(
                'The player is not instance of Player\'s class!'
            )
        elif len(self.players) > 3:
            raise MaxNumbersOfPlayersExceptions(
                'You have got max numbers of players!'
            )
        
        self._players.append(player)

    def play(self) -> None:
        # if there are one to three players on the list, I add the croupier
        # otherwise, it generates an exception about the lack of players
        if 1 < len(self.players) < 3:
            self.add_player(Player('Croupier'))
        else:
            raise NotAvailablePlayersException('You must add at least one and maximum tree players!')

        while self._cards:
            player = self.next_player

        # @TODO algorithm of play

    def next_player(self) -> Player:
        # increasing the player's number on the list
        # returning a player object
        if self._player_number < len(self.players) - 1:
            self._player_number += 1
            return self.players[self._player_number]
        return None

    def summary(self) -> dict:
        return {}
