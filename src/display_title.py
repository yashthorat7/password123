from .utils.utils import clear_console, color_print

TITLE_TEXT = [
    ('bold #ff5ca8', r' ____   _    ____ ______ __  __ _____  ____  ____  _ ____  _____ '),
    ('bold #ff70a1', r'|  _ \ / \  / ___/ ___\ \\/  \// / _ \|  _ \|  _ \/ |___ \|___ / '),
    ('bold #ff8c8b', r'| |_) / _ \ \___ \___ \\ \ /\ / / | | | |_) | | | | | __) | |_ \ '),
    ('bold #ffa168', r'|  __/ ___ \ ___) |__) |\ V  V /| |_| |  _ <| |_| | |/ __/ ___) |'),
    ('bold #ffa724', r'|_| /_/   \_\____/____/  \_/\_/  \___/|_| \_\____/|_|_____|____/'),
]

def display_title():
    """Clears console and displays the Password123 ASCII art title."""
    clear_console()
    for color, line in TITLE_TEXT:
        color_print(line + '\n', color)
    color_print('\n')