from os import getenv


def main():
    with open(f'{getenv("HOME")}/testfile.txt', 'w') as writer:
        writer.write('Hello World!')


if __name__ == '__main__':
    main()
