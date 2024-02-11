import mysql.connector

def haku(connection, koodi):
    sql = f"SELECT name,municipality FROM airport WHERE ident = '{koodi}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(f"{result[0][0]}, {result[0][1]}")
def main():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        passwd="root",
        database="flight_game",
        autocommit=True
    )

    koodi = input("ICAO-koodi: ")
    haku(connection, koodi)

main()