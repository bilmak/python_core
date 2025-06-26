from collections import defaultdict


def character_positions(s: str) -> dict:
    main = defaultdict(list)
    for i, v in enumerate(s):
        main[v].append(i)
    return dict(main)


character_positions("banana")
