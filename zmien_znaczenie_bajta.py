import sqlite3

def zmien_znaczenie_bajta(id_bajta, nowe_znaczenie):

    conn = sqlite3.connect('baza_danych.db')
    cursor = conn.cursor()

    try:
        # Sprawdź, czy istnieje rekord o podanym ID
        cursor.execute('SELECT ID FROM Bajty WHERE ID = ?', (id_bajta,))
        existing_id = cursor.fetchone()

        if existing_id:
            # Aktualizuj znaczenie bajta
            cursor.execute('UPDATE Bajty SET Znak = ? WHERE ID = ?', (nowe_znaczenie, id_bajta))
            print(f'Zaktualizowano znaczenie bajta o ID {id_bajta} na: {nowe_znaczenie}')
        else:
            print(f'Nie znaleziono rekordu o ID {id_bajta}')

        conn.commit()

    finally:
        cursor.close()
        conn.close()


# Przykład użycia: zmień znaczenie bajta o ID 1 na 'X'
zmien_znaczenie_bajta(171, 'ł')



