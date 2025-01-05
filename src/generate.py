from .display_title import display_title
from .utils import panel_print
from .generate_length import generate_length
from .generate_password import generate_password
from .generate_menu import generate_menu

def generate():
    first_time = True
    while True:
        display_title()
        length = generate_length(first_time)
        password = generate_password(length)
        panel_print(password)
        if generate_menu():
            break
        first_time = False