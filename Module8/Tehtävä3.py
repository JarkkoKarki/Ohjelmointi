import mysql.connector
from geopy.distance import geodesic

print("Ohjelma laskee kahden lentokentän välisen etäisyyden")
# Funktio laskemiselle, jossa haetaan ICAO-koodit tietokannasta ja lasketaan etäisyys.


def laske(connection, eka, toka):
    cursor = connection.cursor()
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{eka}'"
    sql2 = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{toka}'"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.execute(sql2)
    result2 = cursor.fetchall()
    matka = geodesic(result[0],result2[0]).kilometers
    print(f"välimatka on {matka:.0f} kilometriä")
    cursor.close()

# Pääfunktio, jossa kysytään lentokenttien ICAO-koodit.


def main():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root",
        database="flight_game",
        autocommit=True,
    )

    eka = input("Kerro ensimmäisen lentokentän ICAO-koodi: ")
    toka = input("Kerro toisen lentokentän ICAO-koodi: ")
    laske(connection, eka, toka)


main()
