# NewsLetter

# Steps to setup the project. 

# Require versions 
Python 3.6+ 
Django 3.1+

# Used Versions
Python 3.8.1
Django 3.2.4

# Step 1:- 
Create virtual environment with python 3.6+ versions

# Step 2:- 
Unzip project folder.

# Step 3:- 
Install requirements using given command **pip install -r requirements.txt** 

# Step 4:- 
Setup environment variables as per your configuration into the following path **newsletter -> .env**

# Step 5:- 
Prepare database using below command **python manage.py migrate**

# Step 6:- 
Create super user to access the admin using **python manage.py createsuperuser** command and fill information accordingly. 

# Step 7:- 
To run celery perform below command with the **redis-server**
Django celery command **celery -A newsletter worker --beat --scheduler django --loglevel=info**

# Project Flow:- 
It will fetch the data from the api mentioned into the .env file and execute management command located
at news -> management -> commands -> news_scheduler. 

After its execution, it will send an email to all database users by their preferences.

# Introduction of each module 

1) Fixtures :- 
It will load static records into the database. Please run the below command. **python manage.py loaddata --format json fixtures/user.json** to load static user data and **python manage.py loaddata --format json fixtures/userpreference.json** to load user preferences. 

2) news:- 

This module represents the records and information regarding to the news. 

Here is the use of specific files.

management -> commands 
news_scheduler :- fetch API and store that data into the database using bulk create. 

admin.py -> Bind news model and visualize it into the admin dashboard.
models.py -> Use to create models. 
signals.py -> It will trigger few code chunk while sender will perform specific actions. 
tasks.py -> This file is responsible to fetch binded scheduler task. 
utils.py -> This file is generated for code reusability. 
views.py -> Business logic for the news authenticity. 

Templates -> news 
email_template:- 
the template which will represent all the latest news, for all users by their preference choices. 

3) userpreference:- 

This module stores the user preferences. and responsible for the fetch user preference while needed. 

# Sudo code and mutiple_ways.txt is covered the below scenarios:-
I. A single API request is used to trigger operations on many items in a loop, that has 2 potential problems:
 The request takes a long time to complete, so the user may suspect the operation has failed, and may retry, running multiple parallel jobs and wasting server resources.
 Due to web server request time out of 60 seconds, the user will not get their response at all if the job takes too long.

II. Advise how we can resolve these issues:
Protect the server against the user submitting parallel requests, both on the server side, but also to provide the user with partial progress updates so they will get immediate and regular feedback that the task is progressing, increasing user confidence in the operation.
Ensure that the operation will continue and complete beyond the web server 60 seconds timeout.
 

