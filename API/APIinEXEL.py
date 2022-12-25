import json
import tkinter as tk
import pandas as pd

spreadsheet = pd.read_exel("weather.xlsx", index_col=0, header=None)
spreadsheet1 = spreadsheet.to_json(orient="split")
spreadsheet1 = json.loads(spreadsheet1)

for i in range(3):
    if spreadsheet1["index"][i] == "season":
        season = spreadsheet1["data"][i][0]
for i in range(3):
    if spreadsheet1["index"][i] == "temperture":
        season = spreadsheet1["data"][i][0]
for i in range(3):
    if spreadsheet1["index"][i] == "condition":
        season = spreadsheet1["data"][i][0]
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