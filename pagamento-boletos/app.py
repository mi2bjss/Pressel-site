from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Servidor Flask rodando!"

@app.route('/processar_pagamento', methods=['POST'])
def processar_pagamento():
    dados = request.get_json()
    print("Dados recebidos:", dados)  # Para debug no Termux
    return jsonify({"mensagem": "Dados recebidos com sucesso!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/processar_pagamento', methods=['POST'])
def processar_pagamento():
    dados = request.json  # Recebe os dados enviados pelo frontend
    print("Dados recebidos:", dados)  # Exibe os dados no terminal

    return jsonify({"mensagem": "Dados recebidos com sucesso!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

