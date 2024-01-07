import sqlite3


conn = sqlite3.connect('baza_danych.db')
cursor = conn.cursor()

# Wykonaj zapytanie SELECT, aby pobrać dane z tabeli Bajty
cursor.execute('SELECT WartoscBajtu, Znak FROM Bajty')
rows = cursor.fetchall()
cursor.close()

# Przekształć wyniki na słownik, gdzie klucz to wartość bajtu, a wartość to odpowiadający mu znak
bajty_mapping = {row[0]: row[1] for row in rows}


with open('s001140.pdf', 'rb') as file:
    byte = file.read(1)
    inside_parentheses = False
    text_inside_parentheses = ""

    while byte:
        # Odczytaj bajt
        byte_value = byte

        # Sprawdź, czy istnieje odpowiadający mu znak w bazie danych
        znak = bajty_mapping.get(byte_value, 'Nieznany znak')

        # Kod do opuszczenia nawiasów
        if znak == '(':
            inside_parentheses = True

        elif znak == ')':
            inside_parentheses = False

        elif inside_parentheses:
            text_inside_parentheses += znak

        # Przeczytaj następny bajt
        byte = file.read(1)

# Podziel tekst na słowa, dodaj odstępy między słowami, a następnie dołącz z powrotem
text_inside_parentheses_with_spaces = ' '.join(text_inside_parentheses.split())


print(text_inside_parentheses_with_spaces)
conn.close()