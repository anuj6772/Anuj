from flask import jsonify, request

# Use the same otp_store as send_otp.py (for demo, not production)
otp_store = {}

def handler(req):
    data = req.get_json()
    mobile = data.get("mobile")
    otp = data.get("otp")
    if not mobile or not otp:
        return jsonify({"success": False, "message": "Missing mobile or OTP."})
    # For demo, always fail unless you use a persistent store
    # In production, use a shared DB/Redis for otp_store
    if otp_store.get(mobile) == otp:
        del otp_store[mobile]
        return jsonify({"success": True, "message": "OTP verified."})
    else:
        return jsonify({"success": False, "message": "Invalid OTP."})
