
from flask import Flask, redirect, render_template_string, url_for

app = Flask(__name__)

# Sample parking data
parking_slots = {
    1: False,
    2: True,
    3: False,
    4: True,
    5: False,
    6: False,
    7: True,
    8: False,
}

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Smart Parking System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f1f5f9;
            margin: 0;
            padding: 30px;
            color: #1e293b;
        }
        .container {
            max-width: 900px;
            margin: auto;
        }
        header {
            background: #123b68;
            color: white;
            padding: 25px;
            border-radius: 12px;
        }
        .summary {
            display: flex;
            gap: 15px;
            margin: 20px 0;
            flex-wrap: wrap;
        }
        .card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            flex: 1;
            min-width: 130px;
        }
        .slots {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
        }
        .slot {
            padding: 20px 10px;
            border-radius: 10px;
            text-align: center;
            color: white;
        }
        .available { background: #16845b; }
        .occupied { background: #c24141; }
        .slot form { margin-top: 12px; }
        button {
            background: white;
            color: #123b68;
            border: none;
            padding: 9px 12px;
            border-radius: 6px;
            cursor: pointer;
            font-weight: bold;
        }
        button:hover { background: #e2e8f0; }
        @media (max-width: 550px) {
            .slots { grid-template-columns: repeat(2, 1fr); }
            body { padding: 15px; }
        }
    </style>
</head>
<body>
<main class="container">
    <header>
    <h1>Smart Parking System</h1>
    <p>Manage parking availability easily</p>
    <p>Feature branch demonstration</p>
    </header>

    <section class="summary">
        <div class="card">
            <h3>Total Slots</h3>
            <h2>{{ slots|length }}</h2>
        </div>
        <div class="card">
            <h3>Available</h3>
            <h2>{{ available }}</h2>
        </div>
        <div class="card">
            <h3>Occupied</h3>
            <h2>{{ occupied }}</h2>
        </div>
    </section>

    <h2>Parking Slot Status</h2>
    <section class="slots">
        {% for number, is_occupied in slots.items() %}
        <div class="slot {{ 'occupied' if is_occupied else 'available' }}">
            <h3>Slot {{ number }}</h3>
            <strong>{{ 'Occupied' if is_occupied else 'Available' }}</strong>

            <form action="{{ url_for('toggle_slot', slot_id=number) }}"
                  method="post">
                <button type="submit">
                    {{ 'Free Slot' if is_occupied else 'Occupy Slot' }}
                </button>
            </form>
        </div>
        {% endfor %}
    </section>
</main>
</body>
</html>
"""


@app.route("/")
def home():
    available = sum(not occupied for occupied in parking_slots.values())
    occupied = sum(parking_slots.values())

    return render_template_string(
        HTML,
        slots=parking_slots,
        available=available,
        occupied=occupied,
    )


@app.route("/toggle/<int:slot_id>", methods=["POST"])
def toggle_slot(slot_id):
    if slot_id in parking_slots:
        parking_slots[slot_id] = not parking_slots[slot_id]

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
