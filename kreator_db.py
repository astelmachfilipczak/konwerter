import sqlite3

# Otwórz połączenie z bazą danych (lub utwórz nową bazę danych, jeśli nie istnieje)
conn = sqlite3.connect('baza_danych.db')

conn.execute('''
    CREATE TABLE IF NOT EXISTS Bajty (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        WartoscBajtu INTEGER,
        Znak TEXT
    )
''')

# Otwórz plik PDF
with open('s001140.pdf', 'rb') as file:
    byte = file.read(1)
    read_bytes = 0
    max_bytes_to_read = 10000

    while byte and read_bytes < max_bytes_to_read:
        byte_value = byte

        # Sprawdź, czy bajt już istnieje w bazie danych
        existing_byte = conn.execute('SELECT WartoscBajtu FROM Bajty WHERE WartoscBajtu = ?', (byte_value,)).fetchone()

        # Jeśli bajt nie istnieje, wstaw go do bazy danych
        if not existing_byte:
            conn.execute('''
                INSERT INTO Bajty (WartoscBajtu, Znak)
                VALUES (?, ?)
            ''', (byte_value, byte.decode('latin-1')))

        # Zwiększ licznik przeczytanych bajtów
        read_bytes += 1

        # Przeczytaj następny bajt
        byte = file.read(1)

# Zatwierdź zmiany i zamknij połączenie
conn.commit()
conn.close()


