from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint GET para Monday validar a conexão
@app.route('/api/monday-to-whatsapp', methods=['GET'])
def validate_webhook():
    """Monday usa GET para validar se o webhook está ativo"""
    return jsonify({"status": "webhook_active", "message": "Webhook is ready to receive data"}), 200

# Endpoint POST para receber dados do Monday
@app.route('/api/monday-to-whatsapp', methods=['POST'])
def webhook():
    """Recebe dados do Monday quando uma linha é criada"""
    data = request.json
    print(f"Dados recebidos do Monday: {data}")
    return jsonify({"status": "received", "message": "Webhook data received successfully"}), 200

# Endpoint raiz para testar
@app.route('/', methods=['GET'])
def home():
    return jsonify({"mensagem": "Webhook está ativo!"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
