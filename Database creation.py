import sqlite3 as SQL
import pandas as pd

def input_movie(con):
    cursor = con.cursor()
    new_movie = input("What new movie did you watch? ")
    rating = input("What would you rate it out of five? ")
    if float(rating) > 5 or float(rating) < 0:
        print("Invalid Value")
        rating = input("What would you rate it out of five")
    date_watched = input("When was the date when you watch it. Format it in the MM/DD/YYYY format ")
    theme = input("What was the theme of the film? Leave blank if no theme insights ")
    data_input = (new_movie, rating, date_watched, theme)
    cursor.execute('INSERT INTO movies_list (movie_title, rating, date_watched, theme) VALUES (?, ?, ?, ?);', data_input)
    con.commit()
    cursor.close()

def update_movie(con):
    cursor = con.cursor()
    movie = input("What new movie did you want to update? ")
    column_picked = False

    while not column_picked:
        column_to_update = input("What variable would you like to update? Select between \nmovie\nrating\ndate_watched\ntheme\n")
        if column_to_update not in ["movie", "rating", "date_watched", "theme"]:
            print("Invalid variable picked")
        else:
            column_picked = True
    updated_info = input(f"You wanted to update the {column_to_update} variable in the {movie} row. Enter information now ")
    query = f"""
    UPDATE movies_list
    SET {column_to_update} = '{updated_info}'
    WHERE movie_title = '{movie}'
    """
    cursor.execute(query)
    con.commit()
    cursor.close()

def delete_movie(con):
    cursor = con.cursor()
    movie = input("What new movie did you want to delete? ")
    column_picked = False

    query = f"""
    DELETE FROM movies_list
    WHERE movie_title = '{movie}'
    """
    cursor.execute(query)
    con.commit()
    cursor.close()

def show_whole_list(con):
    query = """
    SELECT * FROM movies_list
    """
    movie_list = pd.read_sql_query(query, con)
    print(movie_list)
def check_ranking(con):
    movie = input("What movie did you want to check the ranking of? ")

    cursor = con.cursor()
    query = f"SELECT 1 FROM movies_data WHERE title = ? LIMIT 1;"
    cursor.execute(query, (movie,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        query = f"""
            SELECT
                movies_list.movie_title,
                movies_data.title AS movie_title_data,
                movies_data.ROWID AS movie_ranking
            FROM
                movies_list
            JOIN
                movies_data ON movies_list.movie_title = movies_data.title
            WHERE
                movies_list.movie_title = '{movie}';
            """
        IMDBmovie = pd.read_sql_query(query, con)
        ranking = int(IMDBmovie["movie_ranking"])
        print(f"{movie}'s ranking in IMBD is {ranking}")
    else:
        print(f"{movie} not found in top 1000 IMDB list!")

con = SQL.connect("movies.db")
input_movie_checker = None
while input_movie_checker != "6":
    input_movie_checker = input("""\nWhat do you want to do? Enter a number:
                            \n1.Enter new movie
                            \n2.Update previous entry
                            \n3.Delete entry
                            \n4.See movie list
                            \n5.Check movie ranking on IMDB
                            \n6.Stop 
                            \n""")
    if input_movie_checker == "1":
        input_movie(con)
    elif input_movie_checker == "2":
        update_movie(con)
    elif input_movie_checker == "3":
        delete_movie(con)
    elif input_movie_checker == "4":
        show_whole_list(con)
    elif input_movie_checker == "5":
        check_ranking(con)
    elif input_movie_checker == "6":
        print("Movie time over!!!")


