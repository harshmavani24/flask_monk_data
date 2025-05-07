from sensors import get_temperature, get_smoke_level, get_flame_status, get_human_touch, generate_alerts

def get_all_sensor_data():
    return {
        "temperature": {
            "value": get_temperature(),
            "unit": "°C",
            "sensor": "DS18B20"
        },
        "smoke_level": {
            "value": get_smoke_level(),
            "unit": "ppm",
            "sensor": "MQ2 Gas Sensor"
        },
        "flame_detection": {
            "value": get_flame_status(),
            "sensor": "LM393 Flame Sensor"
        },
        "human_touch": {
            "value": get_human_touch(),
            "sensor": "Digital Touch Sensor"
        },
        "recent_alerts": generate_alerts()
    }