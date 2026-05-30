import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "c4db8c57ab2f1f2193b24f1df5f787d2"

def get_weather():
    city = city_entry.get().strip()

    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if str(data.get("cod")) != "200":
            messagebox.showerror("Error", "City not found")
            return

        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"].title()

        result_label.config(
            text=f"""
City: {city_name}, {country}

Temperature: {temp}°C
Feels Like: {feels_like}°C
Humidity: {humidity}%

Condition: {weather}
"""
        )

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong\n{e}")

# Main Window
root = tk.Tk()
root.title("Weather App")
root.geometry("500x400")
root.resizable(False, False)

# Heading
title_label = tk.Label(
    root,
    text="🌦 Weather App",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=15)

# Entry
city_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=25
)
city_entry.pack(pady=10)

# Button
search_btn = tk.Button(
    root,
    text="Get Weather",
    font=("Arial", 12),
    command=get_weather
)
search_btn.pack(pady=10)

# Result
result_label = tk.Label(
    root,
    text="Enter a city name",
    font=("Arial", 12),
    justify="left"
)
result_label.pack(pady=20)

root.mainloop()