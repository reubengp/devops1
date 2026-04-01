# ACEest Fitness Flask DevOps Project

This project converts the baseline Tkinter fitness app into a minimal Flask API for the DevOps assignment. It keeps the core logic for client name, weight, program selection, and calorie calculation, and uses simple in-memory storage.

## Project Structure

```text
project/
│── app.py
│── test_app.py
│── requirements.txt
│── Dockerfile
│── Jenkinsfile
│── README.md
│── .github/workflows/main.yml
```

## Run Locally

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask application:

```bash
python app.py
```

The app starts on `http://0.0.0.0:5001`.

## Run Tests

```bash
pytest
```

## Docker

Build the image:

```bash
docker build -t aceest-fitness-app .
```

Run the container:

```bash
docker run -p 5001:5001 aceest-fitness-app
```

## CI/CD

The GitHub Actions workflow runs on every `push` and `pull_request`. It performs a build and lint check with `py_compile`, runs `pytest`, builds the Docker image, and runs tests from the built Docker image.

## Jenkins Explanation

- Pulls code from GitHub
- Builds the project
- Runs tests
- Acts as a quality gate before deployment or release

This repository also includes a `Jenkinsfile` so the same stages can be configured in Jenkins without changing the application code. In a Jenkins setup, you would create a pipeline job connected to this GitHub repository, and Jenkins would execute the checkout, dependency installation, test, and Docker build stagesautomatically.
