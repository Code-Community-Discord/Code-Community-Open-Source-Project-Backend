# Git Workflow

This document provides best practices for collaborators when interacting with GitHub for this project. 

Git prompts are also provided to address common requests.

## Prerequisites
------

1. Create a personal account on <a href="https://github.com/">GitHub</a>. 

2. Install <a href="https://git-scm.com/book/en/v2/Getting-Started-Installing-Git">Git</a>.

## Visual Aid
------

<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--M_fHUEqA--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/128hsgntnsu9bww0y8sz.png" width="600px">

## Getting Started
------

1. Clone the remote repository to your local device.
* Select or create a new folder where you want the project contents to be stored. 
* Open a shell of your choice and navigate to the folder you created. For example:
    ```
    cd "C:\Users\Darius\Documents\Project Folder"
    ```
* Open the GitHub repository you want to clone and copy the Web URL from GitHub. 

    <img src="https://i.imgur.com/3kxmfR7.png" width="1200px">
* Enter the command: 
    ```
    git clone "<repository_URL>"
    ```

2. Confirm you have write access to the repository. Contact the Product Owner if you do not currently have write access.  

3. Create your own branch. This will become your working directory. Your branch name can be either your first name or Discord username.  
    ```
    git checkout -b <your_name>
    ```

## Making Changes to the Project
------

### Make this first step a habit
------
Before writing any code, it's a good idea to pull the latest updates from the main branch.
* Checkout your branch to your working directory. 
    ```
    git checkout <your_branch_name>
    ```
* Pull the latest code from the main branch to your local repository. 
    ```
    git pull origin main
    ```
* Work on your changes to the project. 

### Submitting Changes 
------
Follow these steps when you have finished editing your files.
* Confirm you are still working in your branch to avoid submitting changes to an incorrect branch. We do not want to push changes to the main branch before they have been reviewed. 
    ```
    git branch
    ```
    Your current local branch will be marked with an asterisk (*).
* Add your files to the staging area. You can add files one by one:
    ```
    git add <file_name>
    ```
    Or, you can add all files:
    ```
    git add .
    ```
* Commit your changes to the local repository. Add a short (but descriptive) message explaining what you are pushing. 
    ```
    git commit -m "<your_message>"
    ```
* Push your changes to your branch. 
    ```
    git push
    ```
* Submit a Pull Request on the GitHub site. You can add a more descriptive message of what you are pushing here. If there are any questions, conflicts, or issues with what you are pushing, please note them here as well. 