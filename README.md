# Little Lemon Capstone Project for Meta Backend Developer Professional Certificate

## Summary
This is the capstone project for the Meta Backend Developer Professional Certificate Course that is hosted on Coursera.

## What I have learnt
This has been an exciting course in which I managed to apply the knowledge I have gained throughout the course.
Topics that I have made use of in this project include:
- Data modelling
- Connecting to a MySQL database
- Django views
- URL routing
- Unit testing

## How to run
To run this project you should do the following:
1. Download the source code to your local machine by running `git clone https://github.com/jerome-simms/LittleLemon.git`
2. Since this project uses the venv module, create a virtual environment using the following command: `python -m venv venv` and then activate it by running `.\venv\Scripts\activate` if on windows or `source ./venv/bin/activate` if on a unix-like operating system
3. Install all the relevant dependencies using the command `pip install -r requirements.txt`
4. Edit the `.env.example` file to include the relavant values to connect to your local MySQL database and rename the file to be just `.env`
5. Make the migrations by running `python manage.py makemigrations`
6. Migrate the data using `python manage.py migrate`
7. Run the development server by running `python manage.py runserver` from the project's root directory
8. You may create example users, menu items, and booking objects to test this project

## Routes to test
Please navigate to the following routes:

**Menu Item Routes**
- [localhost:8000/restaurant/menu/]() - This route should allow you to get all menu items and allow the creation of a new menu item
- [localhost:8000/restaurant/menu/{menuId}]() - This route allows retrieval, updation, and deletion of a menu item with the id of {menuId} 

**Booking Routes**
- [localhost:8000/restaurant/booking/tables/]() - This route should allow you to get all menu items and allow the creation of a new booking object
- [localhost:8000/restaurant/booking/tables/{Id}]() - This route allows retrieval, updation, and deletion of a booking objectt with the id of {idId} 
