import unittest
import flaskblog.routes as route
class TestDatabase(unittest.TestCase):
	database_file = 'database_store/'+'city.sql'
	queryLoader = route.Ln2sql(database_file,'lang_store/english.csv')
	database_object = route.Data_object()
	database_object.load(database_file)
	def test_simpleQuery(self):
		sql=self.queryLoader.get_query('What is the number of the city in this database?')
		self.assertEqual(sql,'\nSELECT COUNT(*)\nFROM city;\n')

	def test_selectQueries(self):
		sql=self.queryLoader.get_query('List me the info of city table')
		self.assertEqual(sql,'\nSELECT *\nFROM city;\n')

	def test_countQueries(self):
		sql=self.queryLoader.get_query('What is the number of the city in this database?')
		self.assertEqual(sql,'\nSELECT COUNT(*)\nFROM city;\n')


	def test_oneColumnQueries(self):
		sql=self.queryLoader.get_query('Tell me all id from city')
		self.assertEqual(sql,'\nSELECT city.id\nFROM city;\n')


	def test_multiColumnQueries(self):
		sql=self.queryLoader.get_query('List all name and score of all emp')
		self.assertEqual(sql,'\nSELECT emp.name, emp.score\nFROM emp;\n')

		
	def test_one_condition_queries(self):
		sql=self.queryLoader.get_query('What is the emp with the name is rupinder ?')
		self.assertEqual(sql,"\nSELECT *\nFROM emp\nWHERE emp.name = 'rupinder';\n")




if __name__ =='__main__':
	unittest.main()
	