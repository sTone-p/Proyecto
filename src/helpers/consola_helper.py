import os

from termcolor import colored, cprint


def limpiar_consola():
    if os.name == 'nt':
        os.system('cls')


def get_string(message: str, accept_blank: bool = True, only_letters: bool = False) -> str:
    while True:
        value = input(colored(message, 'blue')).strip()
        
        if not value and not accept_blank:
            cprint('Debe ingresar algo.', 'red')
            continue
        
        if only_letters and not value.replace(" ", "").isalpha():
            cprint('Solo se permiten letras y espacios.', 'red')
            continue
        
        return value
