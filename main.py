import requests
import json

# Er kunnen meer plaatsen worden aangemaakt


class Antwerpen:
    latitude = 51.22
    longitude = 4.40
    hourly = "temperature_2m"


class Data:
    def __init__(self):
        self.DataLokatie = "Data/data.json"
        with open(self.DataLokatie, "r") as file:
            self.data = json.loads(file.read())

    def LoadData(self):
        with open(self.DataLokatie, "r") as file:
            self.data = json.loads(file.read())


def Init():
    # ContactServer()
    pass


def ContactServer():
    url = f"https://api.open-meteo.com/v1/forecast?latitude={Antwerpen.latitude}&longitude={Antwerpen.longitude}&hourly={Antwerpen.hourly}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        DataFileLokatie = "Data/data.json"
        with open(DataFileLokatie, "w") as file:
            json.dump(data, file, indent=4)
        print(data)
    else:
        print("Error:", response.status_code)


def TemperatuurOpTijd():
    currentData = Data()
    hourly = currentData.data["hourly"]
    times = hourly["time"]
    temperature_2m = hourly["temperature_2m"]
    timeIndex = times.index('2023-03-25T12:00')
    temperature = temperature_2m[timeIndex]
    print(f"de temperatuur op {timeIndex} uur is {temperature} C")


# input kan meer user friendly gemaakt worden

def TempOpUur():
    currentData = Data()
    datum = input("Geef een datum op in formaat (2023-03-25): ")
    tijd = input("Geef een tijdstip op in formaat (00:00 tot 23:00): ")
    Tijdstip = datum + "T" + tijd
    hourly = currentData.data["hourly"]
    times = hourly["time"]
    temperature_2m = hourly["temperature_2m"]
    timeIndex = times.index(Tijdstip)
    temperature = temperature_2m[timeIndex]
    print(f"de temperatuur op {timeIndex} uur is {temperature} C")


def Main():
    TempOpUur()


if __name__ == "__main__":
    Main()
