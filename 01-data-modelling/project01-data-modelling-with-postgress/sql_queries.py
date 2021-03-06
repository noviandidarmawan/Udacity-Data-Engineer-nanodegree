# DROP TABLES

songplay_table_drop = """DROP TABLE IF EXISTS songplays """
user_table_drop = """DROP TABLE IF EXISTS "users" """
song_table_drop = """DROP TABLE IF EXISTS "songs" """
artist_table_drop = """DROP TABLE IF EXISTS "artists" """
time_table_drop = """DROP TABLE IF EXISTS "times" """

# CREATE TABLES


songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS "songplays" (
    songplay_id SERIAL PRIMARY KEY, 
    start_time TIMESTAMP NULL, 
    user_id varchar(140) NULL, 
    level varchar(140) NULL, 
    song_id varchar(140) NULL, 
    artist_id varchar(140) NULL, 
    session_id varchar(140) NULL, 
    location text NULL, 
    user_agent text NULL);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS "users" (
    user_id int PRIMARY KEY, 
    first_name varchar(140) NULL, 
    last_name varchar(140) NULL, 
    gender varchar(140) NULL, 
    level varchar(140) NULL
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS "songs" (
    song_id varchar(140) PRIMARY KEY, 
    title varchar(140) NULL, 
    artist_id varchar(140) NOT NULL, 
    year int NULL, 
    duration float NULL
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS "artists" (
    artist_id varchar(140) PRIMARY KEY, 
    name varchar(140) NULL, 
    location varchar(140) NULL, 
    latitude numeric NULL, 
    longitude numeric NULL
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS "times" (
    start_time timestamp, 
    hour int, 
    day int, 
    week int, 
    month int, 
    year int, 
    weekday int
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO "users" (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO NOTHING
""")

song_table_insert = ("""
INSERT INTO "songs" (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO "artists" (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING
""")


time_table_insert = ("""
INSERT INTO "times" (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
SELECT  songs.song_id, artists.artist_id FROM artists JOIN songs ON artists.artist_id = songs.artist_id
WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]