from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/monday-to-whatsapp', methods=['GET', 'POST'])
def webhook():
    """Endpoint para Monday webhook"""
    if request.method == 'GET':
        return jsonify({"status": "active"}), 200
    
    if request.method == 'POST':
        try:
            data = request.json
            print(f"Recebido: {data}")
            return jsonify({"status": "ok"}), 200
        except:
            return jsonify({"status": "error"}), 500

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Webhook running"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
