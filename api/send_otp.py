import requests
from flask import jsonify, request
import random
import os

FAST2SMS_API_KEY = "sFvFvftJvbueTW31XwZiIhYEBQeOShTqIxiwAixx5hwlsybSEFNZaCR2vqc8"

# Store OTPs in memory (for demo; use DB/Redis for production)
otp_store = {}

def handler(req):
    data = req.get_json()
    mobile = data.get("mobile")
    if not mobile or len(mobile) != 10:
        return jsonify({"success": False, "message": "Invalid mobile number."})
    otp = str(random.randint(100000, 999999))
    otp_store[mobile] = otp
    url = "https://www.fast2sms.com/dev/bulkV2"
    payload = {
        "authorization": FAST2SMS_API_KEY,
        "variables_values": otp,
        "route": "otp",
        "numbers": mobile
    }
    headers = {
        "Content-Type": "application/json"
    }
    r = requests.post(url, json=payload, headers=headers)
    if r.status_code == 200:
        return jsonify({"success": True, "message": "OTP sent."})
    else:
        return jsonify({"success": False, "message": "Failed to send OTP."})
