# EGN 475 Week 1 Assignment 1.1

A small Flask app with a home page and an about page.

## Set up on Windows

From this folder in the VS Code terminal:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell blocks activation, use the VS Code Command Prompt terminal and run:

```cmd
.venv\Scripts\activate
```

## Run the app

With the virtual environment active:

```powershell
flask --app app run --debug
```

Open these URLs in a browser:

- http://127.0.0.1:5000/
- http://127.0.0.1:5000/about

The business name and about sentence in `app.py` use the cafe details selected
for this project. The comments are prompts, not finished explanations. Replace
each TODO with your own explanation before submitting, as required by the assignment.
