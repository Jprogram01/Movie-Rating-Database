# Overview




This project was done to familarize myself wiyh SQL. I wanted to be able to learn how to make queries and work with a database in all possible ways someone would need to. While I didn't do the most advanced queries, I think gained the foundational knowledge I need to easily pick up new techniques in the future.

{Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of how created the Relational Database.}

[Software Demo Video](https://www.loom.com/share/6fc0db3469ae483994b9e22911617a0e)

# Relational Database

SQL, specifically through sqlite.

I created a table for Movies, which had the structure of a UniqueId for a row, Movie Title, Movie Rating, Watch Date, Movie Theme. I also created another table through a dataset of the top 1000 IMDB movies. All the different columns are Poster_Link,Series_Title,Released_Year,Certificate,Runtime,Genre,IMDB_Rating,Overview,Meta_score,Director,Star1,Star2,Star3,Star4,No_of_Votes,Gross

# Development Environment

VS Code

{Describe the programming language that you used and any libraries.}
Python, pandas, and sqlite3
# Useful Websites

{Make a list of websites that you found helpful in this project}

- [Sqlite Documentation](https://docs.python.org/3.8/library/sqlite3.html)
- [Kaggle](https://www.kaggle.com/datasets)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}

- Error handling for different results of preforming a query (Item already exist, item not found, wrong values, ect)
- Do data analysis on the data created, allow users to find rating average or a common word found throughout themes.
- Expand the number of columns that are in the movies table. Allow users to input genre or a small review.