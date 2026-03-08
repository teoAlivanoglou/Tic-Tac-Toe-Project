"""
Αρχείο που διαχειρίζεται τη λογική του παιχνιδιού και την κατάσταση του ταμπλό.
"""
class Game:

    def __init__(self):
        
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def play_turn(self, row, col):
        """
        Εκτελεί το γύρο ενός παίκτη στη δεδομένη θέση.

        :param row: Η γραμμή της κίνησης
        :param col: Η στήλη της κίνησης
        :return: True αν η κίνηση ήταν έγκυρη, False αλλιώς
        """
        pass

    def get_board(self):
        return self.board

    def get_current_player(self):
        return self.get_current_symbol  # θα επιστρεφει Χ η Ο αναλογα ποιος παιζει που την παιρνει απο το αρχειο player.py

    def check_win(self):
        """Ελέγχει αν υπάρχει τριάδα (οριζόντια, κάθετα, διαγώνια) για κάποιον παίκτη."""
        pass

    def check_draw(self):
        if " " not in self.board #ελεγχει αν υπαρχει εστω και ενα αδειο ωστε να δει αν ολο το ταμπλο γεμησε
            return True
        else:
            return False
    
    def reset(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " ",] # Αδειαζουμε τον board ωστε να ξεκινησει απο την αρχη με κενες θεσεις


if __name__ == "__main__":
    # Κώδικας για μεμονωμένη δοκιμή της λογικής του παιχνιδιού
    print("Δοκιμή λογικής παιχνιδιού (Game Logic Test)")
    pass
