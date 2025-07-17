import requests

api_key = "8028eb368596b326f5e918c3de9c71d4"
city_name = input("Enter city name: ")
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] != "200":
    print("City not found. Please check the name.")
else:
    print(f"\n📍 Weather Forecast for {city_name.title()} (Next 3 Days):\n")

    shown_dates = set()
    count = 0

    for forecast in data["list"]:
        date_time = forecast["dt_txt"]
        date, time = date_time.split()

        if time == "12:00:00" and date not in shown_dates:
            shown_dates.add(date)

            temp = forecast["main"]["temp"]
            humidity = forecast["main"]["humidity"]
            wind_speed = forecast["wind"]["speed"]
            description = forecast["weather"][0]["description"]

            print(f"📅 Date        : {date}")
            print(f"🌡️ Temperature : {temp}°C")
            print(f"💧 Humidity    : {humidity}%")
            print(f"🌬️ Wind Speed  : {wind_speed} m/s")
            print(f"🌈 Condition   : {description.title()}\n")

            count += 1
            if count == 3:
                break
import requests

api_key = "8028eb368596b326f5e918c3de9c71d4"
city_name = input("Enter city name: ")
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] != "200":
    print("City not found. Please check the name.")
else:
    print(f"\n📍 Weather Forecast for {city_name.title()} (Next 3 Days):\n")

    shown_dates = set()
    count = 0

    for forecast in data["list"]:
        date_time = forecast["dt_txt"]
        date, time = date_time.split()

        if time == "12:00:00" and date not in shown_dates:
            shown_dates.add(date)

            temp = forecast["main"]["temp"]
            humidity = forecast["main"]["humidity"]
            wind_speed = forecast["wind"]["speed"]
            description = forecast["weather"][0]["description"]

            print(f"📅 Date        : {date}")
            print(f"🌡️ Temperature : {temp}°C")
            print(f"💧 Humidity    : {humidity}%")
            print(f"🌬️ Wind Speed  : {wind_speed} m/s")
            print(f"🌈 Condition   : {description.title()}\n")

            count += 1
            if count == 3:
                break
