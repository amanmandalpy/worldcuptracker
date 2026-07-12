import requests

DATA_URL = "https://raw.githubusercontent.com/openfootball/worldcup.json/master/2026/worldcup.json"

KNOCKOUT = [
    "Round of 32",
    "Round of 16",
    "Quarter-final",
    "Semi-final",
    "Match for third place",
    "Final",
]


def format_score(score):
    """
    Return a readable score.
    """

    if not score:
        return "Upcoming"

    # Penalty Shootout
    if "p" in score:
        et = score.get("et", score.get("ft"))
        p = score["p"]
        return f"{et[0]} - {et[1]} ({p[0]}-{p[1]} Pens)"

    # Extra Time
    if "et" in score:
        et = score["et"]
        return f"{et[0]} - {et[1]} (AET)"

    # Normal Time
    ft = score.get("ft", [0, 0])
    return f"{ft[0]} - {ft[1]}"


def get_matches():

    response = requests.get(DATA_URL, timeout=10)

    response.raise_for_status()

    data = response.json()

    matches = data["matches"]

    knockout = []

    for match in matches:

        if match["round"] in KNOCKOUT:

            # Add formatted score
            match["formatted_score"] = format_score(match.get("score"))

            knockout.append(match)

    knockout.sort(key=lambda match: match.get("num", 0))

    return knockout