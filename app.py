from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) # Permite que o Frontend se conecte com segurança

@app.route('/')
def home():
    return "Ainsten Backend está funcionando!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')

    # Simulação de resposta da IA
    if "olá" in user_message.lower():
        response_message = "Olá, Nathalia! Como posso ajudar você hoje?"
    elif "como você está" in user_message.lower():
        response_message = "Estou funcionando perfeitamente, obrigado por perguntar!"
    elif "seu nome" in user_message.lower():
        response_message = "Meu nome é Ainsten."
    else:
        response_message = f"Entendi que você disse: '{user_message}'. Estou processando sua solicitação."

    return jsonify({"response": response_message})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)