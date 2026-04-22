"""
Αρχείο που περιέχει την κλάση για τη γραφική διεπαφή του παιχνιδιού.
Χρησιμοποιεί τη βιβλιοθήκη tkinter.
"""

import tkinter as tk

from game import Game
from player import HumanPlayer, RandomBot, BetterBot, MinimaxBot


class TicTacToeWindow:
    """
    Κλάση που διαχειρίζεται το παράθυρο και τα γραφικά στοιχεία (widgets)
    του παιχνιδιού Τρίλιζα.
    """

    def __init__(self):
        """Αρχικοποιεί το βασικό παράθυρο και τις ιδιότητές του."""

        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("800x600")
        self.window.resizable(False, False)

        self.main_menu = True
        self.cells = []

        self.game = Game(3)

        self.main_menu_frame = self.create_main_menu_frame()
        self.game_board_frame = self.create_game_board_frame()
        self.select_view()

    def select_view(self):
        """Επιλέγει την ενεργή οθόνη του προγράμματος."""
        if self.main_menu:
            self.game_board_frame.pack_forget()
            self.main_menu_frame.pack(fill="both", expand=True)
        else:
            self.main_menu_frame.pack_forget()
            self.game_board_frame.pack(fill="both", expand=True)

    def create_main_menu_frame(self):
        """Δημιουργεί και επιστρέφει την οθόνη με το βασικό μενού του παιχνιδιού."""

        frame = tk.Frame(self.window)

        # Layout με 3 ζόνες. Τίτλος, Μενού, Έξοδος.
        # Ο τίτλος και η έξοδος θα έχουν σταθερό ύψος.
        # Το μενού θα επεκτείνεται να καλύψει όλον τον διαθέσιμο χώρο
        frame.rowconfigure(0, weight=0)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=0)

        frame.columnconfigure(0, weight=1)

        title = tk.Label(
            frame,
            text="Tic Tac Toe for PLHPRO",
            font=("Arial", 36),
        )
        title.grid(row=0, column=0, pady=20)

        center_area = tk.Frame(frame)
        center_area.grid(row=1, column=0)

        easy_btn = tk.Button(
            center_area,
            text="Easy",
            font=("Arial", 24),
            width=20,
            command=lambda: self.start_game("easy"),
        )
        medium_btn = tk.Button(
            center_area,
            text="Medium",
            font=("Arial", 24),
            width=20,
            command=lambda: self.start_game("medium"),
        )
        hard_btn = tk.Button(
            center_area,
            text="Hard",
            font=("Arial", 24),
            width=20,
            command=lambda: self.start_game("hard"),
        )

        easy_btn.pack(pady=10)
        medium_btn.pack(pady=10)
        hard_btn.pack(pady=10)

        exit_btn = tk.Button(
            frame,
            text="Exit",
            font=("Arial", 24),
            width=20,
            command=self.window.destroy,
        )
        exit_btn.grid(row=2, column=0, pady=20)

        return frame

    def create_game_board_frame(self):
        """Δημιουργεί και επιστρέφει την οθόνη με το ταμπλό του παιχνιδιού."""

        frame = tk.Frame(self.window)

        # Layout με δύο ζόνες. Ταμπλό, Μενού.
        # Το μενού είναι στο κάτω μέρος και έχει όλα τα κουμπιά στην σειρά.
        # Το ταμπλό θα είναι τετράγωνο και θα πιάνει όλο το χώρο που περισσεύει.

        # weight = 1 => γέμισε όσο περισσότερο χώρο μπορείς (και μικραίνεις/μεγαλώνεις αναλόγως)
        # weight = 0 => μην μεγαλώνεις και μην μικραίνεις
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=0)

        frame.columnconfigure(0, weight=1)

        # Ταμπλό
        self.board_frame = tk.Frame(frame, background="black", width=500, height=500)
        self.board_frame.grid_propagate(
            False
        )  # αγνoούμε το μέγεθος του περιεχομένου και κρατάμε σταθερό μέγεθος 500x500
        self.board_frame.grid(column=0, row=0, pady=20)

        # Αντι για 3x3, μεγαλώνω το grid για να βάλω και τις γραμμές της τρίλιζας ενδιάμεσα στα κελιά
        # Για κάθε γραμμή/στήλη ΚΑΙ ενδιάμεσα
        for i in range(3 * 2 - 1):
            if i % 2 == 0:  # στις ζυγές γραμμές και στήλες μπαίνουν τα κουμπιά
                self.board_frame.grid_rowconfigure(i, weight=1, uniform="cell")
                self.board_frame.grid_columnconfigure(i, weight=1, uniform="cell")
            else:  # οι μονές γραμμές και στήλες μένουν κενές, με μέγεθος 2 pixel, ώστε να φαίνεται το μαύρο background του περικλείοντος frame
                self.board_frame.grid_rowconfigure(i, weight=0, minsize=2)
                self.board_frame.grid_columnconfigure(i, weight=0, minsize=2)

        self.cells.clear()
        for i in range(9):
            x = i % 3
            y = i // 3
            btn = tk.Button(
                self.board_frame,
                text="",
                font=("Arial", 42),
                border=0,
                width=2,
                height=1,
                command=lambda x=x, y=y: self._on_cell_click(x, y),
            )
            btn.grid(row=2 * y, column=2 * x, sticky="nsew")
            self.cells.append(btn)

        menu_frame = tk.Frame(frame)
        menu_frame.grid(column=0, row=1, pady=20)

        self.overlay_message = tk.Label(
            self.board_frame,
            text="OVERLAY MESSAGE",
            font=("Arial", 48),
            fg="magenta",
            background=self.window["bg"],
        )

        # Τα κουμπιά για επανεκκίνηση του παιχνιδιού και έξοδο στο αρχικό μενού
        restart_button = tk.Button(
            menu_frame,
            text="Restart",
            font=("Arial", 14),
            width=12,
            command=self._on_restart,
        )

        quit_btn = tk.Button(
            menu_frame,
            text="Quit",
            font=("Arial", 14),
            width=12,
            command=self._on_quit_to_menu,
        )

        restart_button.grid(row=0, column=0, padx=10)
        quit_btn.grid(row=0, column=1, padx=10)

        return frame

    def update_cells(self):
        """
        Ενημερώνει όλα τα κελιά του ταμπλό ανάλογα με το game.get_board().
        """
        board = self.game.get_board()
        for i in range(self.game.board_size * self.game.board_size):
            self.cells[i]["text"] = board[i]

    def display_message(self, message, color):
        """Εμφανίζει ένα μήνυμα στον χρήστη."""

        self.overlay_message["fg"] = color
        self.overlay_message["text"] = message
        self.overlay_message.place(x=150, y=200)

    def start_game(self, enemy):
        """
        Συνδέει τη λογική του παιχνιδιού και τους παίκτες με το UI
        και ξεκινάει ή κάνει reset το παιχνίδι.
        """

        print("Game start!")
        # Για τώρα ο παίχτης 1 είναι πάντα άνθρωπος και έχει το Χ
        # Ήδη μπορούμε να βάλουμε 2 bot να παίξουν μεταξύ τους αν θέλουμε
        self._player1 = BetterBot("X")
        if enemy == "easy":
            self._player2 = RandomBot("O")
        elif enemy == "medium":
            self._player2 = BetterBot("O")
        elif enemy == "hard":
            self._player2 = MinimaxBot("O")
        else:
            print("Invalid option")

        self.enemy = enemy
        self.game.start(self._player1, self._player2)

        # Καθαρισμός UI για νέο παιχνίδι
        self.overlay_message.place_forget()
        self.update_cells()

        self.main_menu = False
        self.select_view()
        self._process_next_turn()

    def run(self):
        """Ξεκινάει τον κύριο βρόχο (main loop) της διεπαφής."""

        self.window.mainloop()

    # ── Βοηθητικές μέθοδοι (private helpers) ─────────────────────────────
    # Οι παρακάτω μέθοδοι δεν αποτελούν μέρος του δημόσιου API, αλλά
    # είτε χρειάζονται για τη σύνδεση των γεγονότων (events) με τη λογική,
    # είτε είναι βοηθητικές μέθοδοι για το παράθυρο.

    def _get_current_player(self):
        """Επιστρέφει το αντικείμενο Player που έχει σειρά, βάσει get_current_player()."""
        return self.game.get_current_player()

    def _on_cell_click(self, x, y):
        """
        Callback όταν ο χρήστης πατάει κελί.
        Αγνοεί κλικ αν δεν είναι σειρά ανθρώπινου παίκτη (is_human=True).
        """
        if self.game.game_over:
            return

        # Προσπάθησε να παίξεις την κίνηση που ζήτησε ο χρήστης.
        valid_move, player = self.game.play_turn(x + 3 * y)
        if not valid_move:
            print(f"Invalid move {x}, {y}. Try again.")
            # Άκυρη κίνηση οπότε δεν προχωράει το state του παιχνιδιού
            return

        # Αν φτάσουμε εδώ σημαίνει ότι η κίνηση ήταν έγκυρη, οπότε ενημερώνουμε το UI
        self.update_cells()

        print(f"Player played at {x}, {y}. Player symbol: {player.symbol}")

        if not self._check_game_over(player):
            print("Game is still on!")
            self._process_next_turn()
        else:
            print("You won!")

    def _process_next_turn(self):
        """
        Ελέγχει αν ο τρέχων παίκτης είναι bot (is_human=False).
        Αν ναι, εκτελεί αυτόματα την κίνησή του.
        Λειτουργεί για κάθε συνδυασμό παικτών (human/bot).
        """

        if not self._get_current_player().is_human:
            print("Bot's turn")
            self._do_bot_turn()
        else:
            print("Human's turn")

    def _do_bot_turn(self):
        """Εκτελεί μία κίνηση bot και μεταβαίνει στον επόμενο γύρο."""
        valid_move = False

        move = -1
        # Αμυντικός προγραμματισμός
        while not valid_move:
            move = self._get_current_player().get_move(self.game)
            valid_move, bot = self.game.play_turn(move)

        # Τα βάλαμε σε συνάρτηση για να μπορεί να κληθεί με το after.
        def make_bot_move():
            print(f"Bot played at {move // 3}, {move % 3}")
            print(f"Board after bot move: {self.game.get_board()}")
            self.update_cells()

            if not self._check_game_over(bot):
                print("Game is still on!")
                self._process_next_turn()

            else:
                print("Game over!")

        # 500ms καθυστέρηση για να φαίνεται οτί και καλά σκέφτεται το bot
        self.window.after(500, make_bot_move)

    def _check_game_over(self, player):
        """
        Ελέγχει νίκη / ισοπαλία μετά από κάθε κίνηση.
        Ενημερώνει σκορ και μήνυμα. Επιστρέφει True αν το παιχνίδι τελείωσε.
        """

        # Υποθέτουμε ότι τελείωσε
        self.game.game_over = True

        if self.game.check_win(self._player1.symbol):
            # Εμφάνιση you win
            self.display_message("You Won!", "green")
            return True
        elif self.game.check_win(self._player2.symbol):
            # Εμφάνιση you lose
            self.display_message("You Lost!", "red")
            return True
        elif self.game.check_draw():
            # Εμφάνιση draw
            self.display_message("Draw!", "blue")
            return True

        # Τελικά δεν τελείωσε
        self.game.game_over = False

        return False

    def _on_restart(self):
        """Callback για το κουμπί Επανεκκίνησης."""
        self.game.reset()
        self.start_game(self.enemy)

    def _on_quit_to_menu(self):
        """Callback για το κουμπί Quit κατα την διάρκεια του παιχνιδιού."""

        self.game.reset()
        self.main_menu = True
        self.select_view()


if __name__ == "__main__":
    # Κώδικας για μεμονωμένη δοκιμή του παραθύρου
    print("Δοκιμή παραθύρου (Window Test)")
    window = TicTacToeWindow()
    window.run()

    print("Run? And done?")
    pass
