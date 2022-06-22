## Requirements for Assignment-2
[Read the instruction](https://github.com/STIW3054-A211/e-sulam/blob/main/Assignment-2.md)

## Your Info:
1. Matric Number & Name & Photo & Phone Number
1. Other related info (if any)

| Photo                          |Matric Number  | Name                | Phone Number     |
| ------------------------------ | ------------- | --------------------|----------------- |
| ![272043](/images/272043.png)  | 272043        | Chong You Wah       | 013-6565126      |

## Introduction
In this assignment, i have create a telegram bot call PKOB_272043_BOT. This telegram bot was connect the database of wed application in assignment 1. It means this telegram will print out the detail that we store throught web application, but the user need to enter the ic number and phone number to get the telegram bot reply all the detail.
## Deployment Guide
After i done all the code that related with telegram bot, i have create a worker in the procfile and i open a new app in heroku which call pkob-272043-bot. After that, I start to run the heroku login, git remote, git add, git commit and git push in terminal to deploy the telegram bot to heroku. Lastly, i go to the resource of app pkob-272043-bot to turn on only the worker which is the telegram bot. Why i only turn on woker not web and worker is because if turn on both the telegram bot will awake only 30 min if the user no load to the website. Since we are connecting with assignment 1, so the web for this app is no important.
## Result/Output (Screenshot of the output)
1. /start
![272043](/images/start.png)

2. About PKOB
![272043](/images/about.png)

3. Website Link
![272043](/images/website.png)

4. About Victim
![272043](/images/victim.png)

5. Victim Detail
![272043](/images/detail.png)

## Youtube Presentation
https://youtu.be/t9IADHd_ODo

## List of Python packages (including the version) used for this system
Package               Version
--------------------- -----------
APScheduler           3.6.3

asgiref               3.4.1

cachetools            4.2.2

certifi               2021.10.8

dj-config-url         0.1.1

Django                3.2.8

gunicorn              20.1.0

pip                   21.3

psycopg2-binary       2.9.2

python-telegram-bot   13.9

pytz                  2021.3

pytz-deprecation-shim 0.1.0.post0

setuptools            57.4.0

six                   1.16.0

sqlparse              0.4.2

tornado               6.1

tzdata                2021.5

tzlocal               4.1

## References (Not less than 10)
1. Creating a Telegram Bot in Python 3.9 Tutorial (Fast & Easy). (2021, January 25). [Video]. YouTube.
       https://www.youtube.com/watch?v=PTAkiukJK7E
2. Python django telegram bot | Telegram bot using django | Telegram bot tutorial | [ telegram bot ]. (2021, June 18). [Video]. YouTube. 
https://www.youtube.com/watch?v=I3Kr46sRDK4&t=2412s
3. PostgreSQL Tutorial for Beginners 1 - Introduction to PostgreSQL. (2019, September 18). [Video]. YouTube. 
https://www.youtube.com/watch?v=FCa4HsG-hb4
4. Deploy PostgreSQL Database to Heroku. (2020, April 11). [Video]. YouTube. 
https://www.youtube.com/watch?v=ffEtxbbzCKQ
5. Heroku Postgres Connection | Django (3.0) Crash Course Tutorials (pt 24). (2020, January 28). [Video]. YouTube. 
https://www.youtube.com/watch?v=TFFtDLZnbSs
6. Pemmaiah, A. (2021, April 14). Building a Telegram Bot using Python. CodeSpeedy. 
https://www.codespeedy.com/building-a-telegram-bot-using-python/
7. How to Use Postgres Database In PyCharm ? (2019, December 8). [Video]. YouTube. 
https://www.youtube.com/watch?v=wGEZWXiEnNI
8. Connect to Heroku Postgres without SSL validation | PyCharm. (2021). PyCharm Help.
https://www.jetbrains.com/help/pycharm/how-to-connect-to-heroku-postgres.html
9. Burk, N. (2021, June 8). How to set up a free PostgreSQL database on Heroku [Video]. DEV Community. 
https://dev.to/prisma/how-to-setup-a-free-postgresql-database-on-heroku-1dc1
10. Telegram and Python - Custom Keyboard Buttons in Telegram Bot - Telegram Reply_Markup Keyboard. (2021, April 18). [Video]. YouTube. 
https://www.youtube.com/watch?v=MP8UrvWNK88
11. Python Telegram Bot with Custom Keyboard, Buttons, and Images. (2021, September 30). [Video]. YouTube. 
https://www.youtube.com/watch?v=5qzsKXxElQ4
