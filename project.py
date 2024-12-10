from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Mi primera vez usando GitHub Actions"}), 200

@app.route('/autor')
def about():
    return jsonify({"autor": "Daniela Vega"}), 200

if __name__ == '__main__':
    app.run(debug=True)
