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
        """
        Αρχικοποιεί τον παίκτη με το σύμβολό του.

        :param symbol: Το σύμβολο του παίκτη ('X' ή 'O')
        """
        pass

    def get_move(self, board):
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

    def get_move(self, board):
        """Επιστρέφει την κίνηση που επέλεξε ο χρήστης μέσω του UI."""
        pass


class RandomBot(Player):
    is_human = False  # Αυτοματοποιημένος παίκτης

    def get_move(self, board):
        matrix = list(board)

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
    pass
