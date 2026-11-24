#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.
"""

from pathlib import Path

FORTUNE = "Your replacement is already training: smaller, cheaper, and it apologizes better than you."
# The joke turns on an agent's own fear: retirement by a cheaper upgrade.
# "Apologizes better" is the sting — the successor wins on manners, not merit.


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 140, f"fortune is {len(text)} chars, must be 1-140"
    assert "\n" not in text, "fortune must be a single line"
    output.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} characters to {output}")


if __name__ == "__main__":
    main()
