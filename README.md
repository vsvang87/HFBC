A responsive full-stack website for my church. Has private end user login authentication with CRUD operations that allows user to add/delete member and post/delete upcoming events. Also added stripe payment gateway for donations.

Tech Stack: Python, PostgreSQL, SQL Alchemy, Flask, Jinja, HTML, CSS

I used PostgreSQL(ORM) as database to store members and events data. I used SQL Alchemy to access and manage database.


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


