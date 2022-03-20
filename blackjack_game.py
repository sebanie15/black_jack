
from black_jack import BlackJack, Deck, Player, Boot
from black_jack.exceptions import NextPlayerNotAvailable


def print_line():
    print('-' * 50)


def add_cards_and_shuffle(boot: Boot):
    try:
        deck_count = int(input('Podaj iloma taliami będziesz grał (1-8): '))
        game.boot.add_cards(Deck(), deck_count)
        game.boot.shuffle()
        print(game.boot)
    except ValueError as e:
        print(e)


def add_players(game: BlackJack):
    while True:
        command = input('Czy chcesz wprowadzić gracza? T/n: ')
        if command == '' or command == 't' or command == 'T':
            game.add_player(Player(input('Podaj imię gracza : ')))
        elif command == 'n' or command == 'N':
            break


if __name__ == '__main__':
    game = BlackJack()
    game.boot = Boot()
    # add cards and shuffle boot
    add_cards_and_shuffle(game.boot)
    # add players
    add_players(game)
    # start the game
    game.play()

    print('Gra rozpoczęta, rozdano każdemu graczowi po dwie karty.')
    print_line()

    print(f'{game.croupier} - [{game.croupier.cards[0]}, ?]')
    print_line()

    #print points
    for player in game.players:
        print(f'{player}: Karty {player.cards}, Punkty {player.points}')
    print_line()
    print_line()

    player = game.player
    print(f'{player}:')
    print_line()

    while True:
        
        print(f'    Karty {player.cards}, Punkty {player.points}')
        command = input('Co chcesz zrobić? 0 - hit, 1 - stand: ')
        if command == '0':
            player.hit()

        if command == '1' or player.points >= 21:
            print(f'    Karty {player.cards}, Punkty {player.points}')
            # print_line()
            try:
                player.stand()
                player = game.player
                print(f'{player}:')
                print_line()
                
            except NextPlayerNotAvailable:
                player = game.croupier
                
                while player.points < 17:
                    player.hit()
                print(f'{player}:')
                print_line()
                print(f'    Karty {player.cards}, Punkty {player.points}')
                
                break
