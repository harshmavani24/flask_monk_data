import random

def get_temperature():
    return round(random.uniform(20.0, 30.0), 2)

def get_smoke_level():
    return random.randint(300, 600)

def get_flame_status():
    return random.choice(["No Flame", "Flame Detected"])

def get_human_touch():
    return random.choice(["Detected", "Not Detected"])

def generate_alerts():
    return [
        {"type": "Human Detection", "time": "2023-03-25 14:32:45", "status": "Active"},
        {"type": "Smoke Level", "time": "2023-03-25 12:15:30", "status": "Resolved"},
        {"type": "Temperature", "time": "2023-03-24 23:45:12", "status": "Critical"},
        {"type": "Flame Detection", "time": "2023-03-24 18:22:05", "status": "Resolved"},
    ]