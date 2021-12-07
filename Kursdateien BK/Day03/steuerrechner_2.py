import sys


def main():
    # Bjoern 2021-12-06 v.001
    try:
        income = float(input('Gib dein Jahreseinkommen ein: '))
    except ValueError:
        print(f'Einkommen muss numerisch sein.')
        sys.exit(1)

    steuersatz = {
        1000: 0.013,
        2000: 0.036,
        5000: 0.055,
    }

    if income > 5000:
        steuer = income * 0.072
    else:
        steuer steuersatz.get(income, 0):
        steuer = income * st

        print(f'Steuer für Einkommen in Höhe von {income} wurde vom Finanzamt vergessen festzulegen.')
        sys.exit(0)

    print(f'Zahlen sie € {steuer:.2f} Steuern.')


if __name__ == '__main__':
    main()
