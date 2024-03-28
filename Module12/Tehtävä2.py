import requests
api_key = "{Enter Api}"

paikka = input("Anna Paikan nimi: ").lower()

url2_paikka = f'https://api.openweathermap.org/geo/1.0/direct?q={paikka}&limit=5&appid={api_key}'

try:
    vastaus = requests.get(url2_paikka)

    if vastaus.status_code == 200:
        vastaus = vastaus.json()
        latitude = vastaus[0]["lat"]
        longitude = vastaus[0]["lon"]

        url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
        vastaus = requests.get(url)
        if vastaus.status_code == 200:
            vastaus = vastaus.json()
            print(f"{vastaus['weather'][0]['main']}, {vastaus['weather'][0]['description']}, {(vastaus['main']['temp'] - 273.15):.2f}\u2103")

        else:
            print("Error")
            print(vastaus.status_code)

    else:
        print("Error")
        print(vastaus.status_code)

except requests.exceptions.ConnectionError as error:
    print("Connection Error")
    print(error)