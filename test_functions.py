"""Набор тестов для модуля functions программы Biorhithms."""

import unittest
from functions import *

class GetDataTestCase(unittest.TestCase):
	"""Тесты для функций get_data_duration() и get_daily_eff()."""
	
	def setUp(self):
		"""Предустановки для каждого теста. Заполняет БД."""
		
		test_values = ('работа', 1, 1, 1, 1, 1)
		
		con = sqlite3.connect("biorhithms.db")
		cur = con.cursor()
		with con:
			for i in range(5):
				cur.execute("""INSERT INTO activities 
					VALUES(?,?,?,?,?,?)""", test_values)					
		
	def  test_data_duration_equal(self):
		"""Тестирует чтение из БД функцией get_data_duration().
			Проверяет правильность вычислений функции."""
		
		test_dict = get_data_duration('работа')
		self.assertEqual(test_dict[1], 5)
		
		
	def  test_data_eff_equal(self):
		"""Тестирует чтение из БД функцией get_daily_eff().
			Проверяет правильность вычислений функции."""
						
		test_list = get_daily_eff('работа')
		self.assertEqual(test_list[1], 10)#Метод setUp итерирует 2 раза.


unittest.main()
