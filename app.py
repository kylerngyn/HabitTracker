#import the Flask class, which we use to create the web app
from flask import Flask

# Import the function that creates our database tables
from database import init_db

#Create the app; __name__ tells Flask where to find the project's files
app = Flask(__name__)

#Run the function below when someone visits the home page ("/")
@app.route("/")
def home():
    return "Hello! My habit tracker is running."

#Only start the server when this file is run directly (not imported)
if __name__ == "__main__":
    # Make sure the database tables exist before the server starts
    init_db()
    #Start the server; debug=True auto restarts on save and shows detailed errors
    app.run(debug=True)
