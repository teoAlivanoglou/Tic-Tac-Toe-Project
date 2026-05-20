# Ορισμός των συμβόλων που χρησιμοποιούνται στο ταμπλό
SYMBOL_O = "O"
SYMBOL_X = "✕"
SYMBOL_EMPTY = " "

# Λίστα διαθέσιμων γραμματοσειρών για το GUI
# Κάθε λεξικό περιέχει το όνομα και το αντίστοιχο αρχείο .ttf
fonts = [
    {"name": "Dela Gothic One", "fileName": "DelaGothicOne-Regular.ttf"},
    {"name": "Comfortaa", "fileName": "Comfortaa-VariableFont_wght.ttf"},
    {"name": "Sofia Sans", "fileName": "SofiaSans-VariableFont_wght.ttf"},
]

# Επιλογή της επιθυμητής γραμματοσειράς μέσω του δείκτη (index)
# 0: Dela Gothic One, 1: Comfortaa, 2: Sofia Sans
font_index = 1

# Τελικές σταθερές που θα χρησιμοποιηθούν από το window.py
FONT_NAME = fonts[font_index]["name"]
FONT_PATH = fonts[font_index]["fileName"]
