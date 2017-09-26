import sqlite3
import os
import numpy as np

data_path = './Data/jeopardy.sqlite'
conn = sqlite3.connect(data_path)
c = conn.cursor()
rows = c.execute('select count(*) from questions where value>0;').fetchone()[0]

def get_question(rows, sqlite_cursor):
    rand_row = np.random.randint(rows, size=1)[0]
    query = '''select 
    category, 
    value, 
    question_text,
    answer
    from questions
    where rowid={}'''.format(rand_row)
    result = sqlite_cursor.execute(query).fetchone()
    category = result[0]
    value = result[1]
    question = result[2]
    answer = result[3]
    # print for debug
    print('{} {} {} {}'.format(category, value, question, answer))

