import praw
import sqlite3
import os
import time
import config

messageFooter = ('\n\n---\n\n^This ^message ^was ^sent ^by ^a ^script. ^If ^there ^is ^an ^issue, ^please ^message ^/u/{}'
                 .format(config.main_account))


def connect_to_database():  # Connects to the database
    conn = sqlite3.connect('Subscriber List.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS Subscribers(Username)')
    conn.commit()
    return c, conn


def connect_to_reddit():  # Connects to Reddit account
    reddit = praw.Reddit(username=config.username, password=config.password, client_id=config.client_id,
                         client_secret=config.client_secret, user_agent=config.user_agent)
    return reddit


# Gets a list of subscribed users that it needs to message
def get_subscribed_users(c, conn):
    subscribers = set()
    c.execute('SELECT Username FROM Subscribers')
    for username in c.fetchall():
        subscribers.add(username[0])
    return subscribers


def get_message_info():  # Takes the Message Subject and Message Body as input from the user
    while True:
        os.system('CLS')
        print('You are currently unable to add new paragraphs to your message, so keep that in mind.')
        print('Also, if you make a mistake, you will need to write the whole thing again, so check before you press enter.')
        print('You will be prompted for confirmation after you enter your Message Subject and Message Body.\n')
        message_subject = 'Make better friends!'
        message_body = 'Hey, I saw your post on r/privacy, and I thought you might be interested in this! We are building a social media incentivized around your closest relationships, not your attention. It is a communication first social media for your closest friends only (limit of 25 friends). Check it out, I would love to get your feedback! https://joinoval.com'
        os.system('CLS')
        print('Your message subject:\n"{}"\n\nYour message body:\n"{}"\n\n'.format(
            message_subject, message_body))
        confirmation = input('Is this correct? Y/N > ').lower()
        if confirmation == 'y':
            return message_subject, message_body
        elif confirmation == 'n':
            continue


def deleteUser(user):
    conn = sqlite3.connect('Subscriber List.db')
    c = conn.cursor()
    c.execute('DELETE FROM subscribers WHERE username = ?', (user,))
    conn.commit()


# Sends the messages to the subscribed users
def send_message(reddit, message_subject, message_body, subscribers):
    i = 0
    for user in subscribers:
        i += 1
        try:
            if(i % 9 == 0):
                print('Sleeping 4 mins')
                time.sleep(240)
            else:
                print(i, user)
                reddit.redditor(user).message(message_subject, message_body)
                deleteUser(user)

        except Exception as e:
            print('System warning - '+str(e))
            pass


def main():
    c, conn = connect_to_database()
    reddit = connect_to_reddit()
    message_subject, message_body = get_message_info()
    subscribers = get_subscribed_users(c, conn)
    send_message(reddit, message_subject, message_body, subscribers)
    print('System Message - Messages have successfully sent. Closing in 5 seconds.')
    time.sleep(5)


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print('Fatal error - '+str(e))
            print('System Message - Sleeping for 1 minute.')
            time.sleep(60)
