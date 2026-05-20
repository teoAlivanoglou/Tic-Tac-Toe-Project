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
        self._board = [" "] * self.board_size**2
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
        :return: Πλειάδα (result, player) result η εγκυρότητα της κίνησης, player ο παίκτης που έπαιξε
        """
        current_player = self.get_current_player()
        if self._board[index] == " ":
            self._board[index] = current_player.symbol
            self.next_player() # Μετά από κάθε έγκυρη κίνηση, αλλάζει η σειρά
            return True, current_player
        return False, None

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
            return True  # Διαγώνιοι

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
        self.game_over = False

# --- Τμήμα Ελέγχου & Δοκιμών (Main) ---
# Ο κώδικας αυτός τρέχει μόνο αν εκτελεστεί το αρχείο απευθείας.
# Χρησιμοποιήθηκε για τη λήψη screenshots στην ομαδική έκθεση.
if __name__ == "__main__":
    # Βοηθητική κλάση για τη δοκιμή
    class MockPlayer:
        def __init__(self, name, symbol):
            self.name = name
            self.symbol = symbol

    def print_current_board(game):
        b = game.get_board()
        print(f" {b[0]} | {b[1]} | {b[2]} ")
        print("---+---+---")
        print(f" {b[3]} | {b[4]} | {b[5]} ")
        print("---+---+---")
        print(f" {b[6]} | {b[7]} | {b[8]} ")
        print()

    p1 = MockPlayer("Player1", "X")
    p2 = MockPlayer("Player2", "O")
    game = Game(3)

    print("-" * 40)
    print(" TEST 1: Έλεγχος Νίκης (Οριζόντια)")
    print("-" * 40)
    game.start(p1, p2)
    # Προσομοίωση κινήσεων: Ο Χ κερδίζει στην πρώτη σειρά
    for move in [0, 3, 1, 4, 2]: 
        game.play_turn(move)
    print_current_board(game)
    if game.check_win("X"):
        print(" Αποτέλεσμα: Το σύστημα αναγνώρισε τη ΝΙΚΗ του X!")

    print("\n" + "-" * 40)
    print("TEST 2: Έλεγχος Ισοπαλίας")
    print("-" * 40)
    game.reset()
    game.start(p1, p2)
    # Σενάριο κινήσεων για πλήρες ταμπλό χωρίς νικητή
    for move in [0, 1, 2, 4, 3, 5, 7, 6, 8]:
        game.play_turn(move)
    print_current_board(game)
    if game.check_draw():
        print(" Αποτέλεσμα: Το σύστημα αναγνώρισε την ΙΣΟΠΑΛΙΑ!")

    print("\n" + "-" * 40)
    print(" TEST 3: Έλεγχος Παράνομης Κίνησης")
    print("-" * 40)
    game.reset()
    game.start(p1, p2)
    game.play_turn(4) # Παίζει ο Π1 στο κέντρο
    print("Ο Player1 έπαιξε στο κέντρο (4).")
    success, _ = game.play_turn(4) # Πάει ο Π2 να παίξει στο ίδιο
    if not success:
        print(" Αποτέλεσμα: Η κίνηση απορρίφθηκε σωστά!")
    print("-" * 40)