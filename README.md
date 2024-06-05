# datafun-03-project

Start by creating a new repository with a README.md file

Open the folder on your computer where you want the repository to live and open a terminal

Clone the repository to the selected folder: git clone REPOSITORY_URL

Create a .py file to code in

Add a requirements.txt to hold the required project modules

Create and activate a Python virtual environment for the project: py -m venv .venv
                                                                  .\.venv\Scripts\Activate
                                                                  
Install all required packages into your local project virtual environment: py -m pip install requests
                                                                  
Redirect the output of the pip freeze command to a requirements.txt file in your root project folder: py -m pip freeze > requirements.txt                                                                  

Add a .gitignore file to your project folder to exclude the virtual environment folder and your .vscode settings folder

Now you can start coding in VS Code

Periodically add, commit and push the file to GitHub: git add .
                                                      git commit -m "message"
                                                      git push origin main

Follow along with the instructions and create appropriate functions

Fetch and write data from online sources in .txt, .csv, .xls, and .json formats Mostly used chatGPT to write functions.

Note: Utilize chatGPT to assit in duplicate work for other file types and troubleshooting

# This project was built to the following specification: https://github.com/denisecase/datafun-03-spec 

