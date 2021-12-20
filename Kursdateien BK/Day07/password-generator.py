import random
import string


def get_chars():
    return string.ascii_letters + string.digits + string.punctuation


def get_password(chars: str, opts: dict):
    return "".join(random.choice(chars) for _ in range(opts['password_length']))


def get_user_input():
    return {
        'password_length': int(input('Wie lang sollen die Passwörter sein? ')),
        'password_count': int(input('Wie viele Passwörter sollen generiert werden? ')),
    }


def main():
    opts = get_user_input()
    chars = get_chars()
    for _ in range(opts['password_count']):
        print(get_password(chars, opts))


if __name__ == '__main__':
    main()
