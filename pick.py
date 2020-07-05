from curses import wrapper
from random import choice
from time import sleep


names = [
    'Pixiestick',
    'Pumpkin',
    'Marbles',
    'Pipsqueak',
    'Dandelion',
    'Scruffles',
    'Snuggles',
]


def main(stdscr):
    stdscr.clear()

    stdscr.addstr(1, 2, 'NAME PICKER')
    stdscr.addstr(2, 2, '~~~~~~~~~~~')
    stdscr.addstr(4, 2, 'A name will be picked from the list below when you press <ENTER>, good luck!')

    y = 6
    for name in names:
        stdscr.addstr(y, 4, '- {}'.format(name))
        y += 1

    y += 1
    c = 0

    while c != 10:
        c = stdscr.getch(y, 2)

    delay = 0
    name = ''
    while delay < .2:
        name = choice(names)
        stdscr.clear()
        stdscr.addstr(1, 2, 'Your name will be: {}'.format(name))
        stdscr.refresh()
        sleep(delay)
        delay += 0.001

    stdscr.addstr(3, 2, 'Welcome to the family, {}! ❤'.format(name))
    stdscr.getkey()


wrapper(main)
