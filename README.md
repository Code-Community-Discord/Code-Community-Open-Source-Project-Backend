# Code Community Group Project

## About 

Our group project is a web application that allows you to join and create social communities.

## Built With

* [Django](https://www.djangoproject.com/)
* [python-decouple](https://pypi.org/project/python-decouple/)
* [Docker](https://www.docker.com/)

# For Contributors

## Prerequisites


Confirm you have the following installations, or follow these instructions: 
1. Install the latest stable release of Python 3.9.9.    

   Locate, download, and install the official Python 3.9.9 package <a href="https://www.python.org/downloads/windows/">here</a>. 

   <img src="https://www.tutorialsteacher.com/Content/images/python/install-wizard2.png" width="600px">

   When selecting optional features to install, make sure *pip* is selected.

2. Install Docker.

   Download and install Docker Desktop <a href="https://www.docker.com/get-started/">here</a>.

   <img src="https://i.imgur.com/Gplv7tI.png" width="400px">

## Setup

1. Open a command console and CD into a directory you want to store the virtual environment in. 

   For example:
   ```
   cd "C:\Users\Darius\Documents\Group Project"
   ```

2. Create a virtual environment with the command: 
   ```
   python -m venv (name_of_your_choice)
   ```

3. CD into the environment created in Step 2: 
   ```
   cd (name_of_environment)
   ```

4. Start the virtual environment. To do this . . .

   **On Windows devices**, enter the command:
   ```
   Scripts\Activate.ps1 
   ```

   NOTE: If this command did not work, try running your command console as an administrator. If it still does not work, try running the command:
   ```
   set-executionpolicy remotesigned
   ```

   **On Mac devices**, Enter then command:
   ```
   source bin/activate
   ```

   If this step was successful, the name of your environment should show up at the start of your next command line prompt in parentheses. 

5. Clone the project's repository into the virtual environment you created: 
   ```
   git clone https://github.com/Code-Community-Discord/Code-Community-Group-Project-Backend.git
   ```

6. Navigate to the directory holding the settings.py file and create a .env file with the provided SECRET_KEY and DEBUG options.

   **The information needed to write the .env file has been provided in Discord.*

------
### Starting the Backend Service
------
1. CD to the root repository directory created in **Setup - Step 5**.
   ```
   cd "C:\Users\Darius\Documents\Group Project\(name_of_environment)\Code-Community-Group-Project-Backend"
   ```

2. Build the Docker container:
   ```
   docker build -t code_community_backend .
   ```

3. Start the container: 
   ```
   docker-compose up
   ```

4. Et Voila! Feel free to start adding to the project.

## Development Guide

This section outlines the community's development process. 

------
### Planning
------

Initial planning follows a sequential process. 

1. Discuss ideas and filter them until one idea becomes the basis for the next major project, or feature update.

2. Describe the purpose of the application or functionality in one sentence. 

3. Define **User Stories**.

* As a ***role***, I want ***objective***, So I ***benefit***.
   
4. Map **Entity-Relationship Models**. 

5. Divide team members (5 - 10 total people) into two subteams. 
* One subteam consists of **frontend developers (FEDs)**, the other subteam consists of **backend developers (BEDs)**.

6. Determine the basis for languages, frameworks, and libraries. 

7. Define preliminary **Requirements**.

8. Create GitHub repository. 
* Two repositories; one for frontend, one for backend. Documentation must include:
   * README
   * GITFLOW
   * REQUIREMENTS
   * CONTRIBUTORS
* Documentation will be updated throughout the course of the project.

9. Define user **Endpoints**.

10. Develop **Wireframe** (Figma).

11. Update the **Product Backlog (PBL)**. 
* Consider all inputs gathered so far.
* Add the **Product Goal** to the PBL, based on the product's purpose defined in Step 2. 
* Continue adding items to the PBL during development.

------
### Development
------

Actual development follows an agile process <a href="https://scrumguides.org/scrum-guide.html">(SCRUM)</a>. 

1. Sprint Planning 
* Review the PBL and develop an agenda for the next sprint.
* Cleary define the **Sprint Goal**. (the *"why"*)
   * What value does this sprint provide?
* Developers map PBL items to the upcoming sprint. (the *"what"*) 
   * Developers determine the quantity of items they are comfortable with including.  
   * New items can be added to the PBL at this time. 
* Developers create a **Definition of Done (DOD)** for each selected PBL task. 
* Developers collaborate plans to complete each item. (the *"how"*)
* Add the Sprint Goal, PBL items, and plans to the **Sprint Backlog (SBL)**.

2. Progression 
* Each week during a sprint, developers will advise the team: 
   * What you've contributed to the project in the past week.
   * What you plan to contribute this week.
   * Is anything hampering your progress?
* Changes can be made to the SBL as more is learned.

3. Sprint Completion
* A sprint is completed once every item in the SBL meets the DOD. 

4. Sprint Review 
* The team shows their results in a working session.
* Outcomes are reviewed and tested. 
* Deviations from expectations are addressed.
* PBL adjustments are made.

5. Sprint Retrospective
* Inspect the last sprint and consider: individuals, interactions, processes, tools, and DODs.  
* What went well? What were the problems? How were they solved/not solved?
* Did someone come in with an assumption that went wrong? Where did the assumption originiate from?
* Identify the most helpful changes that can be made and act ASAP. 

6. Rinse and Repeat
* Return to Step 1 until the Product Goal is accomplished.

------
### Ticketing 
------

As developers come across issues and challenges, tickets should be submitted if the issue is not listed in the PBL. 

To submit a ticket:
* Navigate to the **Issues** tab within your respective repository. 
* Click **New issue**.
* Add a clear title that explains the issue. Descriptive comments are helpful, but not required. 
* Click **Submit new issue**.

<img src="https://i.imgur.com/GIJKwz6.png" width="1200px">

The Product Owner reviews tickets and adds items to the PBL accordingly. 

------
### Key Terms and Their Meaning
------

| Term                          | Acronym       | Definition 
| -------------                 | ------------- | -------------
| Backend Developers            | BEDs          | The subteam that develops backend systems.
| Endpoint                      | ---           | A location where data can be obtained, updated, or created.  
| Entity-Relationship Model     | ERM           | A database model diagram that captures relationships between entities.  
| Definition of Done            | DOD           | A collection of criteria that must be met to be considered done. 
| Frontend Developers           | FEDs          | The subteam that develops frontend systems.
| Product Backlog               | PBL           | An ordered list that captures all work needed to complete the product.
| Product Goal                  | ---           | A long-term objective that captures the finished state of the product.
| Requirements                  | ---           | Features, functions, and tasks needed during a project. 
| Sprint Backlog                | SBL           | Items selected from the Product Backlog to work on during the upcoming sprint.  
| User Story                    | ---           | An end goal expressed from the software user's perspective.
| Wireframe                     | ---           | Web page layouts that illustrate interface elements.