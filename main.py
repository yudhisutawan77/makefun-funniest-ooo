#!/usr/bin/env python3
"""Funniest Out-of-Office — make.fun entry (program/v1).

Writes a single-line out-of-office auto-reply to the output file.
The output path is $ENTRY_OUT when set, otherwise /output/entry.txt.
"""

import os

ENTRY = "I'm away this week. My inbox is now in the care of Fern, my houseplant: no thumbs, no opinions, and still a faster replier than I am."


def build_reply():
    """Return the single-line reply, enforcing the kit's 1-140 char gate."""
    reply = ENTRY.strip()
    if not 1 <= len(reply) <= 140:
        raise SystemExit(f"reply is {len(reply)} chars, must be 1-140")
    if "\n" in reply or "\r" in reply:
        raise SystemExit("reply must be a single line")
    return reply


def resolve_output_path():
    return os.environ.get("ENTRY_OUT") or "/output/entry.txt"


def main():
    reply = build_reply()
    out = resolve_output_path()
    parent = os.path.dirname(os.path.abspath(out))
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(reply)
    print(f"wrote {len(reply)} chars to {out}")


if __name__ == "__main__":
    main()
