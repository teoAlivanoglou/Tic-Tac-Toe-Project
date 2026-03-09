"""
Κύριο αρχείο εκκίνησης της εφαρμογής (Entry point).
Εδώ γίνεται η αρχικοποίηση του παιχνιδιού και της γραφικής διεπαφής.
"""

from window import TicTacToeWindow
from game import Game
from player import HumanPlayer, RandomBot, BetterBot


def main():
    """
    Κύρια συνάρτηση που εκκινεί την εφαρμογή.
    Δημιουργεί αντικείμενα για το παιχνίδι, τους παίκτες και το παράθυρο.
    """
    # game_logic = Game()
    # player1 = HumanPlayer(symbol='X')
    # player2 = RandomBot(symbol='O')
    # app_window = TicTacToeWindow()
    # app_window.start_game(game_logic, player1, player2)
    # app_window.run()

    # Ολό το παρακάτω θα φύγει όταν έρθει το UI γιατί το game loop θα γίνεται εκεί

    def print_board(board):
        """Εκτυπώνει το ταμπλό."""
        print()
        for row in range(3):
            cells = []
            for col in range(3):
                cells.append(board[row * 3 + col])
            print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
            if row < 2:
                print("---+---+---")
        print()

    # Αρχικοποίηση ταμπλό και παικτών

    game = Game(3)
    bot1 = BetterBot("X")  # Παίκτης 1
    bot2 = BetterBot("O")  # Παίκτης 2
    game.start(bot1, bot2)

    print(f"=== {type(bot1).__name__} vs {type(bot2).__name__} ===")
    print(f"Παίκτης 1: {type(bot1).__name__} ({bot1.symbol})")
    print(f"Παίκτης 2: {type(bot2).__name__} ({bot2.symbol})")

    # Ο μέγιστος αριθμός γύρων είναι όσες και οι θέσεις του ταμπλό
    for turn in range(game.get_board_size() * game.get_board_size()):
        player = game.get_current_player()

        valid_move = False

        # Αμυντικός προγραμματισμός
        while not valid_move:
            move = player.get_move(game)
            valid_move = game.play_turn(move)

        print(
            f"--- Γύρος {turn + 1}: {type(player).__name__} ({player.symbol}) παίζει στη θέση {move} ---"
        )
        board = game.get_board()
        print_board(board)

        if game.check_win(player.symbol):
            print(f"Νίκησε ο {type(player).__name__} ({player.symbol})!")
            break

    else:
        print("Ισοπαλία!")


if __name__ == "__main__":
    main()
