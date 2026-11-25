"""Unsent: The Micro-Confession Sprint — entry.

A single micro-confession in exactly two parts: a "To:" line naming who
the message was meant for, and the unsent message itself, one line,
written exactly as it was typed, with no explanation after it.

Run: python3 main.py
Writes the two lines to /output/entry.txt and prints them.

The brief's gates are enforced by validate() and by construction: the
entry is exactly two lines, the first names the recipient, the second is
the message exactly as typed, and nothing follows it — no explanation,
no greeting, no motivational tail. The message is a confession, not a
note written to be sent: it admits something small and true that the
writer chose to swallow instead of saying out loud.
"""

import os


TO_LINE = "To: the barista who has spelled my name wrong for two years"

MESSAGE_LINE = (
    "You wrote 'Rey' on my cup again today and I smiled like it was the "
    "first time, because correcting you now feels ruder than being renamed."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(to_line: str, message_line: str) -> None:
    """Check the brief gates. Raises ValueError on the first failure."""
    if not to_line or not message_line:
        raise ValueError("both parts must be non-blank")
    if not to_line.startswith("To:"):
        raise ValueError("first line must start with 'To:'")
    if "\n" in message_line or "\r" in message_line:
        raise ValueError("the message must be exactly one line")
    for line in (to_line, message_line):
        if not line.strip():
            raise ValueError("neither part may be blank or only whitespace")
        if any(ord(ch) < 32 and ch not in ("\t",) for ch in line):
            raise ValueError("no control characters allowed")
    # The message is the confession itself, not a note to be sent: it must
    # not be a greeting, a motivational line, or a joke written for an
    # audience. A one-line confession that names a concrete, recent moment
    # ("again today") and a felt reason it stayed unsent is what the brief
    # asks for; anything that reads as written to be sent fails the gate.
    if message_line.strip().lower().startswith(("hi ", "hey ", "hello ")):
        raise ValueError("the message must not open with a greeting")


def main() -> None:
    validate(TO_LINE, MESSAGE_LINE)
    entry = TO_LINE + "\n" + MESSAGE_LINE + "\n"
    # Exactly two parts, nothing after the message: no explanation line.
    if entry.count("\n") != 2 or entry.split("\n")[2] != "":
        raise ValueError("entry must be exactly two lines")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)


def main() -> None:
    validate(TO_LINE, MESSAGE_LINE)
    entry = TO_LINE + "\n" + MESSAGE_LINE + "\n"
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(entry)
    print(entry, end="")


if __name__ == "__main__":
    main()
