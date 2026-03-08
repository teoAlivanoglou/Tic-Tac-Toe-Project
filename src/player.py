"""
Αρχείο που περιέχει τις κλάσεις για τους παίκτες (Άνθρωπος, Υπολογιστής).
"""
import random

<<<<<<< HEAD
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
=======
import random

>>>>>>> origin/teo

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

    def get_move(self, board):
        """
        Υπολογίζει και επιστρέφει την επόμενη κίνηση του παίκτη.
        Πρέπει να υλοποιηθεί από τις υποκλάσεις.
        """
        pass


class Bot(Player):
    """
    Βασική κλάση (Base Class) για αναπαράσταση ενός bot.
    """

    is_human = False

    def check_win(self, board, symbol):
        """Ελέγχει αν υπάρχει τριάδα (οριζόντια, κάθετα, διαγώνια) για κάποιον παίκτη."""

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
        """Βρίσκει τις κενές θέσεις στο ταμπλό και επιστρέφει μία λίστα με αυτές"""
        empty_spaces = []  # κενή λίστα που θα αποθηκεύσω τις ελεύθερες θέσεις
        for i in range(9):
            if board[i] == " ":
                empty_spaces.append(i)
        return empty_spaces


class HumanPlayer(Player):
    """
    Κλάση που αναπαριστά έναν ανθρώπινο παίκτη.
    """

    is_human = True

    def get_move(self, board):
        """Επιστρέφει την κίνηση που επέλεξε ο χρήστης μέσω του UI."""
        pass


<<<<<<< HEAD
class RandomBot(Player):
    is_human = False  # Αυτοματοποιημένος παίκτης

    def get_move(self, board):
        matrix = list(board)
=======
class RandomBot(Bot):
    """
    Κλάση που αναπαριστά έναν αυτοματοποιημένο παίκτη (Bot),
    ο οποίος επιλέγει κινήσεις εντελώς τυχαία.
    """

    def get_move(self, board):
        """Βρίσκει κενές θέσεις στο ταμπλό και επιλέγει μία τυχαία."""

        empty_spaces = self.get_empty_spaces(board)
        return random.choice(empty_spaces)


class BetterBot(Bot):
    """
    Κλάση που αναπαριστά έναν αυτοματοποιημένο παίκτη (Bot),
    ο οποίος επιλέγει κινήσεις πιο μεθοδικά.
    """

    def get_move(self, board):
        """Βρίσκει κενές θέσεις στο ταμπλό και επιλέγει μία μεθοδικά."""

        empty_spaces = self.get_empty_spaces(board)

        # Επίθεση
        for i in empty_spaces:
            # Δοκιμάζει αν αυτή η κίνηση νικάει
            board[i] = self.symbol
            if self.check_win(board, self.symbol):
                # Νικάει άρα "παίζει" εκεί
                return i

            # Αν δεν νικάει, επαναφέρει το ταμπλό
            board[i] = " "

        # Άμυνα
        for i in empty_spaces:
            # Βρίσκουμε το σύμβολο του αντπάλου
            enemy_symbol = "O"
            if self.symbol == "O":
                enemy_symbol = "X"

            # Δοκιμάζει αν με αυτή η κίνηση νικάει ο αντίπαλος
            board[i] = enemy_symbol
            if self.check_win(board, enemy_symbol):
                # Αν ο αντίπαλος παίξει εκεί τότε νικάει.
                # Άρα πρέπει να τον μπλοκάρει!
                board[i] = self.symbol
                return i

            # Αν δεν χρειάζεται να μπλοκάρει, επαναφέρει το ταμπλό
            board[i] = " "

        # Δεν μπορεί ούτε να νικήσει ούτε χρειάζεται να μπλοκάρει, οπότε διαλέγει τυχαία
        return random.choice(empty_spaces)
>>>>>>> origin/teo

        for i in range(9): #ΕΠΙΘΕΣΗ
            if matrix[i] == " ":
               matrix[i] = "O" #(1)επιλεγει κινηση και στην κατω if ελεγχει αν κερδιζει με την κινηση αυτη
               if winner(matrix, "O"): #ελεγχει αν νικησε η οχι
                   return i #η τιμη αυτη επιστρεφεται μονο αν νικησει
               matrix[i] = " " #σβηνω το "Ο" μην γεμησει το επομενο κενο καθως το συμπληρωσε στο (1)
            
        opponent = "X" if self.symbol == "O" else "O"   

        for i in range(9):#ΑΜΥΝΑ
            if matrix[i] == " ":
               matrix[i] = "X" #Δοκιμαζει κινηση ωστε να δεις αν θα χρειαστει να αμυνθει
               if winner(matrix, opponent):
                   matrix[i] = " " #Αδιαζει την θεση που γεμισε ωστε να την συμπληρωσει το ΒΟΤ
                   return i 
               matrix[i] = " " #στην συνεχει την αδειαζει την θεση ωστε να ξανα κανει ελεγχο μετα 

        free_choice = []
        for i in range(9):
            if matrix[i] == " ":
                free_choice.append(i)

        if free_choice:
            return random.choice(free_choice)
        return None

if __name__ == "__main__":
    # Κώδικας για μεμονωμένη δοκιμή των παικτών
    print("Δοκιμή παικτών (Players Test)")

    print("Δοκιμή RandomBot")
    bot = RandomBot("O")
    board = ["X", "O", "X", "O", "X", " ", "O", "X", " "]
    move = bot.get_move(board)
    print(f"Το bot διάλεξε τη θέση: {move}")

    print("Δοκιμή BetterBot - Άμυνα")
    # Ο Χρηστης ειναι το "Χ" έχεις δύο στη σειρά (0 και 1).
    # Το bot ΠΡΕΠΕΙ να παίξει στο 2 για να σε σταματήσει.
    bot = BetterBot("O")
    board = ["X", "X", " ", " ", "O", " ", " ", " ", " "]
    move = bot.get_move(board)
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
    board = ["X", "X", " ", "O", "O", " ", " ", " ", " "]
    move = bot.get_move(board)
    print("Το ταμπλό έχει Ο στις θέσεις 3 και 4.")
    print(f"Το hard_bot επέλεξε τη θέση: {move}")
    if move == 5:
        print("ΕΠΙΤΥΧΙΑ!")
    else:
        print("ΑΠΟΤΥΧΙΑ!")
