import praw
import config
import sqlite3
import time

def connect_to_database(): # Connects to the Database
    conn = sqlite3.connect('Subscriber List.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS Subscribers(Username)')
    conn.commit()
    c.execute('CREATE TABLE IF NOT EXISTS OldComments(Comment)')
    return c, conn

def connect_to_reddit(): # Connects to Reddit account
    reddit = praw.Reddit(username=config.username, password=config.password, client_id=config.client_id,
                            client_secret=config.client_secret, user_agent=config.user_agent)
    return reddit
    
def add_user_to_database(c, conn, username): # Adds user to database
    c.execute('INSERT INTO Subscribers VALUES(?)',(username,))
    conn.commit()
    print('Added new user to subscriber list.')

if __name__ == '__main__':
    while True:
        try:
            c, conn = connect_to_database()
            subject = "Check"
            message = "Hi"
            reddit = connect_to_reddit()
            for comment in reddit.subreddit("neovim").comments(limit=100):
                print(comment.author)
                add_user_to_database(c, conn, comment.author.name)

        except Exception as e:
            print('Critical error - '+str(e))
            print('System Message - Sleeping for 1 minute.')
            time.sleep(60)
