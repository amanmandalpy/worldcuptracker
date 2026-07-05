import requests

from config import DATA_URL, KNOCKOUT_ROUNDS
from utils import format_score


print("=" * 60)
print("       WORLD CUP 2026 KNOCKOUT TRACKER")
print("=" * 60)


response = requests.get(DATA_URL, timeout=10)

response.raise_for_status()

data = response.json()

matches = data["matches"]


knockout_matches = []

for match in matches:
    if match["round"] in KNOCKOUT_ROUNDS:
        knockout_matches.append(match)


knockout_matches.sort(key=lambda match: match.get("num", 0))


current_round = ""

for match in knockout_matches:

    if current_round != match["round"]:
        current_round = match["round"]

        print("\n")
        print("=" * 60)
        print(current_round)
        print("=" * 60)

    score = format_score(match.get("score"))

    print(
        f"""
Match No : {match.get("num")}
Date     : {match.get("date")}
Teams    : {match["team1"]} vs {match["team2"]}
Score    : {score}
"""
    )