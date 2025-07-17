import requests
api_key="8028eb368596b326f5e918c3de9c71d4"
city=input("Enter city name")
url=f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
response=requests.get(url)
data=response.json()
if data['cod']!="200":
    print("city  not found.Please check the name.")
else:
    print(f"\nWeather Report for{city.title()}:")
    current=data['list'][0]
    temp=current['main']['temp']
    humidity=current['main']['humidity']
    wind=current['wind']['speed']
    condition=current['weather'][0]['description']
    print(f"Temperature:{temp}C")
    print(f"Humidity:{humidity}%")
    print(f"wind speed:{wind}m/s")
    print(f"condition:{condition.title()}")
