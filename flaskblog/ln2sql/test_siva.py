import os
import re
from ln2sql.ln2sql import Ln2sql
BASE_PATH = os.path.dirname(os.path.dirname(__file__))  # Project directory.
DATABASE_PATH = os.path.join(BASE_PATH, 'ln2sql/database_store/')
LANG_PATH = os.path.join(BASE_PATH, 'ln2sql/lang_store/english.csv')
THESAURUS_PATH = os.path.join(BASE_PATH, 'ln2sql/thesaurus_store/')
input_nl
database_filename=''
database_file_path =DATABASE_PATH+database_filename

ln2sql = Ln2sql(database_file_path,LANG_PATH)
query = ln2sql.get_query(input_nl)
print(query)
