from flask import Flask, Response, json

app = Flask(__name__)


def alkuluku(luku):
    luku = int(luku)
    if luku <= 1:
        return False
    for i in range(2, int(luku**0.5) + 1):
        if luku % i == 0:
            return False
    return True


@app.route('/alkuluku/<luku>')
def main(luku):
    try:
        luku = int(luku)
        tilakoodi = 200
        if alkuluku(luku):
            vastaus = {
                "Number": luku,
                "isPrime": True
            }

        else:
            vastaus = {
                "Number": luku,
                "isPrime": False
            }
    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen yhteenlaskettava"
        }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype='application/json')


if __name__ == '__main__':
    app.run(use_reloader=True, port=3000)
