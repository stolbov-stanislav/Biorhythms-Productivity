"""Основная логика программы Biorithms. Используются библиотеки:
	- matplotlib, pygal (визуализации);
	- tkinter (GUI);
	- time, statistics, os;
	- sqlite3 (работа с БД);
	- собственный модуль autorun.py (работа с автозауском в системах
		Windows OS): winreg, win32api, json;
	- unittest (тесты для функций хранятся в отдельных файлах
		test_functions.py и test_classes.py; в работе программы 
		не участвуют)."""

from tkinter_mainloop import *

if __name__ == "__main__":
	
	try:
		create_db()
	except sqlite3.Error:
		pass
	finally:
		tkinter_mainloop()


