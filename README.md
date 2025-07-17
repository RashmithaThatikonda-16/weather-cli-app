# 🌦️ Weather Forecast CLI App

This is a Python-based Command Line Interface (CLI) application that allows users to get the **current weather** and basic forecast for any city in the world. It uses the **OpenWeatherMap API** to fetch real-time weather information.

---

## 📌 Features

- 🔍 Search weather by **city name**
- 🌡️ Displays **Temperature**, **Humidity**, **Wind Speed**, and **Weather Conditions**
- 📡 Uses **live data** from OpenWeatherMap API
- 🧾 Clean terminal output
- 🔐 Simple and secure API access using an API key

---

## 🖥️ How to Run the Project

### ✅ Prerequisites
- Python installed (version 3.x)
- Internet connection
- A free API key from [OpenWeatherMap](https://openweathermap.org/api)

### ▶️ Steps

1. **Clone or Download** this project folder:
   ```bash
   git clone https://github.com/your-username/weather-cli-app.git
   cd weather-cli-app
   ```

2. **Install the required library** (if not already installed):
   ```bash
   pip install requests
   ```

3. **Paste your API key** in the code:
   Open the Python file and replace the existing key:
   ```python
   api_key = "your_api_key_here"
   ```

4. **Run the project**:
   ```bash
   python weather.py
   ```

5. **Enter the city name** when prompted.

---

## 💻 Example Output

```plaintext
Enter city name: Hyderabad

🌍 Weather Report for Hyderabad:

🌡️ Temperature : 30.5°C
💧 Humidity    : 45%
🌬️ Wind Speed  : 3.2 m/s
🌈 Condition   : Light Rain
```

---

## 🔑 Getting the API Key

1. Go to [OpenWeatherMap.org](https://openweathermap.org/api)
2. Sign up (free)
3. Go to your profile → **API Keys**
4. Copy the default key and paste it in the Python file:
   ```python
   api_key = "your_api_key"
   ```

---

## 📂 File Structure

```bash
weather-cli-app/
├── weather.py         # Main Python script
└── README.md          # Project documentation
```

---

## ✍️ Author

- **Name:** Rashmitha Thatikonda  
- **Email:** your_email@example.com  
- **GitHub:** [https://github.com/your-username](https://github.com/your-username)

---

## 📄 License

This project is for **educational use only**. You may reuse and modify the code with credit to the author.

