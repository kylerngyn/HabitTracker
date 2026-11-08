#import the Flask class, which we use to create the web app
from flask import Flask

#Create the app; __name__ tells Flask where to find the project's files
app = Flask(__name__)

#Run the function below when someone visits the home page ("/")
@app.route("/")
def home():
    return "Hello! My habit tracker is running."

#Only start the server when this file is run directly (not imported)
if __name__ == "__main__":
    #Start the server; debug=True auto restarts on save and shows detailed errors
    app.run(debug=True)
