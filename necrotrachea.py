#!/usr/bin/env python3
"""necrotrachea — random metal/gore name generator.

Names are assembled from prefix / middle / suffix fragment banks and padded
with middle fragments until the target character length (approx) is reached.

Usage:
    python necrotrachea.py                     # 1 name, ~12 chars
    python necrotrachea.py -n 10               # 10 names
    python necrotrachea.py -l 20               # aim for ~20-char names
    python necrotrachea.py -n 5 -l 8 --sep ''  # 5 short glued names
"""

import argparse
import random

PREFIXES = [
    "Gore", "Blood", "Corpse", "Viscer", "Rot", "Putr", "Necro", "Carn",
    "Butcher", "Slaughter", "Disembowl", "Exsanguin", "Gut", "Flesh",
    "Bone", "Marrow", "Grave", "Crypt", "Cadaver", "Sepulch", "Tor",
    "Vile", "Fetid", "Maggot", "Worm", "Bile", "Phlegm", "Pus", "Gangr",
    "Ulcer", "Cyst", "Boil", "Scab", "Wound", "Gash", "Lacer", "Punct",
    "Skull", "Spine", "Rib", "Femur", "Sinew", "Tendon", "Gristle",
    "Hemorrh", "Thromb", "Necrot", "Putresc", "Mortu", "Funer", "Sepul",
]

MIDDLES = [
    "spawn", "rend", "gorg", "churn", "slath", "writhe", "belch", "spew",
    "clot", "spawn", "fiend", "stalk", "crawl", "drip", "seep", "ooze",
    "blight", "writhe", "rot", "murk", "grime", "mawl", "gor", "husk",
]

SUFFIXES = [
    "fiend", "wraith", "reaper", "butcher", "lord", "spawn", "shroud",
    "casket", "womb", "pyre", "altar", "chalice", "monolith", "shrine",
    "throne", "vortex", "abyss", "chasm", "mausoleum", "ossuary",
    "effigy", "reliquary", "sepulcher", "catacomb", "gallows", "pit",
    "eater", "devourer", "feaster", "gurgler", "sprayer", "chewer",
]

JOINERS = ["", "", "", "-", " "]  # mostly glued, sometimes separated


def make_name(target_len: int, rng: random.Random) -> str:
    """Assemble one name of roughly `target_len` characters."""
    name = rng.choice(PREFIXES)
    joiner = rng.choice(JOINERS)

    # Add middle fragments until we're close to the target length.
    while len(name) + len(joiner) + len(rng.choice(SUFFIXES)) < target_len - 3:
        mid = rng.choice(MIDDLES)
        name += mid
        # occasional hard consonant for that death-metal flavor
        if rng.random() < 0.3:
            name += rng.choice(["x", "th", "gh", "rr", "ck"])

    name += joiner + rng.choice(SUFFIXES)
    return name


def main() -> None:
    ap = argparse.ArgumentParser(description="Random metal/gore name generator")
    ap.add_argument("-n", "--count", type=int, default=1,
                    help="how many names to generate (default 1)")
    ap.add_argument("-l", "--length", type=int, default=12,
                    help="target name length in characters (default 12)")
    ap.add_argument("-s", "--seed", type=int, default=None,
                    help="random seed for reproducibility")
    args = ap.parse_args()

    rng = random.Random(args.seed)
    for _ in range(args.count):
        print(make_name(args.length, rng))


if __name__ == "__main__":
    main()
