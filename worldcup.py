import requests

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from config import DATA_URL, KNOCKOUT_ROUNDS
from utils import format_score

console = Console()


def fetch_data():
    response = requests.get(DATA_URL, timeout=10)
    response.raise_for_status()
    return response.json()


def get_knockout_matches(matches):

    knockout = []

    for match in matches:
        if match["round"] in KNOCKOUT_ROUNDS:
            knockout.append(match)

    knockout.sort(key=lambda x: x.get("num", 0))

    return knockout


def display_matches(matches):

    console.print(
        Panel.fit(
            "[bold yellow]⚽ FIFA WORLD CUP 2026 TRACKER[/bold yellow]",
            border_style="green",
        )
    )

    current_round = None
    table = None

    for match in matches:

        if current_round != match["round"]:

            if table:
                console.print(table)
                console.print()

            current_round = match["round"]

            table = Table(
                title=f"[bold cyan]{current_round}[/bold cyan]",
                show_lines=True,
            )

            table.add_column("Match No", justify="center", style="yellow")
            table.add_column("Date", style="green")
            table.add_column("Team 1", style="cyan")
            table.add_column("Team 2", style="cyan")
            table.add_column("Score", justify="center", style="magenta")

        table.add_row(
            str(match.get("num", "")),
            match.get("date", ""),
            match.get("team1", ""),
            match.get("team2", ""),
            format_score(match.get("score")),
        )

    if table:
        console.print(table)


def main():

    data = fetch_data()

    matches = data["matches"]

    knockout = get_knockout_matches(matches)

    display_matches(knockout)


if __name__ == "__main__":
    main()