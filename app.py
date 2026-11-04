# fresh coffee, drinks, and delicious snacks."I import Flask so I can create a web application.
from flask import Flask

# I create the Flask application that will run my website.
app = Flask(__name__)

# This decorator connects the home page URL to the home function.
@app.route("/")
# Flask calls this function when someone visits the home page.
def home():
    # I send this welcome message to the visitor's browser.
    return "Welcome to Manisha's Sunshine Cafe"

# This decorator connects the about page URL to the about function.
@app.route("/about")
# Flask calls this function when someone visits the about page.
def about():
    # I send information about my cafe to the visitor's browser.
        return "Manisha's Sunshine Cafe is a friendly neighborhood cafe serving fresh coffee, drinks, and delicious snacks." 