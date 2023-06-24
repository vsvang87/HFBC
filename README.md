A responsive full-stack website for my church. Has private end user login authentication with CRUD operations that allows user to add/delete member and post/delete upcoming events. I've also implemented Stripe payment gatway for donations.

Tech Stack: Python, PostgreSQL, SQL Alchemy, Flask, Jinja, HTML, CSS, Stripe

I used PostgreSQL(ORM) as database to store users, members, and events. I used SQL Alchemy with Flask to access and manage database and display it in the frontend with Jinja template. I used HTML to structured and CSS to styled the site. 


Data Model:

Users:     |   Members:     |   Events:
-----------|----------------|----------------
user_id    |   member_id    |  event_id
firstname  |   firstname    |   start_date
lastname   |   lastname     |   end_date
email      |   address      |   event_detail
password   |   email        |   user_id(fk)
           |   phone        |
           |   city         |
           |   state        |
           |   zipcode      |  
           |   house_hold   |
           |   user_id(fk)  |


