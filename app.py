from flask import Flask, jsonify
import security_checks

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"})

@app.route('/check_security', methods=['GET'])
def check_security():
    results = security_checks.run_security_checks()
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
