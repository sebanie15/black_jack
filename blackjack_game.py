
from black_jack import BlackJackUI, Deck, Player, Boot
from black_jack.exceptions import NextPlayerNotAvailable


if __name__ == '__main__':
    game = BlackJackUI()
    game.boot = Boot()
    game.play()


