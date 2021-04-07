# User Manual

## Introduction

Thank you for installing my project: "Harvard College Upperclassmen Housing: A Student Hub for Rankings and Reviews". It is an
interactive web application that seeks to foster increased awareness between first-years and upperclassmen on the subject of student
housing. The application is composed of four core pages: the home page, where users can view an interactive map of Harvard houses,
the survey page, where eligible students can leave reviews about their living experience, and lastly, the radcliffe and river house
pages where student reviews are aggregated and sorted into tables.

### How do I configure the project?

1) To begin the configuration process, unzip the project and extract the "sourcecode" folder out from it. This can be uploaded directly
to CS50 IDE. Once it is there, use the command "cd sourcecode" in the CS50 IDE terminal to navigate to the right directory.

2) Going forward, the next step is to open the "authentication_keys.txt" file and to copy the three commands provided there onto your
clipboard. These can be run directly in the CS50 IDE terminal to make sure that the CS50 ID Authentication system is configured for your
operating system.

3) With the set-up nearly complete, use the command "flask run" in the CS50 IDE terminal to start the server. You will be provided with
a link to the running web application, which can be opened up in a separate tab. If authentication through CS50 ID is not working
even after the web app is running, the survey page can be reached manually by entering the route "reviews" into the URL bar from the
project's home page.

4) The web app can be accessed at https://0ac9dbb3-44a2-4f6f-a8d9-43965ee348fa-ide.cs50.xyz:8080/

#### If I need to debug, how do I navigate the project's file structure?

1) The web application is built using the Python framework Flask, and accordingly, follows the recommended file structure that is
provided in the framework's documentation. The "application.py" file serves as the project's controller (MVC) and can be accessed
from the main directory in "sourcecode".

2) There, you will see a series of routes which handle logging-in, submitting the student survey, and loading data on the housing
pages. The application runs a SQLite3 server as its model (MVC). The database can be found in "reviews.db" and was created with the
query: "CREATE TABLE 'reviews' ('HUID' integer PRIMARY KEY NOT NULL, 'certification' boolean, 'house' text, 'blocking' integer,
'athlete' text, 'satisfaction' integer, 'community' integer, 'belonging' integer, 'location' integer, 'living' integer, 'architecture'
integer)". After an upperclassmen student submits a review of their housing experience, the database is used to store their survey
responses persistently.

3) The templates folder contains the application's view (MVC) in the form of a series of html documents for each of the app's major
pages. The templates are rendered in the controller in response to the respective routes being called. In the static folder, there
are image assets for the visual aesthethics of the interface. There is also a script folder which contains the logic for the Leaflet
map on the home page of the website.

##### How do I navigate the user interface?

1) To begin navigating the web app, scroll down to the map on the home page. Panning from side to side moves the window's frame of
reference, whereas zooming in or out has the effect of changing the scale of the map. By clicking on any given icon, information will
be displayed about the house's name.

2) If you are an upperclassmen student, you can proceed to click on the "Leave a Review" button in the top navigation bar. This should
direct you to HarvardKey where you can sign in with your Harvard credentials. If this does not work, go back to the home page and
manually enter "reviews" as a route into your URL bar.

3) From this point on, fill out the survey questions about your experience living in upperclassmen housing. Make sure that all required
fields have been filled out and click submit whenever you are ready.

4) The application should guide you to the "Radcliffe Housing" or "River Housing" pages, where you can view past students reviews
and average satisfaction ratings for each house. Feel free to scroll around and explore the comments past students left about
their housing experience. If confused about what the data in the tables mean, please refer to the comment below this one.

###### How do I interpret the information in the tables on the "Radcliffe Houses" and "River Houses" pages?

The tables on these pages contain a collection of student responses from upperclassmen, with some of the fields in the survey displayed.
Every row corresponds to a unique student. There is only one entry allowed per Harvard University ID. The first column refers to the
student's indicated blocking group size. The next contains their status as a varsity athlete. Finally, the next 6 columns reflect the
student's responses to questions about satisfaction in their house. A "1" on the scale corresponds to a low rating in whichever field,
whereas a "5" corrsponds to the highest (desirability of location, sense of belonging, etc.)

###### My question was not answered. Where can I get further help?

Please feel free to reach out to the project's creator, Ethan McFarlin, at (719) 930-2257 or emcfarlin@college.harvard.edu if you
run into any issues with the application. Thank you very much!

