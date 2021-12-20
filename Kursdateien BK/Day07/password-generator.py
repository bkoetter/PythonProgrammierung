import random
import string
from os import getenv


def get_chars():
    return string.ascii_letters + string.digits + string.punctuation


def get_password(chars: str, opts: dict):
    return "".join(random.choice(chars) for _ in range(opts['password_length']))


def get_user_input():
    while True:
        try:
            return {
                'password_length': int(input('Wie lang soll das jeweilige Passwörter sein? ')),
                'password_count': int(input('Wie viele Passwörter sollen generiert werden? ')),
                'password_output': input('Dateiname Passwörter oder [Eingabe] für Ausgabe auf Konsole: ')
            }
        except ValueError:
            print('Die Eingabe muss numerisch sein.')


def output(opts: dict, passwords: tuple):
    if not opts['password_output']:
        for password in passwords:
            print(password)
        return
    with open(f'{getenv("HOME", ".")}/{opts["password_output"]}', 'w') as writer:
        for password in passwords:
            writer.write(f'{password}\n')
    print(f'Ausgabe erfolgt nach {getenv("HOME", ".")}/{opts["password_output"]}')


def main():
    opts = get_user_input()
    chars = get_chars()
    passwords = tuple(get_password(chars, opts) for _ in range(opts['password_count']))
    output(opts, passwords)


if __name__ == '__main__':
    main()
