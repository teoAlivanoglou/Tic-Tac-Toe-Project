"""
Αρχείο που περιέχει την κλάση για τη γραφική διεπαφή του παιχνιδιού.
Χρησιμοποιεί τη βιβλιοθήκη tkinter.
"""

import tkinter as tk


class TicTacToeWindow:
    """
    Κλάση που διαχειρίζεται το παράθυρο και τα γραφικά στοιχεία (widgets)
    του παιχνιδιού Τρίλιζα.
    """

    def __init__(self):
        """Αρχικοποιεί το βασικό παράθυρο και τις ιδιότητές του."""
        self.root = tk.Tk()
        self.root.title("TIC-TAC-TOE") # Τίτλος στο πάνω μέρος
        self.root.geometry("300x400")  # Το μέγεθος του παραθύρου
        self.buttons = []              # Λίστα για να αποθηκεύσουμε τα κουμπιά
        self.create_widgets()          # Καλούμε τη συνάρτηση που φτιάχνει τα γραφικά
 
    def create_widgets(self):
        """Δημιουργεί τα στοιχεία του παιχνιδιού με απλό τρόπο."""
        
        # Μια ετικέτα για να βλέπουμε ποιος παίζει
        self.label = tk.Label(self.root, text="Σειρά του παίκτη: X", font=('Arial', 14))
        self.label.pack(pady=10) # pack σημαίνει "βάλτο στο παράθυρο"

        # Ένα frame για να έχουμε τα κουμπιά μαζεμένα σε πλέγμα
        self.container = tk.Frame(self.root)
        self.container.pack()

        # Φτιάχνουμε μια λίστα 3x3 γεμάτη None στην αρχή
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        # Με δύο for φτιάχνουμε τα 9 κουμπιά της τρίλιζας
        for r in range(3):
            for c in range(3):
                # Δημιουργούμε το κουμπί
                self.buttons[r][c] = tk.Button(
                    self.container, 
                    text="", 
                    font=('Arial', 20), 
                    width=5, 
                    height=2, 
                    command=lambda row=r, col=c: self._on_cell_click(row, col)
                )
                # Το τοποθετούμε στο πλέγμα (grid)
                self.buttons[r][c].grid(row=r, column=c)

        # Κουμπί για να ξεκινάει το παιχνίδι από την αρχή
        self.reset_btn = tk.Button(self.root, text="Επανεκκίνηση", command=self._on_restart)
        self.reset_btn.pack(pady=20)

    def draw_board(self):
        """Σχεδιάζει / επαναφέρει το πλέγμα 3x3 (καθαρίζει κείμενα και ξανα-ενεργοποιεί κουμπιά)."""
        # Καθαρίζει τα κείμενα από όλα τα κουμπιά
        for row in self.buttons:
            for btn in row:
                btn.config(text="", state="normal")
        self.label.config(text="Σειρά του παίκτη: X")

    def bind_events(self):
        """Συνδέει τις ενέργειες (π.χ. κλικ) των χρηστών με τις αντίστοιχες λειτουργίες."""
        pass

    def update_cell(self, row, col, symbol):
        """
        Ενημερώνει ένα συγκεκριμένο κελί του ταμπλό με το σύμβολο του παίκτη.

        :param row: Η γραμμή της κίνησης (0-2)
        :param col: Η στήλη της κίνησης (0-2)
        :param symbol: Το σύμβολο ('X' ή 'O')
        """
        pass

    def display_message(self, message):
        """Εμφανίζει ένα μήνυμα στον χρήστη (π.χ. ποιος κέρδισε)."""
        pass

    def start_game(self, game_logic, player1, player2):
        """
        Συνδέει τη λογική του παιχνιδιού και τους παίκτες με το UI
        και ξεκινάει ή κάνει reset το παιχνίδι.
        """
        # Συνδέουμε τη λογική από το άλλο αρχείο με το παράθυρο
        self.game = game_logic
        self.draw_board()     
    def run(self):
        """Ξεκινάει τον κύριο βρόχο (main loop) της διεπαφής."""
       # Αυτό κρατάει το παράθυρο ανοιχτό
        self.root.mainloop()

    # ── Βοηθητικές μέθοδοι (private helpers) ─────────────────────────────
    # Οι παρακάτω μέθοδοι δεν αποτελούν μέρος του δημόσιου API, αλλά
    # χρειάζονται για τη σύνδεση των γεγονότων (events) με τη λογική.

    def _get_current_player_obj(self):
        """Επιστρέφει το αντικείμενο Player που έχει σειρά, βάσει get_current_player()."""
        pass

    def _on_cell_click(self, row, col):
        """
        Callback όταν ο χρήστης πατάει κελί.
        Αγνοεί κλικ αν δεν είναι σειρά ανθρώπινου παίκτη (is_human=True).
        """
        # 1. Ρωτάμε τη λογική ποιος παίζει (επιστρέφει "X" ή "O")
        symbol = self.game.get_current_player()
        
        # 2. Λέμε στη λογική να κάνει την κίνηση. Αν είναι έγκυρη (True):
        if self.game.make_move(row, col):
            # Γράφουμε το σύμβολο πάνω στο κουμπί που πατήθηκε
            self.buttons[row][col].config(text=symbol)
            
            # 3. Ελέγχουμε αν κέρδισε κάποιος
            winner = self.game.check_win()
            if winner:
                self.label.config(text=f"Νικητής ο παίκτης: {winner}!")
                self._disable_board() # Κλειδώνουμε τα κουμπιά
            # 4. Ελέγχουμε για ισοπαλία
            elif self.game.check_draw():
                self.label.config(text="Ισοπαλία!")
                self._disable_board()
            else:
                # Αν δεν τελείωσε, αλλάζουμε το κείμενο στην ετικέτα για τον επόμενο
                next_player = self.game.get_current_player()
                self.label.config(text=f"Σειρά του παίκτη: {next_player}")

    def _process_next_turn(self):
        """
        Ελέγχει αν ο τρέχων παίκτης είναι bot (is_human=False).
        Αν ναι, εκτελεί αυτόματα την κίνησή του.
        Λειτουργεί για κάθε συνδυασμό παικτών (human/bot).
        """
        pass

    def _do_bot_turn(self, bot):
        """Εκτελεί μία κίνηση bot και μεταβαίνει στον επόμενο γύρο."""
        pass

    def _check_game_over(self):
        """
        Ελέγχει νίκη / ισοπαλία μετά από κάθε κίνηση.
        Ενημερώνει σκορ και μήνυμα. Επιστρέφει True αν το παιχνίδι τελείωσε.
        """
        winner = self.game.check_win() 
        
        if winner: 
            if winner == "Draw":
                self.label.config(text="Ισοπαλία!")
            else:
                self.label.config(text=f"Νικητής ο παίκτης: {winner}!")
            
            self._disable_board() 
            return True
            
        return False

    def _disable_board(self):
        """Απενεργοποιεί όλα τα κουμπιά του ταμπλό στο τέλος του γύρου."""
        for row in self.buttons:
            for btn in row:
                btn.config(state="disabled")

    def _update_score_label(self):
        """Ενημερώνει την ετικέτα σκορ."""
        pass

    def _on_restart(self):
        """Callback για το κουμπί Επανεκκίνησης."""
        self.game.reset()
        self.draw_board()


if __name__ == "__main__":
    # Κώδικας για μεμονωμένη δοκιμή του παραθύρου
    print("Δοκιμή παραθύρου (Window Test)")
    
    from game import Game # Φέρνουμε την κλάση από το game.py
    
    logic = Game()
    app = TicTacToeWindow()
    app.start_game(logic, None, None)
    app.run()