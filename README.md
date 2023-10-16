SpaceX Launch Data Project
SpaceX Logo

This project is a Flask web application that fetches data from the SpaceX API and displays it in a user-friendly way. Users can view successful, upcoming, and failed SpaceX launches in separate tabs on the web page. The project is designed to demonstrate how to interact with an API, categorize data, and render it using Flask and Bootstrap.

Table of Contents
Features
Prerequisites
Getting Started
Installation
Running the Application
Usage
Contributing
License
Features
Fetches SpaceX launch data from the SpaceX API.
Categorizes launch data into successful, upcoming, and failed launches.
Uses Flask for the web application framework.
Utilizes Bootstrap for styling and tab navigation.
Demonstrates API data retrieval and rendering using Flask.
Prerequisites
Before you begin, ensure you have met the following requirements:

Python 3.x
Flask
Requests library
Bootstrap (included via CDNs in the HTML template)
Getting Started
To get this project up and running, follow these steps:

Installation
Clone this repository to your local machine:

bash
Copy code
https://github.com/c4viveksharma/Flask-spaceX-Visualization.git
Navigate to the project directory:

bash
Copy code
cd Flask-spaceX-Visualization
Create a virtual environment (recommended):

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS and Linux:

bash
Copy code
source venv/bin/activate
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Running the Application
Run the Flask application:

bash
Copy code
flask run
Open your web browser and go to http://localhost:5000 to view the SpaceX launch data.

Usage
The web application displays SpaceX launch data categorized into successful, upcoming, and failed launches.
Click on the tabs to switch between the different launch categories.
Each launch is presented as a card with details such as launch name and date.
Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them.
Push your changes to your fork.
Submit a pull request.