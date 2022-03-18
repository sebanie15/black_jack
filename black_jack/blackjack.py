from abc import ABC, abstractmethod


class BaseBlackJack(ABC):

    @abstractmethod
    def __init__(self) -> None:
        self._players = []
        self._cards = []
    
    @property
    @abstractmethod
    def players(self):
        pass


class BlackJack(BaseBlackJack):

    pass
