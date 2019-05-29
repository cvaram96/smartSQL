from ln2sql.ln2sql import Ln2sql
queryLoader = Ln2sql('database_store/city.sql','lang_store/english.csv','thesaurus_store/th_english.dat')
print(queryLoader.get_query('what is the id of the city which cityName is chulipuram'))