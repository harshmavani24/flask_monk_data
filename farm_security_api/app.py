from flask import Flask, jsonify
from flask_cors import CORS
from data_store import get_all_sensor_data

app = Flask(__name__)
CORS(app)

@app.route('/dashboard', methods=['GET'])
def get_sensor_data():
    data = get_all_sensor_data()
    return jsonify(data)



# Sample RFID Access Logs
rfid_logs = [
    {
        "timestamp": "2025-03-25 08:45:12",
        "card_id": "337589753",
        "user": "Harsh Mavani",
        "action": "Entry"
    },
    {
        "timestamp": "2025-04-25 17:30:45",
        "card_id": "999465783",
        "user": "Aafi Mansuri",
        "action": "Exit"
    },
    {
        "timestamp": "2025-03-25 09:15:33",
        "card_id": "958027583",
        "user": "Shubham Kumar",
        "action": "Entry"
    }
    
]

@app.route('/controlpannel', methods=['GET'])
def get_rfid_logs():
    return jsonify({"logs": rfid_logs})


# Sample Alert Notifications
security_alerts = [
    {
        "timestamp": "2025-03-25 14:32:45",
        "sensor": "Human Detection",
        "location": "Sargasan Gandhingar",
        "severity": "High",
        "status": "Active"
    },
    {
        "timestamp": "2023-03-25 12:15:30",
        "sensor": "Smoke Level",
        "location": "Sargasan Gandhingar",
        "severity": "Medium",
        "status": "Resolved"
    },
    {
        "timestamp": "2025-03-26 12:15:30",
        "sensor": "Temperature",
        "location": "Surat",
        "severity": "High",
        "status": "Critical"
    },
    {
        "timestamp": "2025-03-24 18:22:05",
        "sensor": "Flame Detection",
        "location": "Sargasan Gandhingar",
        "severity": "High",
        "status": "Resolved"
    },
    {
        "timestamp": "2025-03-23 09:12:33",
        "sensor": "Human Detection",
        "location": "Sargasan Gandhingar",
        "severity": "Low",
        "status": "Resolved"
    },
    {
        "timestamp": "2025-03-22 15:48:22",
        "sensor": "Smoke Level",
        "location": "Sargasan Gandhingar",
        "severity": "Medium",
        "status": "Resolved"
    },
    {
        "timestamp": "2025-03-21 07:33:18",
        "sensor": "Temperature",
        "location": "Sargasan Gandhingar",
        "severity": "Medium",
        "status": "Resolved"
    }
]

@app.route('/notification', methods=['GET'])
def get_alerts():
    return jsonify({"alerts": security_alerts})


if __name__ == '__main__':
    app.run(debug=True, port=5000)