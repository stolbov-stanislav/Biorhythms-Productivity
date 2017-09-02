"""Набор функций для программы Biorhithms. Содержит функции для работы
	с визуализациями, а также функции для работы с БД.
	Используются библиотеки matplotlib и pygal."""

import sqlite3
import matplotlib.pyplot as plt
import pygal
import os

def show_plot_daily():
	"""Создаёт визуализацию  на основе данных о деятельности
	и соответствующих ей продуктивности и времени суток(усредн.)."""
	
	names = ['работа','развлечения','обучение']
		
	#Заполняет списки координат.
	x_values = range(0,25)
	work_values = get_daily_eff(names[0])
	entertain_values = get_daily_eff(names[1])
	learn_values = get_daily_eff(names[2])
	
	#Параметры графика.
	title = "Работа - синий, Развлечения - красный, Обучение - зелёный"
	plt.figure(figsize=(10,6))
	plt.title(title, fontsize=14)
	plt.xlabel("Время суток(среднее, 24-часовой формат)", fontsize=18)
	plt.ylabel("Продуктивность", fontsize=18)
	plt.tick_params(axis='both', which='major', labelsize=14)
	plt.axis([0, 24, -10, 10])
	#Рисует графики.
	plt.plot(x_values, work_values)
	plt.plot(x_values, entertain_values)
	plt.plot(x_values, learn_values)
	#Закрашивает пространство между осями.
	plt.fill_between(x_values, work_values, facecolor='blue',
		alpha=0.25)
	plt.fill_between(x_values, entertain_values, facecolor='red',
		alpha=0.25)
	plt.fill_between(x_values, learn_values, facecolor='green',
		alpha=0.25)
	plt.show()#Выводит график на экран.

def show_bar_graph_duration():
	"""Создаёт визуализацию  на основе данных о деятельности
		и соответствующих ей продуктивности и продолжительности."""
	
	names = ['работа','развлечения','обучение']
	dicts = []
	
	for i in names:
		dicts.append(get_data_duration(i))
		
	chart = pygal.Bar()
	chart.title = "Продуктивность\продолжительность"
	chart.title+= " по видам деятельности:"
	chart.x_title = "Продолжительность деятельности (кол-во часов)"
	chart.y_title = "Продуктивность"
	chart.x_labels = range(0,25)
	chart.add(names[0].title(), dicts[0].values())
	chart.add(names[1].title(), dicts[1].values())
	chart.add(names[2].title(), dicts[2].values())
	chart.force_uri_protocol = 'http'
	chart.render_to_file('bar_graph.svg')
	os.system('bar_graph.svg')#Открывает файл графика после создания.

def get_data_duration(activity):
	"""Обращается к БД и получает из неё данные для визуализации.
		Возвращает словарь типа {длительность:общая продуктивность}."""
	
	activity_dict = {}
	
	con = sqlite3.connect("biorhithms.db")
	cur = con.cursor()
	
	cur.execute(
		"""SELECT * FROM activities WHERE activity=:activity""",
		{"activity": activity})
	lines = cur.fetchall()
	
	#Получает данные из БД и заполняет ими словарь.
	#Высчитывает общую продуктивность для каждой длительности.
	for i in range(1,25):
		gen_eff = 0 #общая продуктивность.
		for line in lines:
			if line[4] == i:
				gen_eff += line[5]
		activity_dict[i]= gen_eff
	
	cur.close()
	con.close()
	
	return activity_dict
	
def get_daily_eff(activity):
	"""Обращается к БД и получает из неё данные для визуализации.
		Возвращает список: [общая продуктивность для каждого часа]."""
		
	con = sqlite3.connect("biorhithms.db")
	cur = con.cursor()
	
	values = []
	
	cur.execute(
		"""SELECT * FROM activities WHERE activity=:activity""",
		{"activity": activity})
	lines = cur.fetchall()
	
	#Получает данные из БД и заполняет ими список.
	#Высчитывает общую продуктивность для каждого часа(времени суток).
	for i in range(0,25):
		if i != 24:
			gen_eff = 0 #общая продуктивность.
			for line in lines:
				if line[3] == i:
					gen_eff += line[5]
			values.append(gen_eff)
		else: #24-й час(конец графика) определяется как 0:00.
			values.append(values[0])
		
	cur.close()
	con.close()		

	return values

def create_db():
	"""Функция для создания БД с необходимой таблицей."""
	
	con = sqlite3.connect("biorhithms.db")
	cur = con.cursor()

	sql = """
		CREATE TABLE activities (
			activity VAR_CHAR,
			time_start INTEGER,
			time_end INTEGER,
			mean_time INTEGER,
			duration INTEGER,
			efficiency INTEGER
		);
		"""

	cur.executescript(sql)
	con.commit()
	cur.close()
	con.close()
