from flask import jsonify

class Alert:
    def __init__(self, alert_type, message):
        self.alert_type = alert_type
        self.message = message
