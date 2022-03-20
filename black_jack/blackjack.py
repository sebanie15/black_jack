"""
module contains class definitions for the blackjack game

"""

from __future__ import annotations

from abc import ABC, abstractmethod

from .player import Player, Croupier
# from black_jack.deck import Deck
from .boot import Boot
from .exceptions import (
    NotAvailablePlayersException, 
    IsNotInstanceOfPlayerClass,
    IsNotInstanceOfBootClass,
    MaxNumbersOfPlayersExceptions,
    IsNotInstanceOfDeckClass,
    NextPlayerNotAvailable,
    PlayerIsAlreadyInPlayers
)


class BaseBlackJack(ABC):
    """
    Abstract class of blackjack game.

    """
    MAX_NUMBER_OF_PLAYERS = 6

    def __init__(self) -> None:
        self._players = []
        self._player_number = 0
        self._croupier = Croupier('Croupier')
        self._croupier.blackjack = self
        self._cards = []
        self._boot = None

    @property
    @abstractmethod
    def players(self) -> list:
        """
        property returns list of players

        Returns:
            list: list of players
        """

    @property
    @abstractmethod
    def boot(self) -> Boot:
        """ Property returns Deck object

        Returns:
            Deck: Deck object
        """

    @boot.setter
    @abstractmethod
    def boot(self, boot: Boot):
        """ this is setter for the boot

        Arguments:
            boot (Boot): The boot object
        """

    @property
    @abstractmethod
    def croupier(self) -> Croupier:
        """_summary_

        Returns:
            _description_
        """

    @property
    @abstractmethod
    def player(self) -> Player:
        """Method returns actual Player object

        Returns:
            Player: Player object
        """

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
        Method adds a new player to the list of players.
        A player that is already on the list cannot be added.

        Args:
            player (Player): Player object
        """
    @abstractmethod
    def play(self) -> None:
        """ This is the method that starts every game.
            Checks if there are players on the list, adds the dealer if he is\
                 not on the list.
            This method gives the players the first two cards.
        """

    @abstractmethod
    def summary(self) -> dict:
        """The method returns the information summarizing the game 
        in the form of a dictionary

        Returns:
            dict: Dictionary with summary information
        """
    
    @abstractmethod
    def shuffle(self) -> None:
        """ A method that shuffles the cards
        """


class BlackJack(BaseBlackJack):
    """
    _summary_

    """

    @property
    def players(self) -> list:
        # return a list of players
        return self._players

    @property
    def boot(self) -> Boot:
        # return the Deck object
        return self._boot

    @boot.setter
    def boot(self, boot: Boot):
        # if deck is not instance of Deck, raise exception
        # else set the deck
        if not isinstance(boot, Boot):
            raise IsNotInstanceOfBootClass('The boot must be instance of Boot')

        self._boot = boot

    def add_player(self, player: Player) -> None:
        # check if player is instance of Player class
        # check if numbers of players is not the maximum number of players allowed
        # append new player
        if not isinstance(player, Player):
            raise IsNotInstanceOfPlayerClass(
                'The player is not instance of Player\'s class!'
            )
        elif len(self.players) >= self.MAX_NUMBER_OF_PLAYERS:
            raise MaxNumbersOfPlayersExceptions(
                'You have got max numbers of players!'
            )
        if player in self.players:
            raise PlayerIsAlreadyInPlayers('The player you are trying to add\
                 is already on the list of players.')
        
        self._players.append(player)
        player.blackjack = self


    def play(self) -> None:
        # if there are one to MAX_NUMBER_OF_PLAYERS players in the list, add the croupier
        # otherwise, it generates an exception about the lack of players
        if 1 < len(self.players) > self.MAX_NUMBER_OF_PLAYERS:
            raise NotAvailablePlayersException(f'You must add at least one and\
                 maximum {self.MAX_NUMBER_OF_PLAYERS} players!')
        # # check if there is player with name "Croupier"
        # # if not, add Player('Croupier') to the list of players
        # if self.players[-1].name != 'Croupier':
        #     self.add_player(Player('Croupier'))
        # clearing the list of cards for each player
        # and deal of two cards to each player
        for player in self.players:
            player.clear_cards()
            player.hit(2)

        self.croupier.clear_cards()
        self.croupier.hit(2)

        # @TODO algorithm of play

    @property
    def player(self) -> Player:
        # return player object
        return self.players[self._player_number]

    @property
    def croupier(self) -> Croupier:
        # return player object
        return self._croupier

    def next_player(self) -> Player:
        # increasing the player's number on the list
        # returning a player object
        self._player_number += 1

        if self._player_number == len(self.players):
            self._player_number = 0
            raise NextPlayerNotAvailable('There are no more players on the list,\
             the indicator is set to the first player.')

        player =  self.players[self._player_number]
        # player.clear_cards()
        return player

    def summary(self) -> dict:
        return {}

    def shuffle(self):
        # shuffle the deck
        self.boot.shuffle()


class BlackJackUI(BlackJack):
    """_summary_

    Arguments:
        BlackJack -- _description_
    """
    def play(self):
        super().play()


