# Reddit Bulk Messager

*Messages users that have opted-in to a "Get notified of new posts"-type newsletter.*
*Misuse of this script will probably lead to your account being banned.*

# Setup instructions
*Instructions are for Windows. I've never done this on any other OS so I cannot help, sorry.*

- Download Python latest - https://www.python.org/downloads/
- Add python to environment

- Run *pip install praw* in command prompt. 

- Download this script by clicking on the green *Clone or Download* button, followed by *Download ZIP*. After it downloads, extract the zip.

- Open your favvourite IDE 

- When the window opens, go to *File > Open* and select the *config.py* file that you just extracted.

- Next, to create a bot account on Reddit, create a new Reddit account like you normally would. After it is created, go to *preferences > apps > create new app*. Make sure you select *script*. Call the bot whatever you like, and in the *redirect uri* box, enter *http://localhost:8080*. Then click create. You can also do this with your main account if you like.

- Go back to IDLE and follow the instructions that I commented in for you in the *config.py* file. (Everything with a hash symbol before it. The text should be red.)

- After you entered in all of the credentials for your bot, save *config.py*, close it, and open *Opt-in Comment Finder.py*. You can leave this open 24/7 if you like, or you can open it intermittently throughout the day. If this script does not run, then no names will get added to the database. If you want to send a message to your subscribed users, open *Send Message.py* and follow the instructions on screen.

If someone wishes to be removed from the messaging list, download DB Browser for SQLite here - http://sqlitebrowser.org/

Once downloaded and installed, open up *Subscriber List.db* using DB Browser.

