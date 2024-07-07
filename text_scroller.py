from os import system
from time import sleep
from typing import List

from letters.banner import BANNER_MAP


def ascii_to_screen(text: str, height=5, width=25) -> List[List[str]]:
    letters = []

    for char in text:
        try:
            letters.append(BANNER_MAP[char])
            letters.append(BANNER_MAP['padding'])
        except KeyError:
            print(f"char {char} was not in {BANNER_MAP['name']}")
            break

    return letters


def new_screen(width, height) -> List[List[str]]:
    return [[" " for _ in range(width)] for _ in range(height)]


def display_screen(screen: List[List[str]], width) -> None:
    for line in screen:
        print("".join(line[:width]))


def scroll_text(ascii_text, speed=0.3, height=7, width=100) -> None:

    letters = ascii_to_screen(ascii_text, height=height, width=width)

    screen = new_screen(width=width, height=height)

    for letter in letters:
        for i, line in enumerate(letter):
            screen[i].extend(line)

    while True:
        screen = [line[1:] + line[:1] for line in screen]
        display_screen(screen, width)
        sleep(speed)
        # print(chr(27) + "[2J")
        system('printf "\033c"')


if __name__ == "__main__":
    scroll_text('Hello, World!')
