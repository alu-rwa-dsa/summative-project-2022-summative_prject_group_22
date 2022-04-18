# Final-Jan-April-2022

# About

This programme is Queue management System software that systematically records the customers in first come bases and assigns them priority of services in order of who came first .
With this software in business places , customers do not have to physically wait in long lines and wait idly to get services but rather they have free time while they wait and they can look around the business premises busting customer loyalty and sales .
This project has a user friendly environment thatshows the tellers available and the approximate time on the waiting line.

# OutStanding Trait

This software saves the number a teller in the business premises a teller serves hence improving the efficiency because teller will be keen on saving time and serving the customers efficiently .
This functionality solves our problem and customers services is efficient and is saved!

# Requirments

We used Django tool to create a user friendly GUI for our program.
The program has also intergrated JavaScript to make it a responsive site.
It is Deployed on Heroku App and it can be access us this link http://customer_queue.herokuapp.com
To run this program local on your computer you must have python intepreter if you don't have it you should download and install it from here: https://www.jetbrains.com/pycharm/download/#section=windows and Running environment. then go ahead install the following extentions on the following order
```
python -m venv venv

cd venv

.\Scripts\activate
cd ..

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

```


### To create a user. Open new shell at root
```
python manage.py createsuperuser
```
### fill the info

Then go to http://localhost:8000/admin

### For testing please run the command:

```
py manage.py test
```
