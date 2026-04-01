# ACEest Fitness DevOps Project

This is a simple Flask API built from the original fitness app logic for the DevOps assignment. It stores clients in memory and calculates calories from the selected program and weight.

## Files

```text
app.py
test_app.py
requirements.txt
Dockerfile
Jenkinsfile
README.md
.github/workflows/main.yml
```

## Run Locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

The app runs on `http://127.0.0.1:5001`.

## Run Tests

```bash
pytest
```

## Docker

Build:

```bash
docker build -t aceest-fitness-app .
```

Run:

```bash
docker run -p 5001:5001 aceest-fitness-app
```

## GitHub Actions

The workflow runs on every `push` and `pull_request`. It checks the Python files, runs `pytest`, builds the Docker image, and runs tests inside the built image.

## Jenkins

Jenkins is used as a build pipeline for this project.

- Jenkins pulls the code from GitHub
- Jenkins builds the project
- Jenkins runs the tests
- Jenkins acts as a quality gate before deployment

The repository includes a `Jenkinsfile` for the Jenkins pipeline.
