"""
Κύριο αρχείο εκκίνησης της εφαρμογής (Entry point).
Εδώ γίνεται η αρχικοποίηση του παιχνιδιού και της γραφικής διεπαφής.
"""
import tkinter as tk
from window import TicTacToeWindow
from game import Game
from player import HumanPlayer, RandomBot

# Συναρτήσεις για το GUI
def anoixe_to_gui(paixe_me_bot):
    # Φτιάχνω τη λογική και τον πρώτο παίκτη
    logic = Game()
    p1 = HumanPlayer(symbol='X')
    
    # Διαλέγω αν ο δεύτερος θα είναι άνθρωπος ή το bot
    if paixe_me_bot:
        p2 = RandomBot(symbol='O')
    else:
        p2 = HumanPlayer(symbol='O')
    
    #το παράθυρο που φτιάξαμε στο window.py
    app = TicTacToeWindow()
    app.start_game(logic, p1, p2)
    app.run()

#Συναρτήσεις για τα κουμπιά του μενού
def koumpi_pvp():
    # Κλείνω το μενού και ξεκινάω το παιχνίδι χωρίς bot
    root.destroy()
    anoixe_to_gui(False)

def koumpi_pve():
    # Κλείνω το μενού και ξεκινάω το παιχνίδι με bot
    root.destroy()
    anoixe_to_gui(True)

def koumpi_terminal():
    # Κλείνω το μενού και τρέχω την παλιά μου main
    root.destroy()
    main()

# Μενού επιλογής

def menu_epilogis():
    # global root μπορεί να το βλέπει τις συναρτήσεις από πάνω
    global root
    
    # Φτιάχνω ένα Παράθυρο
    root = tk.Tk()
    root.title("Επιλογή Mode")
    root.geometry("300x250")
    
    # Eτικέτα τίτλοu
    keimeno = tk.Label(root, text="Τι θέλεις να τρέξεις;", font=('Arial', 12))
    keimeno.pack(pady=15)
    
    # (Παίκτης vs Παίκτης)
    btn1 = tk.Button(root, text="Παράθυρο (PvP)", width=20, command=koumpi_pvp)
    btn1.pack(pady=5)
    
    # (Παίκτης vs Bot)
    btn2 = tk.Button(root, text="Παράθυρο (vs Bot)", width=20, command=koumpi_pve)
    btn2.pack(pady=5)
    
    # Κουμπί για το τερματικό
    btn3 = tk.Button(root, text="Τερματικό (Original)", width=20, command=koumpi_terminal)
    btn3.pack(pady=5)
    
    # Κρατάω το μενού ανοιχτό
    root.mainloop()

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
    bot2 = RandomBot("O")  # Παίκτης 2
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
    menu_epilogis()
