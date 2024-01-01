import requests
from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("CrystalsWeather")
win.geometry("400x300")
win.resizable(False, False)

def toggle_entry():
    if var.get():
        key.delete(0, END)
        key.insert(0, '55f1c70a942f84460a16f539a714dafb')
        key.config(state='readonly')
    else:
        key.config(state='normal')
        key.delete(0, END)
def getcords():
    try:
        capital = city.get()
        api = key.get()
        r = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={capital}&appid={api}")
        r.raise_for_status()
        jsonCity = r.json()
        print('Данные города получены')
        lat = jsonCity[0]['lat']
        lon = jsonCity[0]['lon']
        print('Точные координаты города получены')
        getplace(lat, lon, api)
    except requests.exceptions.HTTPError as err:
        if r.status_code == 401:
            messagebox.showerror(title='Неверный API Key', message='Убедитесь в правильности написания вашего ключа.')
        elif r.status_code == 400:
            messagebox.showerror(title='Не можем найти погоду', message=f'Мы не смогли найти данные о погоде в городе {capital}. Проверьте правильность написания.')
        else:
            messagebox.showerror(title='Не можем найти погоду', message=f'Мы не смогли найти данные о погоде в городе {capital}. Проверьте правильность написания.')
def getplace(lat, lon, api):
    try:
        place = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}")
        place.raise_for_status()
        jsonPlace = place.json()
        print('Данные о погоде города получены')
        nameofcity = jsonPlace['name']
        temp = jsonPlace['main']['temp']
        temp1 = temp-273.15
        weath = jsonPlace['weather'][0]['main']
        print('Точная погода получена.')
        namecity.config(text=f'Город (страна): {nameofcity}')
        temperature.config(text=f'Погода: {weath}')
        weather.config(text=f'Температура: {temp1} градусов')
        print("Выведено на экран.")
    except requests.exceptions.HTTPError as err:
        messagebox.showerror(title='Произошла ошибка', message='Убедитесь в правильности написания вашего ключа и названия города.')
title = Label(win, text="Погода на питоне", font=("Segoe UI", 14, "bold"))
title.pack()
note = Label(win, text="Введи название города ниже", font=("Segoe UI", 11))
note.pack()
city = Entry(win, font=("Segoe UI", 9))
city.pack()
note1 = Label(win, text="Введи API Key с сайта openweathermap.org ниже", font=("Segoe UI", 11))
note1.pack()
note3 = Label(win, text="ИЛИ", font=("Segoe UI", 14))
note3.pack()
var = IntVar()
checkbutton = Checkbutton(win, text="Вставить API ключ автора", variable=var, command=toggle_entry)
checkbutton.pack()
key = Entry(win, textvariable='123', font=("Segoe UI", 9), state='normal')
key.pack()
namecity = Label(win, text="Город: ", font=("Segoe UI", 12))
namecity.pack()
temperature = Label(win, text="Температура: ", font=("Segoe UI", 12))
temperature.pack()
weather = Label(win, text="Погода: ", font=("Segoe UI", 12))
weather.pack()

button = Button(win, text='Получить погоду', font=("Segoe UI", 9), command=getcords)
button.pack()


win.mainloop()

