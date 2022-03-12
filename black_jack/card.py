"""_summary_

Returns:
    _description_
"""

from abc import ABC, abstractmethod
import re



class CardColor:

    def __init__(self, color_value: str) -> None:
        self.color_value = color_value


class BaseCard(ABC):
    """_summary_

    Arguments:
        ABC -- _description_
    """

    def __init__(self, figure: str, value: int, color) -> None:
        """_summary_

        Arguments:
            figure -- _description_
            value -- _description_
            color -- _description_
        """
        self._figure = figure
        self._value = value
        self._color = color

    def __str__(self):
        return f"{self._figure} - {self._color}.decode('unicode')"

    def __repr__(self):
        return f'{self._figure} - {self._color}'

    @property
    def figure(self) -> str:
        return self._figure

    @property
    def value(self) -> int:
        return self._value


class Card(BaseCard):
    pass
