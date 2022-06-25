# Code-Community-Group-Project-Backend
* * *
Our group project is a web application that allows you to join and create social communities.

# Built With
- [Django](https://www.djangoproject.com/)
- [python-decouple](https://pypi.org/project/python-decouple/)
- [Docker](https://www.docker.com/)
# Getting Started

* * *

### Prerequisites

Have docker installed on your system

### Setup

Create a virtual environment at a directory of your choosing with the command:

`python -m venv (name_of_your_choice)`

CD into the environment and start it with the command:

`source bin/activate`

Clone this repository into the virtual environment that you have just made.

Navigate into the directory holding the settings.py file and create a .env file with the provided SECRET_KEY and DEBUG options

* * *

### Starting the backend service

Build the container by running the following command:

`docker build -t community_backend .`

To start the container run the following command:

`docker-compose up`

Et Voila! Feel free to start adding to the project
