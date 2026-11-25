"""Worst Fix Ever: Funniest Commit Message.

Writes one commit message to $MAKEFUN_OUTPUT_DIR/entry.txt: the fix
that cured the crash by removing the thing that crashed. Standard
library only.
"""

import os

MESSAGE = "fix: checkout no longer crashes \u2014 I deleted the checkout"


def check_message(text):
    """Check the commit message against the competition gate.

    The gate needs UTF-8 text of 1 to 100 characters, not only white
    space, in a single line: one commit message for a bug fix that
    made everything worse. Returns the cleaned text or raises
    ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("commit message must not be only whitespace")
    if len(cleaned) > 100:
        raise ValueError(
            "commit is %d characters, over the 100 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("commit message must be exactly one line")
    return cleaned


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_message(MESSAGE)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
