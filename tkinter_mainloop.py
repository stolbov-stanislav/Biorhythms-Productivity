"""Конструктор GUI для программы Biorhithms.
	Используется библиотека tkinter."""

from tkinter import *
from functions import *
from classes import *
from autorun import *

def tkinter_mainloop():
	"""Главный цикл, разметка и события."""
	#Хранятся внутри единственной функции(особенности интерпретатора
	#tcl/tk). Вследствие, текст кода выглядит 'грязно' и чересчур
	#объёмно. Комментарии и разделители помогут сориентироваться.
	
	def update_ui():
		#Возвращает UI прежний вид.
		label_choice.configure(text='Выберите вид деятельности:',
			font='arial 14', bg='white')
		button_working.configure(text='РАБОТА', bg='green',
			font='arial 14', command=button_clicked_work)
		button_entertaining.configure(text='РАЗВЛЕЧЕНИЯ',
			bg='green', font='arial 14', command=button_clicked_enter)	
		button_learning.configure(text='ОБУЧЕНИЕ', bg='green',
			font='arial 14', command=button_clicked_learn)
			
	#Надпись для обновлённого label_choice.
	text_record = 'Запись началась...\n'
	text_record+= 'По окончании этапа оцените свою продуктивность:'
	
	#Создаёт объект деятельности. Тип деятельности по умолчанию пустой,
	#именуется в зависимости от выбора пользователя(при нажатии кнопки).
	activity = Activity()
	
	def update_activity():
		#Обновляет данные объекта и сохраняет в БД.
		activity.time_point_end()
		activity.get_mean_time()
		activity.get_duration()
		activity.update_db()
		
	#События для кнопок 'РАБОТА','РАЗВЛЕЧЕНИЯ','ОБУЧЕНИЕ'.
	#Функции практически полностью копируют друг друга.	
	def button_clicked_work():
		activity.activity = 'работа'
		activity.time_point_start()
		#Новое приглашение к выбору(оценка продуктивности).
		#(изменяет часть UI)
		label_choice.configure(text=text_record, font='arial 14',
			bg='yellow')
		#Кнопки теперь оценивают продуктивность.
		button_working.configure(text='НИЗКАЯ',
			bg='white', font='arial 14', command=work_put_eff_low)
		button_entertaining.configure(text='СРЕДНЯЯ',
			bg='white', font='arial 14', command=work_put_eff_normal)
		button_learning.configure(text='ВЫСОКАЯ',
			bg='white', font='arial 14', command=work_put_eff_high)
	def work_put_eff_low():
		activity.efficiency = (-1)
		update_activity()
		update_ui()
	def work_put_eff_normal():
		activity.efficiency = 0
		update_activity()
		update_ui()
	def work_put_eff_high():
		activity.efficiency = 1
		update_activity()
		update_ui()
	def button_clicked_enter():
		activity.activity = 'развлечения'
		activity.time_point_start()
		label_choice.configure(text=text_record, font='arial 14',
			bg='yellow')
		button_working.configure(text='НИЗКАЯ',
			bg='white', font='arial 14', command=enter_put_eff_low)
		button_entertaining.configure(text='СРЕДНЯЯ',
			bg='white', font='arial 14', command=enter_put_eff_normal)
		button_learning.configure(text='ВЫСОКАЯ',
			bg='white', font='arial 14', command=enter_put_eff_high)
	def enter_put_eff_low():
		activity.efficiency = (-1)
		update_activity()
		update_ui()
	def enter_put_eff_normal():
		activity.efficiency = 0
		update_activity()
		update_ui()
	def enter_put_eff_high():
		activity.efficiency = 1
		update_activity()
		update_ui()
	def button_clicked_learn():
		activity.activity = 'обучение'
		activity.time_point_start()
		label_choice.configure(text=text_record, font='arial 14',
			bg='yellow')
		button_working.configure(text='НИЗКАЯ',
			bg='white', font='arial 14', command=learn_put_eff_low)
		button_entertaining.configure(text='СРЕДНЯЯ',
			bg='white', font='arial 14', command=learn_put_eff_normal)
		button_learning.configure(text='ВЫСОКАЯ',
			bg='white', font='arial 14', command=learn_put_eff_high)
	def learn_put_eff_low():
		activity.efficiency = (-1)
		update_activity()
		update_ui()
	def learn_put_eff_normal():
		activity.efficiency = 0
		update_activity()
		update_ui()
	def learn_put_eff_high():
		activity.efficiency = 1
		update_activity()
		update_ui()
								
	#События для кнопок 'ПРОДОЛЖИТЕЛЬНОСТЬ','ВРЕМЯ СУТОК'.
	def button_show_duration():
		show_bar_graph_duration()
	def button_show_daily():
		show_plot_daily()
		
	#Событие для кнопки 'ВКЛЮЧИТЬ АВТОЗАПУСК'.
	#используется функция и класс модуля autorun.py.
	path = get_path('main.py')
	autorun = AutoRun('Биоритмы: продуктивность', path)
	autorun.flag_load()#Загружает флаг автозапуска.
	def button_clicked_autorun():
		if button_autorun['bg']=='green':
			button_autorun.configure(text='ВЫКЛЮЧИТЬ АВТОЗАПУСК',
				bg='red', font='arial 14')
			autorun.set_autorun()
			autorun.flag_dump()
		else:
			button_autorun.configure(text='ВКЛЮЧИТЬ АВТОЗАПУСК',
				bg='green', font='arial 14')
			autorun.remove_autorun()
			autorun.flag_dump()
										
	#Основной цикл программы и разметка.
	root=Tk()
	root.title('БИОРИТМЫ: продуктивность')
	root.resizable(False, False)#размер окна неизменяем.
	#Виджеты.
	label_choice = Label(root, text='Выберите вид деятельности:',
		font='arial 14')
	button_working = Button(root, text='РАБОТА', bg='green',
		font='arial 14', command=button_clicked_work)	
	button_entertaining = Button(root, text='РАЗВЛЕЧЕНИЯ', bg='green',
		font='arial 14', command=button_clicked_enter)	
	button_learning = Button(root, text='ОБУЧЕНИЕ', bg='green',
		font='arial 14', command=button_clicked_learn)	
	label_result = Label(root, text='Посмотреть результаты:',
		font='arial 14')	
	button_duration = Button(root, text='ПРОДОЛЖИТЕЛЬНОСТЬ', bg='yellow',
		font='arial 14', command=button_show_duration)	
	button_daily = Button(root, text='ВРЕМЯ СУТОК', bg='yellow',
		font='arial 14', command=button_show_daily)
	if autorun.flag==0:#Кнопка автозапуска зависит от флага.
		button_autorun = Button(root, text='ВКЛЮЧИТЬ АВТОЗАПУСК',
			bg='green', font='arial 14', command=button_clicked_autorun)
	else:
		button_autorun = Button(root, text='ВЫКЛЮЧИТЬ АВТОЗАПУСК',
			bg='red', font='arial 14', command=button_clicked_autorun)
	#Упаковщики.
	label_choice.grid(row=0, column=0, columnspan=3, sticky='nsew')
	button_working.grid(row=1, column=0, columnspan=1, sticky='nsew')
	button_entertaining.grid(row=1, column=1, columnspan=1,sticky='nsew')
	button_learning.grid(row=1, column=2, columnspan=1, sticky='nsew')
	label_result.grid(row=2, column=0, columnspan=3, sticky='nsew')
	button_duration.grid(row=3, column=0, columnspan=2, sticky='nsew')
	button_daily.grid(row=3, column=2, columnspan=1, sticky='nsew')
	button_autorun.grid(row=4, column=0, columnspan=3, sticky='nsew')
	#Запускает цикл.
	root.mainloop()
	
