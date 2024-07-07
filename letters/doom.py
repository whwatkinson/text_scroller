DOOM_MAP = {"a": ""}


for key, value in DOOM_MAP.items():
    for row in value:
        print("".join(row), end="\n")
