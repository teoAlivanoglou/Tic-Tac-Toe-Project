ΑΠΟ ΤΟ PROJECT ROOT (ΑΥΤΟΝ ΤΟΝ ΦΑΚΕΛΟ)

ΧΩΡΙΣ VIRTUAL ENVIRONMENT:

pip install -r requirements.txt
python src/main.py

ΕΝΑΛΛΑΚΤΙΚΑ ΜΕ ΧΡΗΣΗ VENV:

python -m venv .venv
./.venv/Scripts/activate.bat
pip install -r requirements.txt

Για το κύριο πρόγραμμα:
python src/main.py

Για την προσομοίωση (τα minimax χρειάζονται πολύ χρόνο για να τελειώσουν):
python src/simulate.py

Ομοίως μπορεί κάποιος να τρέξει και μεμονωμένα τα υπόλοιπα αρχεία για να εκτελεστεί ο δοκιμαστικός κώδικας:
python src/game.py
python src/player.py
python src/window.py


ΣΗΜΕΙΩΣΗ:
Σε κάθε περίπτωση μπορεί κάποιος να χρησιμοποιήσει το "pythonw" αντί για το "python" και να τρέξει το παράθυρο χωρίς μηνύματα στην κονσόλα.