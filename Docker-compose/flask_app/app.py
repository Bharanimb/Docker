from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("DB_NAME", "employee_db"),
        user=os.getenv("DB_USER", "admin"),
        password=os.getenv("DB_PASSWORD", "admin123")
    )

@app.route("/")
def home():
    return "Flask + PostgreSQL application is running!"

@app.route("/employees", methods=["POST"])
def add_employee():
    data = request.get_json()

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO employees (name, role) VALUES (%s, %s)",
        (data["name"], data["role"])
    )

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Employee added successfully"})

@app.route("/employees", methods=["GET"])
def get_employees():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name, role FROM employees ORDER BY id")
    employees = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(employees)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
