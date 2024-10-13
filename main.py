from flask import Flask, render_template
import requests


app = Flask(__name__)


# Route for the homepage
@app.route('/')
def index():
  # Make a request to the News API for the top science headlines in the US
  Url = 'https://newsapi.org/v2/everything?q=tesla&from=2024-08-17&sortBy=publishedAt&apiKey=ed3ef6c15c94483cb836bca10352ae16'
  r = requests.get(Url).json()
  # Store the articles in a dictionary
  case = {'articles': r['articles']}
  # Render the index.html template and pass in the case dictionary
  return render_template("index.html", case=case)





# Route for the about page
@app.route('/about')
def about():
  # Render the about.html template
  return render_template("about.html")


# Route for the contact page
@app.route('/contact')
def contact():
  # Render the contact.html template
  return render_template("contact.html")


# Run the app
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
