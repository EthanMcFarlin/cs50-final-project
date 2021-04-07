# Design Guide

## Technologies

HTML, CSS, Javascript, Bootstrap, Python, Flask, SQLite3, Leaflet

Running On: https://0ac9dbb3-44a2-4f6f-a8d9-43965ee348fa-ide.cs50.xyz:8080/

## Graphical Prototyping

I began the project by sketching up some mockups of the graphical user interface in Adobe Photoshop, which provided an opportunity for
me to play around with design styles and develop a brand identity for the project. In doing so, I recognized that I wanted to feature
a map prominently on the home page and separate housing information into two categories: the Radcliffe quadrangle and River houses.
During the early process of drafting designs for the housing pages, I identified that a table would be my desired means of presenting
survey responses from upperclassmen. At this stage, however, I wasn't sure what fields I wanted to collect from them and how to
aggregate this all in one place. I also was unclear as to what registration or sign-in process would stand in between users and the
survey.

### Site Wireframing and Data Model

As the user experience started to take shape, I created an animated wireframe in Adobe XD which illustrated the interaction between
different pages of the site. Starting from the home page, the user would funnel either to "Leave A Review" or one of the housing portals
with information on past responses. I also made a diagram on my whiteboard to map out the project structure using the Model View
Controller conceptual framework. Through this process, I determined that SQLite3 would be my model, Python with Flask would be my
controller, and HTML with Boostrap would be my view. SQL offered persistent data storage and the option of using relationship databases,
and Python with Flask was both dynamic and suitable for web programming.

#### Writing Controller Logic

When it came time for implementation, I began with the controller logic in Python. For each major route, I laid out my return
statements and began the data validation process for the survey. I also made sure that I was able to configure CS50 ID for use in my
project. This way, the survey form would be off limits to those who do not have an official Harvard Key account. I tried to take
necessary measures to prevent users from injecting invalid data in the database, such as checking their input against a list of possible
values for the houses and athlete statuses on the server side. I also invested time in making sure that the survey form felt intuitive
and covered an appropriate breadth of topics about the students' living experience (architecture, location, quality of rooms, etc.) When
an invalid response to the form is submitted, an error message pops up directing the user on how to fix the necessary elements of their
response.

##### Fleshing Out Final Design Features

From a design perspective, I made an effort to standardize a few patterns between different views of the webapp. One core feature of the
app's pages is a tinted background image which stretches across the top of their browser. This serves the purpose of adding visual
intrigue to the design and creating increased transparency about the site's pagemap. On the home page, I embedded a Leaflet map and
wrote logic in Javascript to zoom into particular coordinates and overlay icons/popups corresponding to each upperclassmen house. When
the user pans, the map reacts accordingly. Elsewhere, I tried to mirror the design of the "River Houses" page on the
"Radcliffe Quadrangle Houses" page to keep a consistent format. There is a table there which presents student responses to the form.
I was worried about this being overwhelming from a visual standpoint, so I added an overflow property to the table so that a scrollbar
would be created. I also added a feature on those pages that presents the average satisfaction rating for each house, allowing students
to directly compare the relative standing of each house when stacked up with each other.

###### Future Avenues for Improvement

Heading into the future, I would like to provide support for free-response answers to the survey questions. This way, students will be
able to offer a much more detailed and comprehensive overview of what their experience with housing was. I would also like to invest in
user testing and conduct research to see which points of the interface users commonly get stuck on. Thank you very much!

