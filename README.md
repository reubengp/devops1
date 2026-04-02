# ACEest Fitness DevOps Project

This project is a small Flask web application made for the DevOps assignment. It keeps the main fitness logic from the original program: client name, weight, selected program, and calorie calculation.

## Project Files

```text
app.py
test_app.py
requirements.txt
Dockerfile
Jenkinsfile
README.md
.github/workflows/main.yml
```

## Run the App

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5001`

## Run Tests

```bash
pytest
```

## Docker

```bash
docker build -t aceest-fitness-app .
docker run -p 5001:5001 aceest-fitness-app
```

## GitHub Actions

The workflow runs on every `push` and `pull_request`. It checks the Python files, runs the tests, and builds the Docker image.

## Jenkins


Jenkins is used as the build pipeline in this project.

- Jenkins pulls the code from GitHub
- Jenkins builds the project
- Jenkins runs the tests

The Jenkins pipeline is defined in `Jenkinsfile`.
