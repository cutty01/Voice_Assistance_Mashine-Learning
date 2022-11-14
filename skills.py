import os
import webbrowser
import sys
import subprocess
import voice
from vars import *
import time 
import pyautogui


try:
	import requests		#pip install requests
except:
	pass

def browser():
	'''Открывает браузер заданнный по уполчанию в системе с url указанным здесь'''
	webbrowser.open('https://google.com', new=1)


def youtube():
	webbrowser.open('https://www.youtube.com', new=2)


def closed_browser():
		os.system("taskkill /im chrome.exe /f")



def game():
	'''Нужно разместить путь к exe файлу любого вашего приложения'''
	try:
		subprocess.Popen('path')
	except:
		voice.speaker('Путь к файлу не найден, проверьте, правильный ли он')

def stop_game():
	try:
		os.system("taskkill /im javaw.exe /f")
	except:
		voice.speaker('Процесс был завершен ранее!')

def offpc():
	#Эта команда отключает ПК под управлением Windows

	os.system('shutdown /s /t 2')
	print('пк был бы выключен, но команде # в коде мешает;)))')


def weather():
	'''Для работы этого кода нужно зарегистрироваться на сайте
	https://openweathermap.org или переделать на ваше усмотрение под что-то другое'''
	try:
		params = {'q': 'Сюда впиши свой город', 'units': 'metric', 'lang': 'ru', 'appid': 'сюда впиши api ключ'}
		response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
		if not response:
			raise
		w = response.json()
		voice.speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")
		
	except:
		voice.speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')


def offBot():
	'''Отключает бота'''
	sys.exit()


def passive():
	'''Функция заглушка при простом диалоге с ботом'''
	pass
