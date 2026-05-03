from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/api/monday-to-whatsapp', methods=['GET', 'POST'])
def webhook():
    """Endpoint para Monday webhook"""
    
    if request.method == 'GET':
        return jsonify({"status": "active"}), 200
    
    if request.method == 'POST':
        try:
            data = request.json or {}
            
            # ✅ CORREÇÃO CRÍTICA: responder ao challenge do Monday
            if 'challenge' in data:
                return jsonify({"challenge": data['challenge']}), 200
            
            # Lógica principal — executa quando uma linha é criada
            event = data.get('event', {})
            pulse_id = event.get('pulseId')
            board_id = event.get('boardId')
            column_values = event.get('columnValues', {})
            
            print(f"Nova linha criada — Board: {board_id}, Item: {pulse_id}")
            print(f"Valores das colunas: {column_values}")
            
            # Aqui vai a lógica de WhatsApp (próximo passo)
            
            return jsonify({"status": "ok"}), 200
        
        except Exception as e:
            print(f"Erro: {e}")
            return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Webhook running"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
