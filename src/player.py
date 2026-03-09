"""
Αρχείο που περιέχει τις κλάσεις για τους παίκτες (Άνθρωπος, Υπολογιστής).
"""

import random
from game import Game


class Player:
    """
    Βασική κλάση (Base Class) για αναπαράσταση ενός παίκτη.
    Οι υποκλάσεις ορίζουν is_human = True/False ανάλογα τον τύπο.
    """

    is_human = True  # Προεπιλογή: ανθρώπινος παίκτης

    def __init__(self, symbol):
        """
        Αρχικοποιεί τον παίκτη με το σύμβολό του.
        :param symbol: Το σύμβολο του παίκτη ('X' ή 'O')
        """
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
            enemy_symbol = "O"
            if self.symbol == "O":
                enemy_symbol = "X"

            # Δοκιμάζει αν με αυτή η κίνηση νικάει ο αντίπαλος
            if game.check_win(enemy_symbol, i):
                # Αν ο αντίπαλος παίξει εκεί τότε νικάει.
                # Άρα πρέπει να τον μπλοκάρει!
                return i

        # Δεν μπορεί ούτε να νικήσει ούτε χρειάζεται να μπλοκάρει, οπότε διαλέγει τυχαία
        return random.choice(empty_spaces)


if __name__ == "__main__":
    # Κώδικας για μεμονωμένη δοκιμή των παικτών
    print("Δοκιμή παικτών (Players Test)")

    game = Game(3)

    print("Δοκιμή RandomBot")
    bot = RandomBot("O")
    game._board = ["X", "O", "X", "O", "X", " ", "O", "X", " "]
    move = bot.get_move(game)
    print(f"Το bot διάλεξε τη θέση: {move}")

    print("Δοκιμή BetterBot - Άμυνα")
    # Ο Χρηστης ειναι το "Χ" έχεις δύο στη σειρά (0 και 1).
    # Το bot ΠΡΕΠΕΙ να παίξει στο 2 για να σε σταματήσει.
    bot = BetterBot("O")
    game._board = ["X", "X", " ", " ", "O", " ", " ", " ", " "]
    move = bot.get_move(game)
    print("Το ταμπλό έχει Χ στις θέσεις 0 και 1.")
    print(f"Το hard_bot επέλεξε τη θέση: {move}")
    if move == 2:
        print("ΕΠΙΤΥΧΙΑ!")
    else:
        print("ΑΠΟΤΥΧΙΑ!")

    print("Δοκιμή BetterBot - Επίθεση")
    # Το bot ειναι το "Ο" έχει δύο στη σειρά (3 και 4).
    # Το bot ΠΡΕΠΕΙ να παίξει στο 5 για να νικήσει.
    bot = BetterBot("O")
    game._board = ["X", "X", " ", "O", "O", " ", " ", " ", " "]
    move = bot.get_move(game)
    print("Το ταμπλό έχει Ο στις θέσεις 3 και 4.")
    print(f"Το hard_bot επέλεξε τη θέση: {move}")
    if move == 5:
        print("ΕΠΙΤΥΧΙΑ!")
    else:
        print("ΑΠΟΤΥΧΙΑ!")
