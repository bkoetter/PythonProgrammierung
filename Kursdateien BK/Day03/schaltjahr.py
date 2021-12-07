def main():
    try:
        jahr = int(input('Jahr eingeben: '))
    except TypeError:
        raise SystemExit("Stop right there!")

    if jahr % 400 == 0:
        schaltjahr = True
    elif jahr % 100 == 0:
        schaltjahr = False
    elif jahr % 4 == 0:
        schaltjahr = True
    else:
        schaltjahr = False

    if schaltjahr:
        print(f'Jahr {jahr} ist ein Schaltjahr')
    else:
        print(f'Jahr {jahr} ist kein Schaltjahr')


if __name__ == '__main__':
    main()
