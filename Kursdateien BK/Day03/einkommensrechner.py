import sys


def main():
    # Bjoern Koetter 2021-12-06 v.002
    nochmal = 'j'
    while nochmal in ('j', 'J'):
        try:
            income = float(input('Gib dein Jahreseinkommen ein: '))
        except ValueError:
            print(f'Einkommen muss numerisch sein.')
            sys.exit(1)

        if income >= 1000:
            steuer = income * 0.013
        elif income >= 2000:
            steuer = income * 0.036
        elif income >= 5000:
            steuer = income * 0.055
        elif income > 5000:
            steuer = income * 0.072
        else:
            print(f'Steuer für Einkommen in Höhe von {income} wurde vom Finanzamt vergessen festzulegen.')
            sys.exit(0)
        print(f'Zahlen sie € {steuer:.2f} Steuern.')
        nochmal = input('Einkommen noch mal eingeben? [j/n] ')


if __name__ == '__main__':
    main()
