with open('s001140.pdf', 'rb') as file:
    byte = file.read(1)
    while byte:
        # Wyświetl bajty
        print(byte, end=" ")
        byte = file.read(1)

