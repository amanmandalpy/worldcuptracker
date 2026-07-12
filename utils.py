def format_score(score):
    """
    Format football scores.
    """

    if not score:
        return "Upcoming"

    ft = score.get("ft", [0, 0])

    if "p" in score:
        et = score.get("et", ft)
        p = score["p"]
        return f"{et[0]}-{et[1]} ({p[0]}-{p[1]} Pens)"

    if "et" in score:
        et = score["et"]
        return f"{et[0]}-{et[1]} (AET)"

    return f"{ft[0]}-{ft[1]}"