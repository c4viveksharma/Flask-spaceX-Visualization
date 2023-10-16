from flask import Flask, render_template
from datetime import datetime
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", launches = launches)

def fetch_spcex_launches():
    url = 'https://api.spacexdata.com/v4/launches'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

# def categorize_launches(launches):


def categorize_launches(Launches):
    successful = list(filter( lambda x: x["success"] and not x["upcoming"],Launches))
    failed = list(filter(lambda x: not x["success"] and not x["upcoming"],Launches))
    upcoming = list(filter(lambda x: x["upcoming"],Launches))
  
    return {

        "succesful": successful,
        "failed": failed,
        "upcoming": upcoming
    }

launches = categorize_launches(fetch_spcex_launches())


if __name__ == '__main__':
    app.run(debug=True)