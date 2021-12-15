# 2021-12-15 Björn v0.0.1

getraenke = {'Cola': 1.5, 'Fanta': 1.4, 'Wein': 3.2, 'Whisky': 4.8, 'Gin': 3.8, 'Tonic': 1.6}


def selection():
    """selection fragt den Anwender nach einer Auswahl ab und gibt ein Integer zurück"""
    print('Bitte wähle eine der folgenden Optionen:')
    print('1. Abfrage, welche Getränke haben wir')
    print('2. Abfrage, welche Getränke bekomme ich für mein Geld')
    print('3. Ein Getränk bestellen')
    while True:
        try:
            return int(input('Auswahl? [1, 2, 3] '))
        except ValueError:
            print('Gib bitte eine Zahl 1, 2 oder 3 ein.')


def getraenk_abfragen():
    """getraenk_abfragen erfragt ein Getränk vom Anwender und prüft, ob dieses verfügbar ist"""
    getraenk = input('Welches Getränk soll ich auf Verfügbarkeit prüfen? ')
    if getraenk in getraenke.keys():
        print(f'Getränk {getraenk} können wir anbieten')
    else:
        print(f'Getränk {getraenk} haben wir nicht im Angebot')


def getraenk_budget():
    """getraenk_budget fragt den Anwender, wie viel Geld für Getränke verfügbar ist"""
    while True:
        try:
            budget = int(input('Wie viel Geld hast du für Getränke? '))
            break
        except ValueError:
            print('Gib bitte eine Zahl oder Kommazahl ein')

    erschwinglich = []
    for getraenk, preis in getraenke.items():
        if preis <= budget:
            erschwinglich.append(getraenk)
    print(f'Du kannst dir die Getränke {", ".join(erschwinglich)} leisten')


def getraenk_bestellen():
    """getraenk_bestellen nimmt die Bestellung des Anwenders auf"""
    getraenk = input('Welches Getränk möchtest du bestellen? ')
    if getraenk in getraenke.keys():
        print(f'Deine Bestellung für Getränk {getraenk} wurde aufgenommen')
    else:
        print(f'Getränk {getraenk} haben wir nicht im Angebot')


def main():
    optionen = [getraenk_abfragen, getraenk_budget, getraenk_bestellen]
    menue_select: int = selection()
    optionen[menue_select - 1]()


if __name__ == '__main__':
    main()
