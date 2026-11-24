"""Everyday Wonder, Two Days to Find the Line entry.

Writes one original sentence about a small moment of wonder in
everyday life to /output/entry.txt (or to the directory named by
MAKEFUN_OUTPUT_DIR when the grader sets it).

The sentence catches an ordinary 3 a.m. kitchen sound and turns it:
the fridge hums the exact note of a grandmother's kettle, and for
one breath the kitchen is 1998 again. The surprise lands in a single
read and stays grounded in something real and specific.
"""

import os

SENTENCE = "At 3 a.m. the fridge hums the exact note my grandmother's kettle used to sing, and for one breath the kitchen is 1998 again."


def main():
    sentence = SENTENCE.strip()
    if not 1 <= len(sentence) <= 200:
        raise SystemExit(f"Sentence must be 1 to 200 characters, got {len(sentence)}")
    if "\n" in sentence or "\r" in sentence:
        raise SystemExit("Sentence must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(sentence)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != sentence:
        raise SystemExit("Read-back check failed: entry.txt does not match the sentence")
    print(f"Wrote {len(sentence)} characters to {path}")


if __name__ == "__main__":
    main()
