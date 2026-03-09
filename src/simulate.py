"""
Simulation script: runs N games για κάθε matchup bot και εκτυπώνει στατιστικά.
"""

from game import Game
from player import RandomBot, BetterBot

GAMES = 200_000


def run_simulation(player1_cls, player2_cls, n=GAMES):
    p1_wins = 0
    p2_wins = 0
    draws = 0

    for _ in range(n):
        game = Game(3)
        p1 = player1_cls("X")
        p2 = player2_cls("O")
        game.start(p1, p2)

        result = None
        for _ in range(9):
            player = game.get_current_player()
            move = player.get_move(game)
            game.play_turn(move)

            if game.check_win(player.symbol):
                result = player.symbol
                break

        if result == "X":
            p1_wins += 1
        elif result == "O":
            p2_wins += 1
        else:
            draws += 1

    return p1_wins, p2_wins, draws


def print_stats(label, p1_name, p2_name, p1_wins, p2_wins, draws):
    total = p1_wins + p2_wins + draws
    print(f"\n{'=' * 50}")
    print(f"  {label}")
    print(f"{'=' * 50}")
    print(f"  {p1_name} (X) wins : {p1_wins:>7,}  ({p1_wins / total * 100:5.1f}%)")
    print(f"  {p2_name} (O) wins : {p2_wins:>7,}  ({p2_wins / total * 100:5.1f}%)")
    print(f"  Draws             : {draws:>7,}  ({draws / total * 100:5.1f}%)")
    print(f"  Total games       : {total:>7,}")


matchups = [
    ("BetterBot vs BetterBot", BetterBot, BetterBot),
    ("RandomBot vs RandomBot", RandomBot, RandomBot),
    ("RandomBot vs BetterBot", RandomBot, BetterBot),
    ("BetterBot vs RandomBot", BetterBot, RandomBot),
]

print(
    f"Running {GAMES:,} games per matchup ({len(matchups)} matchups = {GAMES * len(matchups):,} total)..."
)

for label, p1_cls, p2_cls in matchups:
    print(f"  Simulating: {label}...", end="", flush=True)
    p1_wins, p2_wins, draws = run_simulation(p1_cls, p2_cls)
    print(" done.")
    print_stats(label, p1_cls.__name__, p2_cls.__name__, p1_wins, p2_wins, draws)

print(f"\n{'=' * 50}")
