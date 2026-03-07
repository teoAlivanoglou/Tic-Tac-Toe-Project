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

    game_logic = Game()

    board = game_logic.get_board()
    bot1 = RandomBot("X")  # Παίκτης 1
    bot2 = BetterBot("O")  # Παίκτης 2
    players = [bot1, bot2]
    current = 0  # Δείκτης για τον τρέχοντα παίκτη (0 ή 1)

    print(f"=== {type(bot1).__name__} vs {type(bot2).__name__} ===")
    print(f"Παίκτης 1: {type(bot1).__name__} ({bot1.symbol})")
    print(f"Παίκτης 2: {type(bot2).__name__} ({bot2.symbol})")

    # Ο μέγιστος αριθμός γύρων είναι όσες και οι θέσεις του ταμπλό
    for turn in range(len(board)):
        player = players[current]
        move = player.get_move(board)

        # Τοποθετεί το σύμβολο στο ταμπλό (πάντα εδώ, ανεξάρτητα από το bot)
        # Γενικά καλό είναι να αποφύγουμε να αφήνουμε τα bot να επηρεάζουν το ταμπλό
        # Καλύτερα είναι τα bot (και οι παίχτες) να λένε στο game manager "Θέλω να παίξω εκεί (game_logic.play_turn(x, y))"
        board[move] = player.symbol

        print(
            f"--- Γύρος {turn + 1}: {type(player).__name__} ({player.symbol}) παίζει στη θέση {move} ---"
        )
        print_board(board)

        # Έλεγχος νίκης με check_win του ίδιου του παίκτη
        # Όπως και πιο πάνω, ίσως καλύτερα να ήταν αυτός ο έλεγχος να γίνεται απο το game manager
        if player.check_win(board, player.symbol):
            print(f"Νίκησε ο {type(player).__name__} ({player.symbol})!")
            break

        current = 1 - current  # Εναλλαγή παίκτη (0→1, 1→0)
    else:
        print("Ισοπαλία!")


if __name__ == "__main__":
    main()
