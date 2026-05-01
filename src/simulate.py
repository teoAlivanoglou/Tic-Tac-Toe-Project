"""
Simulation script: runs N games για κάθε matchup bot και εκτυπώνει στατιστικά.
"""

from game import Game
from player import RandomBot, BetterBot, MinimaxBot
import config

GAMES = 1_000


def run_simulation(player1_cls, player2_cls, n=GAMES):
    p1_wins = 0
    p2_wins = 0
    draws = 0

    for _ in range(n):
        game = Game(3)
        p1 = player1_cls("P1", config.SYMBOL_X)
        p2 = player2_cls("P2", config.SYMBOL_O)
        game.start(p1, p2)

        result = None
        while True:
            player = game.get_current_player()
            move = player.get_move(game)

            ok, played_player = game.play_turn(move)

            if not ok:
                raise ValueError(f"Illegal move {move} by {player.name}")

            if game.check_win(player.symbol):
                result = player.symbol
                break
            elif game.check_draw():
                result = " "
                break

        if result == config.SYMBOL_X:
            p1_wins += 1
        elif result == config.SYMBOL_O:
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
    ("RandomBot vs RandomBot", RandomBot, RandomBot),
    ("BetterBot vs RandomBot", BetterBot, RandomBot),
    ("MinimaxBot vs RandomBot", MinimaxBot, RandomBot),
    ("RandomBot vs BetterBot", RandomBot, BetterBot),
    ("BetterBot vs BetterBot", BetterBot, BetterBot),
    ("MinimaxBot vs BetterBot", MinimaxBot, BetterBot),
    ("RandomBot vs MinimaxBot", RandomBot, MinimaxBot),
    ("BetterBot vs MinimaxBot", BetterBot, MinimaxBot),
    ("MinimaxBot vs MinimaxBot", MinimaxBot, MinimaxBot),
]

print(
    f"Running {GAMES:,} games per matchup ({len(matchups)} matchups = {GAMES * len(matchups):,} total)..."
)

for label, p1_cls, p2_cls in matchups:
    print(f"\n{'=' * 50}")
    print(f"  Simulating: {label}...", end="", flush=True)
    p1_wins, p2_wins, draws = run_simulation(p1_cls, p2_cls)
    print(" done.", end="")
    print_stats(label, p1_cls.__name__, p2_cls.__name__, p1_wins, p2_wins, draws)

print(f"\n{'=' * 50}")
