"""
Αρχείο που περιέχει τις κλάσεις για τους παίκτες (Άνθρωπος, Υπολογιστής).
"""
import random

def winner(thesi,symbol): #Ε λεγχος Γραμμων,Στηλων,Διαγωνιο για Νικητη. (3χ3)
    if ((thesi[0] == symbol and thesi[1] == symbol and thesi[2] == symbol) or
       (thesi[3] == symbol and thesi[4] == symbol and thesi[5] == symbol) or
       (thesi[6] == symbol and thesi[7] == symbol and thesi[8] == symbol)):
        
        return True # Ελεγχος Γραμμων
    
    if ((thesi[0] == symbol and thesi[3] == symbol and thesi[6] == symbol) or
       (thesi[1] == symbol and thesi[4] == symbol and thesi[7] == symbol) or
       (thesi[2] == symbol and thesi[5] == symbol and thesi[8] == symbol)):

       return True #Ελεγχος Στηλων

    if ((thesi[0] == symbol and thesi[4] == symbol and thesi[8] == symbol) or
       (thesi[6] == symbol and thesi[4] == symbol and thesi[2] == symbol)):
       
       return True # Διαγωνιος

    return False

class Player:
    """
    Βασική κλάση (Base Class) για αναπαράσταση ενός παίκτη.
    Οι υποκλάσεις ορίζουν is_human = True/False ανάλογα τον τύπο.
    """

    is_human = True  # Προεπιλογή: ανθρώπινος παίκτης

    def __init__(self, symbol):
    
        self.symbol = symbol

    def get_move(self, board, position=None):
        return position # Επιστρέφει το index (0-8) που θα πάτησει ο άνθρωπος

class Bot(Player):
    """
    Βασική κλάση (Base Class) για αναπαράσταση ενός bot.
    """

    is_human = False

    def check_win(self, board, symbol):

        if (
            (board[0] == board[1] == board[2] == symbol)
            or (board[3] == board[4] == board[5] == symbol)
            or (board[6] == board[7] == board[8] == symbol)
        ):
            return True  # Ελεγχος Γραμμων

        if (
            (board[0] == board[3] == board[6] == symbol)
            or (board[1] == board[4] == board[7] == symbol)
            or (board[2] == board[5] == board[8] == symbol)
        ):
            return True  # Ελεγχος Στηλων

        if (board[0] == board[4] == board[8] == symbol) or (
            board[6] == board[4] == board[2] == symbol
        ):
            return True  # Διαγωνιος

        return False

    def get_empty_spaces(self, board):
        empty_spaces = []  # κενή λίστα που θα αποθηκεύσω τις ελεύθερες θέσεις
        for i in range(9):
            if board[i] == " ":
                empty_spaces.append(i)
        return empty_spaces


class HumanPlayer(Player):
   
    is_human = True

    def get_move(self, board):
        pass

    def __init__(self, symbol):
        self.symbol = symbol

class RandomBot(Bot):
    is_human = False  # Αυτοματοποιημένος παίκτης

    def get_move(self, board):
        matrix = list(board)

        for i in range(9): #ΕΠΙΘΕΣΗ
            if matrix[i] == " ":
               matrix[i] = self.symbol #(1)επιλεγει κινηση και στην κατω if ελεγχει αν κερδιζει με την κινηση αυτη
               if winner(matrix,self.symbol): #ελεγχει αν νικησε η οχι
                   return i #η τιμη αυτη επιστρεφεται μονο αν νικησει
               matrix[i] = " " #σβηνει γιατι πρεπει να επαναφερει το ταμπλο στην αρχικη καταστσαη
            
        opponent = "X" if self.symbol == "O" else "O"   

        for i in range(9):#ΑΜΥΝΑ
            if matrix[i] == " ":
               matrix[i] = opponent #Δοκιμαζει κινηση ωστε να δεις αν θα χρειαστει να αμυνθει
               if winner(matrix, opponent):
                   return i 
               matrix[i] = " " #στην συνεχει την αδειαζει την θεση ωστε να ξανα κανει ελεγχο μετα 

        free_choice = self.get_empty_spaces(board) #Τυχαία κίνηση
        if free_choice:
            return random.choice(free_choice)
        return None

if __name__ == "__main__":
    # Κώδικας για μεμονωμένη δοκιμή των παικτών
    print("Δοκιμή παικτών (Players Test)")

    # Δημιουργούμε ένα Bot που παίζει με το "O"
    bot = RandomBot("O")

    # ΤΕΣΤ 1: Επίθεση (Το bot πρέπει να κερδίσει)
    # Το "O" έχει τα 3 και 4. Πρέπει να παίξει στο 5.
    board_attack = ["X", "X", " ", 
                    "O", "O", " ", 
                    " ", " ", " "]
    print("\nΤεστ 1 - Επίθεση:")
    move = bot.get_move(board_attack)
    print(f"Το ταμπλό έχει 'O' στα 3,4. Το bot έπαιξε στο: {move}")
    if move == 5:
        print("ΕΠΙΤΥΧΙΑ: Το Bot νίκησε!")
    else: 
        print("ΑΠΟΤΥΧΙΑ: Το Bot έχασε την ευκαιρία.")

    # ΤΕΣΤ 2: Άμυνα (Το bot πρέπει να μπλοκάρει τον παίκτη)
    # Ο παίκτης "X" έχει τα 0 και 1. Το bot πρέπει να παίξει στο 2.
    board_defense = ["X", "X", " ", 
                     " ", "O", " ", 
                     " ", " ", " "]
    print("\nΤεστ 2 - Άμυνα:")
    move = bot.get_move(board_defense)
    print(f"Το ταμπλό έχει 'X' στα 0,1. Το bot έπαιξε στο: {move}")
    if move == 2: 
        print("ΕΠΙΤΥΧΙΑ: Το Bot σε μπλόκαρε!")
    else: 
        print("ΑΠΟΤΥΧΙΑ: Το Bot σε άφησε να κερδίσεις.")

    # ΤΕΣΤ 3: Τυχαία κίνηση
    # Όλα κενά εκτός από ένα.
    board_random = ["X", " ", " ", 
                    " ", " ", " ", 
                    " ", " ", " "]
    print("\nΤεστ 3 - Τυχαία κίνηση:")
    move = bot.get_move(board_random)
    if move is not None and board_random[move] == " ":
        print(f"ΕΠΙΤΥΧΙΑ: Το Bot διάλεξε την έγκυρη θέση {move}")