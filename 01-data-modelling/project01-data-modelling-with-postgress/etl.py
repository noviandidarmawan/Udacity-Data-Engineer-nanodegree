import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
    - Function for process song file 
    - input song data, and artist data to sparkifydb
    
    Params:
    cur = db cursor
    filepath = song file path
    """
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = df[['song_id','title','artist_id','year','duration']]
    song_data = song_data.values[0].tolist()
    
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df[['artist_id','artist_name','artist_location','artist_latitude','artist_longitude']]
    artist_data = artist_data.values[0].tolist()
    
    cur.execute(artist_table_insert, artist_data)

def process_log_file(cur, filepath):
    """
    - process log file
    - input user data, time data, and songplay data to sparkifydb
    
    Params:
    cur = db cursor
    filepath = log file path
    """
    # open log file
    df = pd.read_json(filepath, lines=True)
    
    # convert timestamp column to datetime
    df['ts'] = pd.to_datetime(df['ts'], unit='ms')

    # filter by NextSong action
    df = df[df['page'] == 'NextSong']
    
    t = df['ts']
    
    #define each component of time
    hour = t.dt.hour
    day = t.dt.day
    week_of_year = t.dt.weekofyear
    month = t.dt.month
    year = t.dt.year
    weekday = t.dt.weekday

    # insert time data records
    time_data = list(zip(t,hour,day, week_of_year, month, year, weekday))
    column_labels = ['timestamp', 'hour', 'day', 'week', 'month', 'year', 'weekday']
    time_df = pd.DataFrame(time_data, columns=column_labels)
    
    time_tuples = [tuple(x) for x in time_df.values]  #convert df to list of tuples to suit the cur.executemany params       
    cur.executemany(time_table_insert, time_tuples) # insert bulk of data at once

    # load user table
    user_df = df[['userId','firstName','lastName','gender','level']].drop_duplicates()

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    songplay_tuples = []
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.length)
        songplay_tuples.append(songplay_data)

    cur.executemany(songplay_table_insert, songplay_tuples) # insert bulk of data at once
        


def process_data(cur, conn, filepath, func):
    """
    - load all file in 'data' directory
    - run function 'process_song_file' and 'process_log_file'
    
    Params:
    cur = db cursor
    conn = db connection
    filepath = file that will be processed
    func = function that will be processed inside this function
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()