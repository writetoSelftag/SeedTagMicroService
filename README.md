# MicroService on Python

## Previous requirements:
>`Docker` `Python 3.9` `Postman - external app`

## How to execute the service:
You have 2 option for run the server. 

First option is using Docker. You only need to install docker.
        
>1. `docker-compose up`
>2. `docker-compose exec backend sh`
>3. Now we are inside docker console
>4. Try `python manage.py migration` if doesn't detect the migrations try with:
>   1. `python manage.py makemigrations radars`

Second option is using python directly. You need to install Python 3.9 and pip3

After that, you need to install requirements with:

>pip3 install -r requirements.txt

And then, launch the server
>`python3 manage.py runserver 0.0.0.0:8888`
        
## WITH DATABASE
The solution allows saving the inputs and the result in the database.
For that purpose, migrations must be launched first.

For docker:
>docker-compose exec backend sh

And inside docker console launch the command:
> python manage.py migrate

For python server, open terminal and launch this command in root of the project:
> python3 manage.py migrate        
        
In `./src/radars/views.py ` you need to uncomment line 22.

>#serializer.save()

And last but not least, go to `./app/settings.py `, line 68, and uncomment all that is inside DATABASES constant:

>DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'microservice',
       'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'db',
        'PORT': '3306'
     }
}

Otherwise, the solution can work without database.

## How to check is running:

http://localhost:8888

## Why port :8888
The tests.sh checks CURLS on that port, so the Docker solution is binded to this port.

## Overview
Purpose of this challenge is to enable you to demonstrate your proficiency in solving problems
using software engineering tools and processes.

## Specification

 Read the PDF


### Input:

Example: 
>{
 "protocols":["avoid-mech"],
  "scan":[
     {
        "coordinates": {"x":0,"y":40},
        "enemies": {
               "type":"soldier",
               "number":10
         }
     }
  ]
 }

### Output:

> {"x":0,"y":40}

# Testing
If you followed the instructions pytest should have been installed with 

>pip install -r requirements.txt

So, you need to move to `./tests` and launch `pytest -v` in terminal

In case you are using the Docker version 

>docker-compose exec backend sh

And inside docker console launch the command:
>cd tests/
>pytest -v