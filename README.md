# 🌦️ 3-Day Weather Forecast CLI App

This is a **Python command-line application** that fetches the 3-day weather forecast for any city using the **OpenWeatherMap API**.

It shows temperature, humidity, wind speed, and weather conditions for the next **3 days at 12:00 PM** (midday) — giving you a quick glance at the weather ahead.

---

## 📌 Features

- ✅ Takes city name as user input  
- ✅ Uses OpenWeatherMap 5-day/3-hour forecast API  
- ✅ Filters forecast to display **one reading per day**  
- ✅ Displays:
  - 🌡️ Temperature
  - 💧 Humidity
  - 🌬️ Wind speed
  - 🌈 Weather condition  
- ✅ Clean and readable CLI output

---

## 📸 Sample Output

```
Enter city name: Hyderabad

📍 Weather Forecast for Hyderabad (Next 3 Days):

📅 Date        : 2025-07-18
🌡️ Temperature : 30.3°C
💧 Humidity    : 49%
🌬️ Wind Speed  : 3.6 m/s
🌈 Condition   : Light Rain

📅 Date        : 2025-07-19
🌡️ Temperature : 29.7°C
💧 Humidity    : 52%
🌬️ Wind Speed  : 3.2 m/s
🌈 Condition   : Scattered Clouds

📅 Date        : 2025-07-20
🌡️ Temperature : 31.1°C
💧 Humidity    : 46%
🌬️ Wind Speed  : 2.9 m/s
🌈 Condition   : Clear Sky
```

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/weather-forecast-cli.git
cd weather-forecast-cli
```

### 2. Install Required Package

```bash
pip install requests
```

### 3. Run the Python Script

```bash
python weather_forecast.py
```

---

## 🔑 Get Your OpenWeatherMap API Key

1. Visit [https://openweathermap.org/api](https://openweathermap.org/api)
2. Sign up and log in
3. Navigate to **API Keys**
4. Copy your key and replace it in the script:

```python
api_key = "your_api_key_here"
```

---

## 📁 File Structure

```
weather-forecast-cli/
├── weather_forecast.py   # Main script
└── README.md             # Documentation
```

---

## 🛠 Tech Used

- Python 3
- Requests Library
- OpenWeatherMap API

--
