"""Rank numeric tokens by frequency."""


def rank(lines):
    counts = {}
    for line in lines:
        for token in line.split():
            try:
                v = float(token)
            except ValueError:
                continue
            counts[v] = counts.get(v, 0) + 1
    return sorted(counts.items(), key=lambda kv: -kv[1])


def rank_file(path):
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        return rank(handle)
