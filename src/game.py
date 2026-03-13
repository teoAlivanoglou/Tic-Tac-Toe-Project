"""
Αρχείο που διαχειρίζεται τη λογική του παιχνιδιού και την κατάσταση του ταμπλό.
"""
class Game:

    def __init__(self):
        
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.current_player = "X" # υποθετουμε οτι ξεκιναμε με χ

    def play_turn(self, row, col):
        
        thesi = row * 3 + col
        
        if self.board[thesi] != " ":
            return False
        
        self.board[thesi] = self.current_player

        if self.current_player == "X": # παιζει ο παικτης 1, υποθετουμε οτι ειναι χ
           self.current_player = "O"  # ο αλλος παικτης  τωρα παιζει που ειναι ο O
        else:
           self.current_player = "X"   # σε περιπτωση που το παραπανω ειναι αντιθετο. 

        return True

    def get_board(self):
        return self.board

    def get_current_player(self):
        return self.current_player  # θα επιστρεφει Χ η Ο αναλογα ποιος παιζει που την παιρνει απο το αρχειο player.py

    def check_win(self):
        numbers = [] #φτιανω λιστα 
        for i in self.board:
            if i == "X":
                numbers.append(1) #οπου βρει χ βαζει στην λιστα το 1
            elif i == "O":
                numbers.append(-1) #οπου βρει y βαζει στην λιστα το -1
            else:
                numbers.append(0) #οπου δεν βρει κατι  βαζει στην λιστα το 0 δηλαδη κενο
        triades = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Οριζόντια
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Κάθετα
        (0, 4, 8), (2, 4, 6) ]            # Διαγώνια

    #  Ελέγχω τις τριάδες οριζοντιες καθετε και διαγωνιο αν υπαρχει καποια γεματη με Χ  η Ο
        for a, b, c in triades:
            athroisma = numbers[a] + numbers[b] + numbers[c]
        
            if athroisma == 3:
                return "X"  # Βρήκαμε 3 x , κέρδισε το X!
            if athroisma == -3:
                return "O"  # Βρήκαμε 3 o, κέρδισε το O!

        return None #ΔΕΝ ΒΡΕΘΗΚΕ 3αδα

    def check_draw(self):
        if " " not in self.board: #ελεγχει αν υπαρχει εστω και ενα αδειο ωστε να δει αν ολο το ταμπλο γεμησε
            return True
        else:
            return False
    
    def reset(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " ",] # Αδειαζουμε τον board ωστε να ξεκινησει απο την αρχη με κενες θεσεις


if __name__ == "__main__":
    # Κώδικας για μεμονωμένη δοκιμή της λογικής του παιχνιδιού
    print("Δοκιμή λογικής παιχνιδιού (Game Logic Test)")
    
    game = Game()

    game.play_turn(0,0)
    print("ταμπλο: ",game.get_board())
