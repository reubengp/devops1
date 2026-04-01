# ACEest Fitness Flask DevOps Project

This project converts the baseline Tkinter fitness app into a minimal Flask API for the DevOps assignment. It keeps the core logic for client name, weight, program selection, and calorie calculation, and uses simple in-memory storage.

## Project Structure

```text
project/
│── app.py
│── test_app.py
│── requirements.txt
│── Dockerfile
│── README.md
│── .github/workflows/main.yml
```

## Run Locally

1. Create and activate a virtual environment if you want an isolated setup.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask application:

```bash
python app.py
```

The app starts on `http://0.0.0.0:5002`.

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
docker run -p 5002:5002 aceest-fitness-app
```

## CI/CD

The GitHub Actions workflow runs on every `push` and `pull_request`. It installs dependencies, runs `pytest`, and builds the Docker image.

## Jenkins Explanation

Jenkins is not installed in this project. For the assignment, Jenkins would be used as a build server that:

- Pulls code from GitHub
- Builds the project
- Runs tests
- Acts as a quality gate before deployment or release
