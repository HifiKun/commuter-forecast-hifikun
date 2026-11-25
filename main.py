"""One-line weather forecast for make.fun's "Charm the Commuter" bounty.

A single forecast line, at most 140 characters, for a city that does not
exist: the punchline comes first (the bus comes the moment you stop
looking for it), then the city, its weather, and a second twist — the rain
itself is running late too, so the weather shares the commuter's delay.
"""

import os

FORECAST = (
    "The bus comes the moment you stop looking for it. Gloomsbury: "
    "sunny, 19\u00b0, a breeze, and the rain is running 10 minutes late too."
)


def main() -> None:
    # One line only: the gate rejects anything over 140 chars or anything
    # that is only white space, and the judge reads a single cold line.
    text = " ".join(FORECAST.split())
    assert "\n" not in text, "forecast must be a single line"
    assert 1 <= len(text) <= 140, f"forecast must be 1-140 chars, got {len(text)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
