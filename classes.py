"""Набор классов для программы Biorhithms."""

import time
import sqlite3
import statistics as st

class Activity():
	"""Объект деятельности. Полученные данные сохраняются в DB."""
	
	def __init__(self, activity=''):
		
		self.activity = activity
		self.time_start = 0
		self.time_end = 0
		self.mean_time = 0
		self.duration = 0
		self.efficiency = 0#Получает данные извне через функции GUI.
		
	def time_point_start(self):
		"""Определяет начало периода."""
		
		self.time_start = time.localtime()[3]
		
		
	def time_point_end(self):
		"""Определяет конец периода."""
		
		self.time_end = time.localtime()[3]
		
	def get_mean_time(self):
		"""Вычисляет среднее время периода."""
		
		#Форматируем время с учётом того, что сутки
		#заканчиваются после 23:59.
		if self.time_end > self.time_start:
			self.mean_time = int(st.mean(
				[self.time_start, self.time_end]))
		elif self.time_end < self.time_start:
			value = int((24 - self.time_start + self.time_end)//2)
			value+= self.time_start
			if value > 24:
				self.mean_time = value - 24
			else:
				self.mean_time = value
		elif self.time_end == self.time_start:
			self.mean_time = 1		
			
	def get_duration(self):
		"""Вычисляет продолжительность деятельности."""
	
		#Форматируем время с учётом того, что сутки
		#заканчиваются после 23:59.	
		if self.time_end > self.time_start:
			self.duration = self.time_end - self.time_start
		elif self.time_end < self.time_start:
			self.duration = 24 - self.time_start + self.time_end
		elif self.time_end == self.time_start:
			self.duration = 1
		
	def update_db(self):
		"""Добавляет полученные данные объекта класса в БД."""
		
		#Кортеж полученных данных объекта.
		data = (
			self.activity, self.time_start, self.time_end,
			self.mean_time, self.duration, self.efficiency
			)
		
		con = sqlite3.connect("biorhithms.db")
		cur = con.cursor()
		cur.execute("""
			INSERT INTO activities VALUES(?,?,?,?,?,?)""", data)
		con.commit()
		cur.close()
		con.close()
