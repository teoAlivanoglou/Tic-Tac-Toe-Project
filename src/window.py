"""
Αρχείο που περιέχει την κλάση για τη γραφική διεπαφή του παιχνιδιού.
Χρησιμοποιεί τη βιβλιοθήκη tkinter.
"""

import tkinter as tk
from game import Game
from player import HumanPlayer, RandomBot, BetterBot, MinimaxBot
import config

import pyglet
import os, sys


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

        # https://stackoverflow.com/a/1297407
        dir_name = os.path.dirname(os.path.abspath(__file__))
        # print(dir_name)
        font_path = os.path.join(dir_name, "..", "fonts", config.FONT_PATH)
        # print(font_path)

        # https://stackoverflow.com/a/76001345
        # https://stackoverflow.com/a/61353191
        # https://stackoverflow.com/a/1325587
        if os.name == "nt":
            pyglet.options["win32_gdi_font"] = True
        pyglet.font.add_file(font_path)

        # fonts = tkfont.families()
        # from pprint import pprint
        # pprint(fonts)
        # quit()

        self.main_menu = True
        self.cells = []

        self.game = Game(3)

        self.main_menu_frame = self.create_main_menu_frame()
        self.game_board_frame = self.create_game_board_frame()

        # https://www.reddit.com/r/learnpython/comments/1629dlo/comment/jxwaqcn/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
        self.after_id = None

        # https://stackoverflow.com/a/34373558
        self.window.update_idletasks()
        self.overlay_message = tk.Label(
            self.window,
            text="OVERLAY MESSAGE",
            font=(config.FONT_NAME, 48),
            fg="magenta",
            wraplength=self.window.winfo_width() - 50,
            justify="center",
            background=self.window["bg"],
        )

        self.select_view()

    def select_view(self):
        """Επιλέγει την ενεργή οθόνη του προγράμματος."""

        self.overlay_message.place_forget()

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
            font=(config.FONT_NAME, 48),
        )
        title.grid(row=0, column=0, pady=20, columnspan=2)

        center_area = tk.Frame(frame)
        center_area.grid(row=1, column=0, columnspan=2)

        self.selected_p1 = "Human"
        self.selected_p2 = "Unbeatable"

        self.p1_buttons = []
        self.p2_buttons = []

        options = ["Human", "Easy", "Hard", "Unbeatable"]

        def style_buttons(button_list, selected):
            """Αλλάζει το στυλ των κουμπιων ανάλογα με το αν είναι επιλεγμένο ή όχι."""
            for button in button_list:
                if button["text"] == selected:
                    button.config(relief="sunken", bg="dodgerblue", fg="white")
                else:
                    button.config(relief="raised", bg="lightgray", fg="black")

        def select_p1(choice):
            self.selected_p1 = choice
            style_buttons(self.p1_buttons, choice)

        def select_p2(choice):
            self.selected_p2 = choice
            style_buttons(self.p2_buttons, choice)

        p1_label = tk.Label(
            center_area,
            text=f"Player 1 ({config.SYMBOL_X})",
            font=(config.FONT_NAME, 18),
        )
        p1_label.pack(pady=(10, 5))

        p1_row = tk.Frame(center_area)
        p1_row.pack(pady=5)

        for option in options:
            btn = self._make_button(
                p1_row,
                text=option,
                # font=("Arial", 16),
                # width=15,
                command=lambda v=option: select_p1(v),
            )
            btn.pack(side="left", padx=5)
            self.p1_buttons.append(btn)

        p2_label = tk.Label(
            center_area,
            text=f"Player 2 ({config.SYMBOL_O})",
            font=(config.FONT_NAME, 18),
        )
        p2_label.pack(pady=(10, 5))

        p2_row = tk.Frame(center_area)
        p2_row.pack(pady=5)

        for option in options:
            btn = self._make_button(
                p2_row,
                text=option,
                # font=("Arial", 16),
                # width=15,
                command=lambda v=option: select_p2(v),
            )
            btn.pack(side="left", padx=5)
            self.p2_buttons.append(btn)

        style_buttons(self.p1_buttons, self.selected_p1)
        style_buttons(self.p2_buttons, self.selected_p2)

        menu_frame = tk.Frame(frame)
        menu_frame.grid(row=2, column=0, columnspan=2, pady=20)

        start_btn = self._make_button(
            menu_frame,
            text="Start",
            command=lambda: self.start_game(self.selected_p1, self.selected_p2),
        )

        exit_btn = self._make_button(
            menu_frame,
            text="Exit",
            command=self.window.destroy,
        )

        start_btn.grid(row=0, column=0, padx=10)
        exit_btn.grid(row=0, column=1, padx=10)

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
            btn = self._make_button(
                self.board_frame,
                text=" ",
                font=(config.FONT_NAME, 42),
                bg="SystemButtonFace",
                command=lambda x=x, y=y: self._on_cell_click(x, y),
            )
            btn.grid(row=2 * y, column=2 * x, sticky="nsew")
            self.cells.append(btn)

        menu_frame = tk.Frame(frame)
        menu_frame.grid(column=0, row=1, pady=20)

        # Τα κουμπιά για επανεκκίνηση του παιχνιδιού και έξοδο στο αρχικό μενού
        restart_button = self._make_button(
            menu_frame,
            text="Restart",
            command=self._on_restart,
        )

        quit_btn = self._make_button(
            menu_frame,
            text="Quit",
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
        self.overlay_message.place(rely=0.5, relx=0.5, anchor="center")

    def start_game(self, player1, player2):
        """
        Συνδέει τη λογική του παιχνιδιού και τους παίκτες με το UI
        και ξεκινάει ή κάνει reset το παιχνίδι.
        """

        print("Game start!")
        # Για τώρα ο παίχτης 1 είναι πάντα άνθρωπος και έχει το Χ
        # Ήδη μπορούμε να βάλουμε 2 bot να παίξουν μεταξύ τους αν θέλουμε
        # Ελπίζω τα σύμβολα να φαίνονται κανονικά...
        if player1 == "Human":
            self._player1 = HumanPlayer("Παίχτης 1", config.SYMBOL_X)
        elif player1 == "Easy":
            self._player1 = RandomBot("Random Bot 1", config.SYMBOL_X)
        elif player1 == "Hard":
            self._player1 = BetterBot("Better Bot 1", config.SYMBOL_X)
        elif player1 == "Unbeatable":
            self._player1 = MinimaxBot("Unbeatable Bot 1", config.SYMBOL_X)
        else:
            print("Invalid option")

        if player2 == "Human":
            self._player2 = HumanPlayer("Παίχτης 2", config.SYMBOL_O)
        elif player2 == "Easy":
            self._player2 = RandomBot("Random Bot 2", config.SYMBOL_O)
        elif player2 == "Hard":
            self._player2 = BetterBot("Better Bot 2", config.SYMBOL_O)
        elif player2 == "Unbeatable":
            self._player2 = MinimaxBot("Unbeatable Bot 2", config.SYMBOL_O)
        else:
            print("Invalid option")

        self.game.start(self._player1, self._player2)

        # Καθαρισμός UI για νέο παιχνίδι
        self.update_cells()
        self.main_menu = False
        self.select_view()

        # Έναρξη του πρώτου γύρου του παιχνιδιού
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

        print(f"Player played at {x}, {y}.")

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
            self._disable_cells()
            print("Bot's turn")
            self._do_bot_turn()
        else:
            self._enable_cells()
            print("Human's turn")

    def _disable_cells(self):
        """Απενεργοποιεί όλα τα κελιά του ταμπλό."""
        for cell in self.cells:
            cell.config(state="disabled")

    def _enable_cells(self):
        """Ενεργοποιεί όλα τα κελιά του ταμπλό."""
        for cell in self.cells:
            cell.config(state="normal")

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
            self.update_cells()

            if not self._check_game_over(bot):
                print("Game is still on!")
                self._process_next_turn()

            else:
                print("Game over!")

        # 500ms καθυστέρηση για να φαίνεται οτί και καλά σκέφτεται το bot
        self.after_id = self.window.after(500, make_bot_move)

    def _check_game_over(self, player):
        """
        Ελέγχει νίκη / ισοπαλία μετά από κάθε κίνηση.
        Ενημερώνει σκορ και μήνυμα. Επιστρέφει True αν το παιχνίδι τελείωσε.
        """

        # Υποθέτουμε ότι τελείωσε
        self.game.game_over = True

        humans = sum(1 for p in (self._player1, self._player2) if p.is_human)

        if self.game.check_win(player.symbol):
            if humans == 1:  # Human vs Bot
                if player.is_human:
                    self.display_message(f"Ο {player.name} νίκησε!", "green")
                else:
                    self.display_message("Ωχ όχι. Έχασες.", "red")
            elif humans == 2:  # Human vs Human
                self.display_message(
                    f"Ο {player.name} ({player.symbol}) νίκησε!", "green"
                )
            else:  # Bot vs Bot
                self.display_message(
                    f"Το {player.name} ({player.symbol}) κέρδισε!", "green"
                )

            return True

        elif self.game.check_draw():
            self.display_message("Ισοπαλία!", "blue")
            return True

        # Τελικά δεν τελείωσε
        self.game.game_over = False

        return False

    def _on_restart(self):
        """Callback για το κουμπί Επανεκκίνησης."""
        self.game.reset()
        if self.after_id is not None:
            self.window.after_cancel(self.after_id)
            self.after_id = None
        self.start_game(self.selected_p1, self.selected_p2)

    def _on_quit_to_menu(self):
        """Callback για το κουμπί Quit κατα την διάρκεια του παιχνιδιού."""

        self.game.reset()
        if self.after_id is not None:
            self.window.after_cancel(self.after_id)
            self.after_id = None
        self.main_menu = True
        self.select_view()

    def _make_button(self, parent, **kwargs):
        """
        Βοηθητική συνάρτηση που φτιάχνει ένα button με ορισμένες προεπιλογές
        https://blacknerd.dev/day-27-tkinter-args-kwargs-creating-guis
        """

        font_size = kwargs.pop("font_size", 12)
        font = kwargs.pop("font", (config.FONT_NAME, font_size))
        width = kwargs.pop("width", 15)
        height = kwargs.pop("height", 1)
        bg = kwargs.pop("bg", "lightgray")
        fg = kwargs.pop("fg", "black")
        border = kwargs.pop("border", 0)
        relief = kwargs.pop("relief", "raised")
        activebackground = kwargs.pop("activebackground", "dodgerblue")
        activeforeground = kwargs.pop("activeforeground", "white")

        return tk.Button(
            parent,
            font=font,
            width=width,
            height=height,
            bg=bg,
            fg=fg,
            border=border,
            relief=relief,
            activebackground=activebackground,
            activeforeground=activeforeground,
            disabledforeground=fg,
            **kwargs,
        )


if __name__ == "__main__":
    # Κώδικας για μεμονωμένη δοκιμή του παραθύρου
    print("Δοκιμή παραθύρου (Window Test)")
    pass
