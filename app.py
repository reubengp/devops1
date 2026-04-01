from flask import Flask, jsonify, request


PROGRAM_FACTORS = {
    "Fat Loss (FL) – 3 day": 22,
    "Fat Loss (FL) – 5 day": 24,
    "Muscle Gain (MG) – PPL": 35,
    "Beginner (BG)": 26,
}


def calculate_calories(weight, program):
    factor = PROGRAM_FACTORS.get(program, 25)
    return int(float(weight) * factor)


def create_app():
    app = Flask(__name__)
    clients = []

    @app.get("/")
    def home():
        return (
            jsonify(
                {
                    "message": "ACEest Fitness API is running",
                    "routes": ["GET /", "GET /clients", "POST /clients"],
                }
            ),
            200,
        )

    @app.get("/clients")
    def get_clients():
        return jsonify(clients), 200

    @app.post("/clients")
    def add_client():
        data = request.get_json(silent=True) or {}
        name = str(data.get("name", "")).strip()
        program = str(data.get("program", "")).strip()
        weight = data.get("weight")

        if not name or not program or weight is None:
            return jsonify({"error": "name, weight, and program are required"}), 400

        try:
            weight = float(weight)
        except (TypeError, ValueError):
            return jsonify({"error": "weight must be a number"}), 400

        client = {
            "name": name,
            "weight": weight,
            "program": program,
            "calories": calculate_calories(weight, program),
        }
        clients.append(client)
        return jsonify(client), 201

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
