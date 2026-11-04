# TODO: In your own words, explain why this file imports Flask.
from flask import Flask

# TODO: Explain what the Flask application object is used for.
app = Flask(__name__)

# TODO: Explain how this decorator connects a URL to a function.
@app.route("/")
# TODO: Explain when Flask calls this function.
def home():
        # TODO: Explain what value this return statement sends to the browser.
        return "Welcome to Manisha's Sunshine Cafe"

# TODO: Explain how this decorator connects /about to a function.
@app.route("/about")
# TODO: Explain when Flask calls this function.
def about():
        # TODO: Explain what value this return statement sends to the browser.
        return "Manisha's Sunshine Cafe is a friendly neighborhood cafe serving fresh coffee, drinks, and delicious snacks."
