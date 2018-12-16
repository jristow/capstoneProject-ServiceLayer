# Service Layer for Capstone Project

This repository contains the service layer design documents and design for my capstone project.

The purpose of the project is to create an interactive visualization of housing affordability in America. The visualization
will consist of a map of the US, with individual dots representing different zip codes. The dots will be color coded based on
the affordability score of that particular zip code. The interface allows for users to type in a zip code and housing cost
data will be displayed in the graphic for that zip code.

Service layer is built with Python Flask and a MongoDB database.
User interface layer is built with D3.js.

This application has been deployed live to both AWS and Heroku. Links are available below.

AWS: http://finalcapstoneproject.mzadpkv4wh.us-west-2.elasticbeanstalk.com/ /br
Heroku: https://ristowcapstoneproject.herokuapp.com/

To run, from the directory with the service layer enter the following commands in your terminal:
```
export FLASK_APP=app.py
flask run
```
