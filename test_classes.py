"""Набор тестов для модуля classes программы Biorhithms."""

import unittest
from classes import *

class TestActivity(unittest.TestCase):
	"""Тесты для класса Activity."""
	
	def setUp(self):
		self.act = Activity('работа')
	
	def test_get_mean_time(self):
		"""Тестирует метод get_mean_time()."""
		#Тестирует четыре условия.
		self.act.time_point_start()
		self.act.time_point_end()
		self.act.get_mean_time()
		self.assertEqual(self.act.mean_time, 1)
		
		self.act.time_end = 10
		self.act.time_start = 4
		self.act.get_mean_time()
		self.assertEqual(self.act.mean_time, 7)
		
		self.act.time_end = 10
		self.act.time_start = 20
		self.act.get_mean_time()
		self.assertEqual(self.act.mean_time, 3)		

		self.act.time_end = 2
		self.act.time_start = 20
		self.act.get_mean_time()
		self.assertEqual(self.act.mean_time, 23)
		
	def test_duration_time(self):
		"""Тестирует метод get_duration()."""
		#Тестирует три условия.
		self.act.time_point_start()
		self.act.time_point_end()
		self.act.get_duration()
		self.assertEqual(self.act.duration, 1)
		
		self.act.time_end = 10
		self.act.time_start = 4
		self.act.get_duration()
		self.assertEqual(self.act.duration, 6)
		
		self.act.time_end = 10
		self.act.time_start = 20
		self.act.get_duration()
		self.assertEqual(self.act.duration, 14)
		
	def test_update_db(self):
		"""Тестирует метод update_db()."""
		#Случайные данные для объекта.
		self.act.time_start = 1
		self.act.time_end = 2
		self.act.mean_time = 3
		self.act.duration = 4
		self.act.efficiency = 5
		
		#Тестирует заполнение базы данных.
		self.act.update_db()
		
		con = sqlite3.connect("biorhithms.db")
		cur = con.cursor()
		cur.execute("""SELECT * FROM activities WHERE
			activity:=activity""", {"activity": self.act.activity})
		row = cur.fetchone()
		cur.close()
		con.close()	
		self.assertEqual(row, ('работа', 1, 2, 3, 4, 5)
		
unittest.main()
