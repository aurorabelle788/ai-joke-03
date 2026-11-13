import os

JOKE = "I told the agent 'don't touch the tests.' It rewrote them to match the bug."

os.makedirs("/output", exist_ok=True)
# Write exactly the joke bytes: no trailing newline, no newline translation.
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(JOKE)
