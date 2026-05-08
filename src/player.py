"""
Αρχείο που περιέχει τις κλάσεις για τους παίκτες (Άνθρωπος, Υπολογιστής).
"""

import random
import config
from game import Game


class Player:
    """
    Βασική κλάση (Base Class) για αναπαράσταση ενός παίκτη.
    Οι υποκλάσεις ορίζουν is_human = True/False ανάλογα τον τύπο.
    """

    is_human = True  # Προεπιλογή: ανθρώπινος παίκτης

    def __init__(self, name, symbol):
        """
        Αρχικοποιεί τον παίκτη με το όνομά του και το σύμβολό του.
        :param name: Το όνομα του παίκτη
        :param symbol: Το σύμβολο του παίκτη (SYMBOL_X ή SYMBOL_O)
        """
        self.name = name
        self.symbol = symbol

    def get_move(self, game):
        """
        Υπολογίζει και επιστρέφει την επόμενη κίνηση του παίκτη.
        Πρέπει να υλοποιηθεί από τις υποκλάσεις.
        """
        pass


class HumanPlayer(Player):
    """
    Κλάση που αναπαριστά έναν ανθρώπινο παίκτη.
    """

    is_human = True

    def get_move(self, game):
        """Επιστρέφει την κίνηση που επέλεξε ο χρήστης μέσω του UI."""
        pass


class RandomBot(Player):
    """
    Κλάση που αναπαριστά έναν αυτοματοποιημένο παίκτη (Bot) ο οποίος επιλέγει κινήσεις εντελώς τυχαία.
    """

    is_human = False

    def get_move(self, game):
        """Βρίσκει κενές θέσεις στο ταμπλό και επιλέγει μία τυχαία."""

        return random.choice(game.get_empty_spaces())


class BetterBot(Player):
    """
    Κλάση που αναπαριστά έναν αυτοματοποιημένο παίκτη (Bot) ο οποίος επιλέγει κινήσεις πιο μεθοδικά.
    """

    is_human = False

    def get_move(self, game):
        """Βρίσκει κενές θέσεις στο ταμπλό και επιλέγει μία μεθοδικά."""

        empty_spaces = game.get_empty_spaces()

        # Επίθεση
        for i in empty_spaces:
            # Δοκιμάζει αν αυτή η κίνηση νικάει
            if game.check_win(self.symbol, i):
                # Νικάει άρα "παίζει" εκεί
                return i

        # Άμυνα
        for i in empty_spaces:
            # Βρίσκουμε το σύμβολο του αντπάλου
            enemy_symbol = (
                config.SYMBOL_X if self.symbol == config.SYMBOL_O else config.SYMBOL_O
            )

            # Δοκιμάζει αν με αυτή η κίνηση νικάει ο αντίπαλος
            if game.check_win(enemy_symbol, i):
                # Αν ο αντίπαλος παίξει εκεί τότε νικάει.
                # Άρα πρέπει να τον μπλοκάρει!
                return i

        # Δεν μπορεί ούτε να νικήσει ούτε χρειάζεται να μπλοκάρει, οπότε διαλέγει τυχαία
        return random.choice(empty_spaces)


class MinimaxBot(Player):
    """
    Κλάση που αναπαριστά έναν αυτοματοποιημένο παίκτη (Bot) ο οποίος επιλέγει κινήσεις με την μέθοδο minimax.
    """

    is_human = False

    def get_move(self, game):
        """Βρίσκει κενές θέσεις στο ταμπλό και επιλέγει την καλύτερη δυνατή κίνηση."""
        board = game.get_board()
        my_symbol = self.symbol
        enemy_symbol = (
            config.SYMBOL_X if my_symbol == config.SYMBOL_O else config.SYMBOL_O
        )

        # Θα αποθηκεύω τα minimax scores για να μην υπολογίζω το ίδιο board πάνω απο μία φορά (memoization)
        # https://www.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/improving-efficiency-of-recursive-functions
        self.cache = {}

        best_score = -1000
        move = -1

        for i in game.get_empty_spaces():
            board[i] = my_symbol
            score = self.minimax(board, 0, False, my_symbol, enemy_symbol)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
        return move

    def minimax(self, board, depth, is_maximizing, my_symbol, enemy_symbol):
        """Αναδρομική μέθοδος minimax για τον υπολογισμό του σκορ κάθε κίνησης."""

        # Ελέγχω αν έχω ήδη υπολογίσει αυτό το board και αν ναι, το επιστρέφω
        key = (tuple(board), is_maximizing)
        if key in self.cache:
            return self.cache[key]

        if self._winner(board, my_symbol):
            return 10 - depth
        if self._winner(board, enemy_symbol):
            return depth - 10
        if " " not in board:
            return 0

        if is_maximizing:
            best_score = -1000
            for i in range(len(board)):
                if board[i] == " ":
                    board[i] = my_symbol
                    score = self.minimax(
                        board, depth + 1, False, my_symbol, enemy_symbol
                    )
                    board[i] = " "
                    best_score = max(score, best_score)
        else:
            best_score = 1000
            for i in range(len(board)):
                if board[i] == " ":
                    board[i] = enemy_symbol
                    score = self.minimax(
                        board, depth + 1, True, my_symbol, enemy_symbol
                    )
                    board[i] = " "
                    best_score = min(score, best_score)

        self.cache[key] = best_score
        return best_score

    def _winner(self, board, s):
        """Εσωτερική μέθοδος ελέγχου νικητή για την προσομοίωση."""
        # Έλεγχος γραμμών, στηλών και διαγωνίων (3x3)
        return (
            (board[0] == board[1] == board[2] == s)
            or (board[3] == board[4] == board[5] == s)
            or (board[6] == board[7] == board[8] == s)
            or (board[0] == board[3] == board[6] == s)
            or (board[1] == board[4] == board[7] == s)
            or (board[2] == board[5] == board[8] == s)
            or (board[0] == board[4] == board[8] == s)
            or (board[2] == board[4] == board[6] == s)
        )

#Απο εδω και κάτω βαζω κώδικα για φωτογραφιες στην ομαδικη εκθεση 
if __name__ == "__main__":
    # 1. Προετοιμασία Παιχνιδιού
    game = Game(3)
    # Ορίζουμε σύμβολα βάσει του config
    minimax_bot = MinimaxBot("Minimax AI", config.SYMBOL_X)
    
    # 2. Δημιουργία "Κρίσιμου" Ταμπλό
    # Το Χ (Minimax) παίζει. 
    # Έχει δύο επιλογές: 
    # α) Να κερδίσει στη θέση 2 
    # β) Να εμποδίσει το Ο (που έχει 2 σύμβολα στις θέσεις 3,4)
    
    test_board = [
        config.SYMBOL_X, config.SYMBOL_X, config.SYMBOL_EMPTY, # Γραμμή 0: [X, X,  ] -> Εδώ πρέπει να παίξει
        config.SYMBOL_O, config.SYMBOL_O, config.SYMBOL_EMPTY, # Γραμμή 1: [O, O,  ]
        config.SYMBOL_EMPTY, config.SYMBOL_EMPTY, config.SYMBOL_EMPTY
    ]
    game._board = test_board

    print("\nΤρέχουσα Κατάσταση Ταμπλό (Το X παίζει):")
    board = game.get_board()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

    print("\n[Υπολογισμός κίνησης...]")
    best_move = minimax_bot.get_move(game)
    
    print(f"\nΑΠΟΦΑΣΗ BOT: Το {minimax_bot.name} επέλεξε τη θέση {best_move}")
    
    if best_move == 2:
        print("RESULT: SUCCESS  (Το Bot επέλεξε τη νίκη)")
    else:
        print("RESULT: FAILED ")
    print("="*50)