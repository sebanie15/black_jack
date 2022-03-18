"""

Returns:
    _description_
"""

from abc import ABC, abstractmethod


class BaseCard(ABC):
    """ An abstract representation of the base class that describes the card """
    @abstractmethod
    def __init__(self, figure: str, value: int, color) -> None:
        """Object initialization

        Args:
            figure (str): figure name
            value (int): the numerical value of the card
            color (): card suit reprezentation
        """

    @abstractmethod
    def __str__(self) -> str:
        """The special method is responsible for returning the text defined
            when displaying the object

        Returns:
            str: text describing the object
        """

    @abstractmethod
    def __repr__(self) -> str:
        """The special method is responsible for returning the text defined
        during the representation of the object

        Returns:
            str: object reprezentation
        """

    @property
    @abstractmethod
    def figure(self) -> str:
        """Property theat describes the figure

        Returns:
            str: text representation of a figure
        """

    @property
    @abstractmethod
    def value(self) -> int:
        """Property type method that determines the value of the card

        Returns:
            int: the numerical value of the card
        """


class Card(BaseCard):
    """_summary_

    Args:
        BaseCard (class): abstract class of Card
    """

    def __init__(self, figure: str, value: int, color) -> None:
        super().__init__(figure, value, color)
        self._figure = figure
        self._value = value
        self._color = color

    def __str__(self) -> str:
        """ The special method is responsible for returning the text defined
            when displaying the object
            e.g. str(Card)

        Returns:
            str: text describing the object
        """
        return f"{self._figure}{self._color}"

    def __repr__(self) -> str:
        """The special method is responsible for returning the text defined
        during the representation of the object
            e.g. print([Card])

        Returns:
            str: text representation of a figure
        """
        return f'{self._figure}{self._color}'

    @property
    def figure(self) -> str:
        """Property theat describes the figure

        Returns:
            str: text representation of a figure
        """
        return self._figure

    @property
    def value(self) -> int:
        """Property type method that determines the value of the card

        Returns:
            int: the numerical value of the card
        """
        return self._value
