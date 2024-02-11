import mysql.connector
# Airport tauluun lisääminen vaatii myös id kentän, joka kysytään käyttäjältä nimen ja ICAO koodin lisäksi.
# Tehtävään lisätty myös poista ominaisuus, jotta lentokenttä on helppo poistaa sen tekemisen jälkeen.
def poistaa(connection, id, ident, name):
    cursor = connection.cursor()
    sql = f"delete from airport where id = '{id}' and ident = '{ident}' and name = '{name}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    if cursor.rowcount == 1:
        print(f"Lentokenntä {id}, {ident}, {name} on poistettu.")
    else:
        print("Lentokentän poistaminen ei onnistunut")
    cursor.close()
def syöttää(connection, id, ident, name):
    cursor = connection.cursor()
    sql = f"INSERT INTO airport(id, ident, name) values('{id}', '{ident}', '{name}')"
    cursor = connection.cursor()
    cursor.execute(sql)
    if cursor.rowcount == 1:
        print(f"Lentokenttä {id}, {ident} {name} luotu")
    else:
        print("Lentokentän luominen ei onnistunut")
    cursor.close()
def hakea(connection, ident):
    cursor = connection.cursor()
    sql = f"SELECT name FROM airport WHERE ident = '{ident}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
        print(result[0][0])
    else:
        print("Lentokenttää ei löydy")
    cursor.close()
def main():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        database="flight_game",
        user="root",
        password="root",
        autocommit=True
    )
    while True:
        tehtävä = input("Haluatko syöttää uuden lentokentän/ poistaa lentokentän/ hakea lentokenttää/ lopettaa ohjelman: 'S'/'P'/'H'/'L'")
        if tehtävä == 'H':
            ident = input("ICAO koodi: ")
            hakea(connection, ident)
        elif tehtävä == 'S':
            id = input("ID: ")
            ident = input("ICAO koodi: ")
            nimi = input("Lentokentän nimi: ")
            syöttää(connection, id, ident, nimi)
        elif tehtävä == 'P':
            id = input("ID: ")
            ident = input("ICAO koodi: ")
            nimi = input("Lentokentän nimi: ")
            poistaa(connection, id, ident, nimi)
        elif tehtävä == 'L':
            print("Ohjelma lopetetaan")
            break
        else:
            print("väärä syöte")

main()
