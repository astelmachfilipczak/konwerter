
import sqlite3

conn = sqlite3.connect('baza_danych.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM Bajty')
rows = cursor.fetchall()

# Wyświetl zawartość tabeli
for row in rows:
    print(f"ID: {row[0]}, Wartość bajtu: {row[1]}, Znak: {row[2]}")

cursor.close()
conn.close()