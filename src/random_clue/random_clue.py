#TODO filter final jeopardy
#TODO make dem functions better
#TODO add prompt for # of questions (and include final jeopardy?)
#TODO add timer

import sqlite3
import os
import numpy as np

data_path = '/home/haydenh/repos/projects/jeopardy/Data/jeopardy.sqlite'
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
    return category, value, question, answer


def play(rows, sqlite_cursor):
    cat, val, q, ans = get_question(rows, sqlite_cursor)
    user ='y' 
    if user == 'y':
        print("Category: {}".format(cat))
        print("Value: ${}".format(val))
        print("{}".format(q))
        user = input("Type [a] if you're ready for the answer: ")
        if user == 'a':
            print(ans)
            return ""

def keep_playing(rows, sqlite_cursor):
    play(rows, sqlite_cursor)
    user = input("play another? [y/n] ")
    if user == 'y':
       keep_playing(rows, sqlite_cursor)
    else:
        return ""

if __name__=="__main__":
    keep_playing(rows, c)
