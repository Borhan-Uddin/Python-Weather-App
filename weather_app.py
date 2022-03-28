import requests
import tkinter as tk
import time
import os
from dotenv import load_dotenv

load_dotenv()


main_window = tk.Tk()
main_window.geometry('500x500')
main_window.title('Weather App using python')


def getWeatherData(main_window):
    city = textfield.get()
    api_key = os.getenv("API_KEY")
    print(api_key)
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key

    data_json = requests.get(api).json()
    weather_condition = data_json['weather'][0]['main']
    temp = int(data_json['main']['temp'] - 273.15)
    max_temp =int(data_json['main']['temp_max'] - 273.15)
    min_temp = int(data_json['main']['temp_min'] - 273.15)

    sunrise = time.strftime("%I:%M:%S",time.gmtime(data_json['sys']['sunrise'] - 3600))
    sunset = time.strftime("%I:%M:%S",time.gmtime(data_json['sys']['sunset'] - 3600))

    main_text = weather_condition +"\n" + str(temp) +"°C"
    sec_text = "\nMax temp: "+str(max_temp)+"\nMin temp: "+str(min_temp)+"\nSunrise: "+str(sunrise)+"\nSunset: "+str(sunset)

    label_1.config(text= main_text)
    label_2.config(text=sec_text)


font_default = ("Times", 15)
font_big = ("Times", 30, "bold")

textfield = tk.Entry(main_window,font = font_default)
textfield.pack(pady=15)
textfield.focus()
textfield.bind('<Return>',getWeatherData)

label_1 = tk.Label(main_window,font=font_big)
label_1.pack()
label_2 = tk.Label(main_window,font=font_default)
label_2.pack()





# mainloop 
main_window.mainloop()
