# Yara's weather app using Tkinter
# 04.01.2022

from requests import *
from bs4 import BeautifulSoup
from tkinter import *

programWindow = Tk()
programWindow.title("City Temprature App, By Yara")
programWindow.geometry("400x600")
programWindow.resizable(0, 0)
programWindow.configure(bg="#DB6B97")

closeButton = Button(text="close program", command=programWindow.destroy)
closeButton.pack(pady=20, side=TOP)

cityLable = Label(text="Please enter the city name in the text box, \nthen press the button below")
cityLable.pack(pady=20)

cityInputField = Entry()
cityInputField.pack(pady=20)

def getWeatherMethod():
    cityname = cityInputField.get()

    if cityname == "":
        print("Enter city name")
        errorLable = Label(text=" Please enter the city name! ")
        errorLable.pack(pady=20)
    else:
        cityname = cityname + " city temperature"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        tempDB = get(
            f'https://www.google.com/search?q={cityname}&oq={cityname}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
            headers=headers)
        soup = BeautifulSoup(tempDB.text, 'html.parser')
        weatherTemp = soup.select('#wob_tm')[0].get_text().strip()
        Info_01 = Label(text=f" The {cityname} is now {weatherTemp} C ", bg="#FFF89A")
        Info_01.pack(pady=20)


checkCityButton = Button(text="Click to Get Weather", command=getWeatherMethod)
checkCityButton.pack(pady=20)

# adding a fance image:

img = PhotoImage(file='/Users/yaraelsakka/PycharmProjects/yara-weather-app-tkinter/photo_589980544.971383_s.png')
yara = Label(image=img)
yara.pack(pady=20, side=BOTTOM)

mainloop()

# end of code
# 03.01.2022