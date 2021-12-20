import random
import string


def get_chars():
    return string.ascii_letters + string.digits


def get_password(chars: str, size: int):
    return "".join(random.choice(chars) for x in range(size))


def main():
    size = 8
    chars = get_chars()
    passw = get_password(chars, size)
    print(passw)


if __name__ == '__main__':
    main()
