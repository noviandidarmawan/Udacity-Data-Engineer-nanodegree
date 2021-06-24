# Project data modeling with PostgreeSQL

This project is the first project of the Data Engineer Nanodegree in Udacity. 

### Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new 
music streaming app. The analytics team is particularly interested in understanding what songs users are listening 
to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user 
activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play 
analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. 
You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from 
Sparkify and compare your results with their expected results.

### Project Description
In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using 
Python. To complete the project, you will need to define fact and dimension tables for a star schema for a 
particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories i
nto these tables in Postgres using Python and SQL.

### Data Model
Data Model in this project consists of Fact Table and Dimensions Table

#### Fact Table
**songplays**  - records in log data associated with song plays i.e. records with page NextSong
- songplay_id (INT) SERIAL PRIMARY KEY: Generated ID of each user song play
- start_time (TIMESTAMP): Timestamp of beginning of user activity
- user_id (INT): ID of each user
- level (VARCHAR): user level {free|paid}
- song_id (VARCHAR): ID of song played
- artist_id (VARCHAR): ID of artist which song played
- session_id (INT): ID of user Session 
- location (TEXT): user location
- user_agent (TEXT): agent used by user

#### Dimension Table
**users** - users in the app
- user_id (INT) PRIMARY KEY NOT NULL: ID of user
- first_name (VARCHAR): first name of user
- last_name (VARCHAR): last name of user
- gender (VARCHAR): gender of user
- level (VARCHAR): user level

**songs** - songs in music database
- song_id (INT) PRIMARY KEY NOT NULL: ID of song
- title (VARCHAR): title of song
- artist_id (VARCHAR) NOT NULL: ID of artist of the song
- year (INT): year of song released
- duration (FLOAT): duration of song

**artists** - artists in music database
- artist_id (INT) PRIMARY KEY NOT NULL: ID of artist
- name (VARCHAR): name of artist
- location (VARCHAR): location of artist
- lattitude (FLOAT): Lattitude location of artist
- longitude (FLOAT): Longitude location of artist

**time** - timestamps of records in songplays broken down into specific units
- start_time (DATE) PRIMARY KEY: Timestamp of row
- hour (INT): Hour from start_time
- day (INT): Day from start_time
- week (INT): Week of year from start_time
- month (INT): Month from start_time 
- year (INT): Year from start_time
- weekday (TEXT): Name of week day related to start_time

### File Structure

1. **data** : source file of log and song data.
2. **sql_queries.py** contains all sql queries to be called in several .py files.
3. **create_tables.py** drops and creates tables. You run this file to reset your tables before each time you run your ETL scripts.
4. **test.ipynb** displays the first few rows of each table to let you check your database.
5. **etl.ipynb** reads and processes a single file from song_data and log_data and loads the data into your tables. 
6. **etl.py** reads and processes files from song_data and log_data and loads them into your tables. 
7. **README.md** current file, provides discussion on my project.


### Project Flow

**Create Sparkifydb database**
1. run 'create_tables.py' by writing "python create_tables.py" in terminal after 'sql_queries.py' is filled
2. run 2 first rows in 'test.ipynb' to see the db has been created or not.

**make ETL process**
1. make each step on ETL process in 'etl.ipynb'
2. check 'test.ipynb' to see the data is successfully created or not into db.
3. build a function from etl.ipynb' to 'etl.py'
4. run 'etl.py' in terminal 