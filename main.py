import Plaatsen as p
import requests
import json
from matplotlib import pyplot
from datetime import datetime, timedelta
# Er kunnen meer plaatsen worden aangemaakt



class Data:
    def __init__(self):
        self.DataLokatie = "Data/data.json"
        with open(self.DataLokatie, "r") as file:
            self.data = json.loads(file.read())
        self.currentDate = datetime.now().strftime("%Y-%m-%d")

    def LoadData(self):
        with open(self.DataLokatie, "r") as file:
            self.data = json.loads(file.read())


def Init():
    # ContactServer()
    pass


def ContactServer():
    lokatie = p.Antwerpen()
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lokatie.latitude}&longitude={lokatie.longitude}&hourly={lokatie.hourly}"
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


def Plot():
    currentData = Data()
    hourly = currentData.data["hourly"]
    times = hourly["time"]
    currentDayTimes = []
    currentDayTemperatures = []
    for i, time in enumerate(times):
        if time.startswith(currentData.currentDate):
            currentDayTimes.append(
                datetime.fromisoformat(time).strftime("%H:%M"))
            currentDayTemperatures.append(hourly["temperature_2m"][i])
    pyplot.plot(currentDayTimes, currentDayTemperatures,
                label="Temperatuur", color="red", marker="o", linestyle="dashed")
    pyplot.xticks(range(0, len(currentDayTimes), 1), rotation=45)
    for time, temperature in zip(currentDayTimes, currentDayTemperatures):
        pyplot.annotate(f"{temperature} C",
                        (time, temperature+0.2), ha="center", rotation=45)

    pyplot.xlabel("Tijd")
    pyplot.ylabel("Temperatuur")
    pyplot.title("Temperatuur in Antwerpen op " + currentData.currentDate)
    pyplot.show()


def Main():
    Plot()


if __name__ == "__main__":
    Main()
