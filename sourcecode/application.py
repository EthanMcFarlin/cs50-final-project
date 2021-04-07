# Flask imports

import os
from cs50 import SQL
from authlib.integrations.flask_client import OAuth
from flask import Flask, abort, redirect, render_template, request, session, url_for
from flask_session import Session

# Starts web application

app = Flask(__name__)

# Runs SQL database

db = SQL("sqlite:///reviews.db")

# db = SQL("postgres://loogmnhxxajegy:b6b6523c9aec424b7845e411954b1bab1f2c50dc039b2a8ef4fd2dfa9dce5f9e@ec2-34-234-228-127.compute-1.amazonaws.com:5432/davn2bf5jkcb23")

# Complete list of houses for reference

HOUSES = [
    "Eliot",
    "Kirkland",
    "Winthrop",
    "Dunster",
    "Mather",
    "Leverett",
    "Quincy",
    "Adams",
    "Lowell",
    "Pfohozeimer",
    "Currier",
    "Cabot"
]

# Athlete status for data validation

ATHLETE_STATUS = [
    "Yes",
    "No"
]

# River houses list for average rating calculations

RIVER_HOUSES = [
    "Eliot",
    "Kirkland",
    "Winthrop",
    "Dunster",
    "Mather",
    "Leverett",
    "Quincy",
    "Adams",
    "Lowell",
]

# Quad houses list for average rating calculations

QUAD_HOUSES = [
    "Pfohozeimer",
    "Currier",
    "Cabot"
]

# Default route

@app.route("/")
def index():
    return render_template("index.html")

# Log-in implementation (adapted from CS50ID documentation written by David J. Malan at https://github.com/cs50/id/tree/master/flask)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

oauth = OAuth(app)
oauth.register(
    "cs50",
    client_id=os.environ.get("CLIENT_ID"),
    client_secret=os.environ.get("CLIENT_SECRET"),
    server_metadata_url=os.environ.get("SERVER_METADATA_URL")
)

@app.route("/login")
def login():
    return oauth.cs50.authorize_redirect(redirect_uri=url_for("review", _external=True))

@app.route("/review")
def review():
    return render_template("review.html", houses=HOUSES)

# Survey submission route: validates student reviews and stores it in a SQL database

@app.route("/submit", methods=["POST"])
def submit():

    current_HUID = db.execute("SELECT * FROM reviews WHERE HUID = ?", request.form.get("HUID")) # Keeps track of past HUID's in use

    certification = request.form.get("certification") # Collects certification form response
    if not certification: # Checks whether the certification text is filled
        return render_template("review.html", failure="Please agree to the certification", houses=HOUSES)

    HUID = request.form.get("HUID") # Collects HUID form response
    if not HUID: # Checks whether the HUID text is filled
        return render_template("review.html", failure="Please provide a Harvard University ID", houses=HOUSES)

    house = request.form.get("house") # Collects house form response
    if house not in HOUSES: # Ensures that the entered house name is a valid Harvard house (prevents against hacking)
        return render_template("review.html", failure="Please select a house", houses=HOUSES)

    blocking = request.form.get("blocking") # Collects blocking form response
    if not blocking: # Checks whether the entered blocking group size is valid
        return render_template("review.html", failure="Please specify a valid blocking size", houses=HOUSES)

    athlete = request.form.get("athlete") # Collects athlete form response
    if athlete not in ATHLETE_STATUS: # Ensures that the user either selected "Yes or No" (prevents against hacking)
        return render_template("review.html", failure="Please specify an athlete status", houses=HOUSES)

    satisfaction = request.form.get("satisfaction") # Collects satisfaction form response
    if not satisfaction: # Checks whether a satisfaction rating has been selected
        return render_template("review.html", failure="Please provide a satisfaction rating", houses=HOUSES)

    community = request.form.get("community") # Collects community form response
    if not community: # Checks whether a community rating has been selected
        return render_template("review.html", failure="Please provide a community rating", houses=HOUSES)

    belonging = request.form.get("belonging") # Collects belonging form response
    if not belonging: # Checks whether a belonging rating has been selected
        return render_template("review.html", failure="Please provide a belonging rating", houses=HOUSES)

    location = request.form.get("location") # Collects location form response
    if not location: # Checks whether a location rating has been selected
        return render_template("review.html", failure="Please provide a location rating", houses=HOUSES)

    living = request.form.get("living") # Collects architecture form response
    if not living: # Checks whether a living rating has been selected
        return render_template("review.html", failure="Please provide a living rating", houses=HOUSES)

    architecture = request.form.get("architecture") # Collects architecture form response
    if not architecture: # Checks whether an architecture rating has been selected
        return render_template("review.html", failure="Please provide an architecture rating", houses=HOUSES)

    if not len(current_HUID) == 0:  # Ensures that multiple reviews are not tied to a single HUID
        return render_template("review.html", failure="HUID already in use", houses=HOUSES)

    db.execute("INSERT INTO reviews (HUID, certification, house, blocking, athlete, satisfaction, community, belonging, location, living, architecture) VALUES (:HUID, :certification, :house, :blocking, :athlete, :satisfaction, :community, :belonging, :location, :living, :architecture)", HUID=HUID, certification=certification, house=house, blocking=blocking, athlete=athlete, satisfaction=satisfaction, community=community, belonging=belonging, location=location, living=living, architecture=architecture)

    if house in RIVER_HOUSES:
        return redirect("/riverhouses")

    if house in QUAD_HOUSES:
        return redirect("/radcliffequadrangle")

# River houses route: handles the display of individual and average ratings for 9/12 of the upperclassmen houses

@app.route("/riverhouses")
def riverhouses():

    AVG_RIVER_RATINGS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # Initializes a data structure for storage of river house average ratings
    counter = 0 # Initializes a counter variable to 0

    for individual_house in RIVER_HOUSES: # Iterates through a list of individual houses
        AVG_RIVER_RATINGS[counter] = db.execute("SELECT AVG(satisfaction) FROM reviews WHERE house = :selected_house", selected_house = individual_house)
        counter = counter + 1 # Increments counter by 1

    reviews = db.execute("SELECT * from reviews WHERE house = 'Eliot' or house = 'Kirkland' or house = 'Winthrop' or house = 'Mather' or house='Leverett' or house='Quincy' or house='Adams' or house='Lowell'")
    return render_template("riverhouses.html", reviews=reviews, ratings=AVG_RIVER_RATINGS) # Renders river houses template

# Quad houses route: handles the display of individual and average ratings for 3/12 of the upperclassmen houses

@app.route("/radcliffequadrangle")
def radcliffequadrangle():

    AVG_QUAD_RATINGS = [0, 1, 2] # Initializes a data structure for storage of quad hosue average ratings
    counter = 0 # Initializes a counter variable to 0

    for individual_house in QUAD_HOUSES: # Iterates through a list of individual houses
        AVG_QUAD_RATINGS[counter] = db.execute("SELECT AVG(satisfaction) FROM reviews WHERE house = :selected_house", selected_house = individual_house)
        counter = counter + 1 # Increments counter by 1

    reviews = db.execute("SELECT * from reviews WHERE house = 'Cabot' or house = 'Currier' or house = 'Pfohozeimer'")
    return render_template("radcliffequadrangle.html", reviews=reviews, ratings=AVG_QUAD_RATINGS) # Renders quad houses template

