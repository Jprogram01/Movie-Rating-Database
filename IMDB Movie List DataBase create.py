import sqlite3 as SQL
import pandas as pd
csv_source = 'imdb_top_1000.csv'
connection = SQL.connect("movies.db")
minion = connection.cursor()
# Creating the table.
SQL_command = """
    CREATE TABLE
        movies_data
        (
            title TEXT NOT NULL,
            release_year TEXT,
            certificate TEXT,
            runtime INTEGER,
            imdb_rating REAL NOT NULL,
            num_votes INTEGER,
            gross REAL
        );
"""
#minion.execute(SQL_command)
# Checking that the table was created.
#tables = minion.execute("SELECT name FROM sqlite_master")
#tables.fetchall()
data = pd.read_csv(csv_source, nrows=3)
print(data)
SQL_command = """
    INSERT INTO
        movies_data
    VALUES
        (?, ?, ?, ?, ?, ?, ?);
"""

# Iterate the csv by chunks of 100.
chunksize = 100
for chunk in pd.read_csv(csv_source, chunksize=chunksize):
    records = []
    for index, row in chunk.iterrows():
        record = (
            row['Series_Title'],
            row['Released_Year'],
            row['Certificate'],
            int(row['Runtime'].split()[0]),
            row['IMDB_Rating'],
            row['No_of_Votes'],
            row['Gross']
        )
        records.append(record)
    minion.executemany(SQL_command, records)
    connection.commit()
print('Database Update Complete!')
# Check the number of records in the table.
SQL_command = """
    SELECT
        COUNT(*)
    FROM
        movies_data;
"""
minion.execute(SQL_command)
print(minion.fetchall())
# Check the first 9 titles against the CSV file.
SQL_command = """
    SELECT
        rowid,
        title
    FROM
        movies_data
    WHERE
        rowid < 10;
"""
minion.execute(SQL_command)
data = pd.read_csv(csv_source, nrows=9)
print(f'         SQL DATA        |         CSV FILE         ')
for i in range(0, 9):
    sql_data = minion.fetchone()
    print(f'{sql_data[0]}, {sql_data[1][:20]} {data["Series_Title"][i][:20]:>24}')

print(pd.read_sql_query("SELECT * FROM movies_data", connection))

connection.close()