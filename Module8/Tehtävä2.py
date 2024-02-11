import mysql.connector

def haku(connection, koodi):
    cursor = connection.cursor()
    sql = f"SELECT type FROM airport where iso_country = '{koodi}'"
    cursor.execute(sql)
    counts = cursor.fetchall()

    lentokenttä_tyypit = {}
    for luku in counts:
        tyyppi = luku[0]
        lentokenttä_tyypit[tyyppi] = lentokenttä_tyypit.get(tyyppi, 0) + 1

    for tyyppi, items in lentokenttä_tyypit.items():
        print(f" {tyyppi} {items}")

def main():

    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root",
        database="flight_game",
        autocommit=True,
    )

    koodi = input("Syötä maa koodi: ")
    haku(connection, koodi)

main()