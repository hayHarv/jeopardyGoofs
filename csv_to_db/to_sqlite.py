import pandas as pd
import sqlite3
import os


csv_dir = '/home/haydenh/repos/projects/jeopardy/Data/jeopardy-database'
data_dir = '/home/haydenh/repos/projects/jeopardy/Data'
sqlite_file = '/home/haydenh/repos/projects/jeopardy/Data/jeopardy.sqlite'

conn = sqlite3.connect(sqlite_file)

def create_db(conn, csv_dir):

    for file in os.listdir(csv_dir):
        table_name = str(file.split('.')[0])
        df = pd.read_csv(csv_dir + "/" + file)
        df.to_sql(table_name, conn)


if __name__=="__main__":
    create_db(conn, csv_dir)



