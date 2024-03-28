import mysql.connector
from flask import Flask, Response, json

app = Flask(__name__)

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="root",
    database="flight_game",
    autocommit=True
)


def hae_maa(koodi):
    cursor = connection.cursor()
    sql = f"SELECT name, municipality from airport WHERE ident='{koodi}'"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return result[0]


@app.route('/kenttä/<ICAO>')
def etsi_maa(ICAO):
    try:
        koodi = ICAO
        vastaus = hae_maa(koodi)
        tilakoodi = 200
        vastaus = {
            "ICAO": ICAO,
            "Name": vastaus[0],
            "Municipality": vastaus[1],
        }

    except mysql.connector.Error:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen yhteenlaskettava"
        }
    json_vast = json.dumps(vastaus)
    return Response(response=json_vast, status=tilakoodi, mimetype='application/json')


if __name__ == '__main__':
    app.run(use_reloader=True, port=3000)
