import tkinter as tk
import json
with open('weather.json', 'r') as f:
    weather = json.load(f)
    season = weather["fact"]["season"]
    temp = weather["fact"]["temp"]
    condition = weather["fact"]["condition"]

    window = tk.Tk()
    window.title("Weather")
    window.geometry("250x100")

season_tk = tk.Label(window, text="Season: "+str(season))
season_tk.grid(column=0, row=0)

temp_tk = tk.Label(window, text="Temperture: "+str(temp))
temp_tk.grid(column=0, row=1)

condition_tk = tk.Label(window, text="Condition: "+str(condition))
condition_tk.grid(column=0, row=2)

window.mainloop()