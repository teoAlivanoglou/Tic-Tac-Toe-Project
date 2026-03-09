"""
Αρχείο που διαχειρίζεται τη λογική του παιχνιδιού και την κατάσταση του ταμπλό.
"""

from copy import copy


class Game:
    """
    Κλάση που περιέχει τη λογική, ελέγχει τους κανόνες, τις νίκες, τις ήττες
    και τη διαχείριση γύρων.
    """

    def __init__(self, board_size):
        """Αρχικοποιεί το ταμπλό, τους παίκτες και τις μεταβλητές του παιχνιδιού."""
        self.board_size = board_size
        self.reset()

    def start(self, player1, player2):
        """Αρχίζει ένα νέο παιχνίδι με τους δύο παίκτες που δίνονται ως παράμετροι."""
        self._player1 = player1
        self._player2 = player2
        self._current_player = player1

    def play_turn(self, index):
        """
        Εκτελεί το γύρο ενός παίκτη στη δεδομένη θέση.

        :param index: Η θέση της κίνησης
        :return: True αν η κίνηση ήταν έγκυρη, False αλλιώς
        """
        current_player = self.get_current_player()
        if self._board[index] == " ":
            self._board[index] = current_player.symbol
            # Σωστή κίνηση οπότε προχωράει η σειρά
            self.next_player()
            return True
        return False

    def get_board(self):
        """
        Επιστρέφει αντίγραφο της δομής δεδομένων που αναπαριστά το ταμπλό.
        Για μετάλλαξη του ταμπλό πρέπει να κλειθεί η play_turn.
        """
        return copy(self._board)

    def get_board_size(self):
        """
        Επιστρέφει το μεγεθος του ταμπλο
        """
        return self.board_size

    def get_empty_spaces(self):
        """Βρίσκει τις κενές θέσεις στο ταμπλό και επιστρέφει μία λίστα με αυτές"""
        empty_spaces = []  # κενή λίστα που θα αποθηκεύσω τις ελεύθερες θέσεις
        for i in range(self.board_size**2):
            if self._board[i] == " ":
                empty_spaces.append(i)
        return empty_spaces

    def get_current_player(self):
        """
        Επιστρέφει το σύμβολο του παίκτη που έχει σειρά να παίξει.
        """
        return self._current_player

    def next_player(self):
        """Αλλάζει τον τρέχοντα παίκτη σε σειρά."""
        if self._current_player == self._player1:
            self._current_player = self._player2
        else:
            self._current_player = self._player1

    def check_win(self, player_symbol, temp_play_index=None):
        """Ελέγχει αν υπάρχει τριάδα (οριζόντια, κάθετα, διαγώνια) με το σύμβολο του παίκτη

        :param player_symbol: Το σύμβολο του παίκτη
        :temp_play_index: Προερετική παράμετρος που ελέγχει το αποτέλεσμα αν νικάει ο player_symbol σε περίπτωση που παίξει στην θέση temp_play_idex
        """

        board = self.get_board()
        if temp_play_index is not None:
            board[temp_play_index] = player_symbol

        # TODO: να το κάνω με loop ώστε να μπορεί να ελέγξει και άλλα μεγέθη ταμπλό

        if (
            (board[0] == board[1] == board[2] == player_symbol)
            or (board[3] == board[4] == board[5] == player_symbol)
            or (board[6] == board[7] == board[8] == player_symbol)
        ):
            return True  # Γραμμές

        if (
            (board[0] == board[3] == board[6] == player_symbol)
            or (board[1] == board[4] == board[7] == player_symbol)
            or (board[2] == board[5] == board[8] == player_symbol)
        ):
            return True  # Στήλες

        if (board[0] == board[4] == board[8] == player_symbol) or (
            board[6] == board[4] == board[2] == player_symbol
        ):
            return True  # Διαγώνιος

        return False

    def check_draw(self):
        """Ελέγχει αν το ταμπλό γέμισε χωρίς να υπάρξει νικητής."""
        if " " not in self._board:
            # ελεγχει αν υπαρχει εστω και ενα αδειο ωστε να δει αν ολο το ταμπλο γεμησε
            return True
        else:
            return False

    def reset(self):
        """Καθαρίζει το ταμπλό και επαναφέρει το παιχνίδι στην αρχική του κατάσταση."""
        self._board = [" "] * self.board_size**2
        self._player1 = None
        self._player2 = None
        self._current_player = None


if __name__ == "__main__":
    # Κώδικας για μεμονωμένη δοκιμή της λογικής του παιχνιδιού
    print("Δοκιμή λογικής παιχνιδιού (Game Logic Test)")
    pass
