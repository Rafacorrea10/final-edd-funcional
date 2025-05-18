from flask import Flask, render_template, request, jsonify
from math import hypot
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/shortest_path", methods=["POST"])
def shortest_path():
    data = request.get_json()
    origin = data["origin"]
    dest = data["dest"]
    waypoints = data.get("waypoints", [])
    sequence = [find_node(origin)] + [find_node(wp) for wp in waypoints] + [find_node(dest)]
    return jsonify(path=sequence)

def find_node(nid):
    return {"id": nid, "name": f"Node {nid}"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
