from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

@app.route("/get_result", methods=["GET"])
def get_result():
    # Weighted probabilities
        colors = ["red", "green", "violet"]
            weights = [0.45, 0.45, 0.10]  # red=45%, green=45%, violet=10%

                result = random.choices(colors, weights=weights, k=1)[0]
                    return jsonify({"result": result})

                    if __name__ == "__main__":
                        port = int(os.environ.get("PORT", 5000))  # Railway will assign PORT
                            app.run(host="0.0.0.0", port=port)




