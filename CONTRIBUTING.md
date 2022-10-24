# Welcome to GUI-PROJECTS REPOSITORY BY CLUELESS COMMUNITY

### Haven't made your first-contribution yet? 😢
Do check our [First Contribution](https://github.com/Clueless-Community/first-contribution) repository, where we have provided the guidelines to set up Git and how to make a pull request !

# Project Setup

## Fork the repository and clone the forked repository on your local machine
```bash
git clone https://github.com/MihirRajeshPanchal/GUI-Projects.git
```

## Change the directory
```bash
cd GUI-Projects
```
> Folder Structure
```
📂GUI-Projects
│   
└───📂Project 1
│   │   
│   └───Project files
│   │ 
|   └───README.md
│   │ 
|   └───requirements.txt(If required)
└───📂Project 2
│   │   
│   └───Project files
│   │ 
|   └───README.md
│   │ 
|   └───requirements.txt(If required)
.
.
.

    📄.gitignore
    📄CONTRIBUTING.md
    📄main.py
    📄README.md
    📄requirements.txt
```
# Note : Create a separate Folder for each GUI Project along with Readme.md and requirements.txt(if needed) file 

Once you are done with the changes you wanted to add. Follow the steps to make the pull request.
## Create and checkout to the new branch.
```powershell
git checkout -b <branch_name>
```
## Add the changes
```
git add .
```
## Commit your change with a proper messagge
```
git commit -m "Enter your message here"
```

## Make the Pull Request
```
git push origin <branch_name>
```