from flask import Flask, request, jsonify

# Importações necessárias
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

# Criação da instância do Flask
app = Flask(__name__)

# Configuração do JWT
app.config['JWT_SECRET_KEY'] = 'sua_chave_secreta_aqui'  # Substitua por uma chave secreta forte
jwt = JWTManager(app)

# Rota de Login - Para gerar o token de acesso
@app.route('/login', methods=['POST'])
def login():
    # Dados fictícios para teste
    username = 'usuario_teste'
    password = 'senha_teste'
    
    # Para fins de teste, sempre retorna sucesso, sem autenticação real
    if request.json.get('username') == username and request.json.get('password') == password:
        # Criação do token JWT
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Credenciais inválidas"}), 401

# Rota protegida
@app.route('/protegida', methods=['GET'])
@jwt_required()
def rota_protegida():
    # Obtém a identidade do usuário do token JWT
    current_user = get_jwt_identity()  # Obtém o usuário autenticado
    print("Rota protegida acessada")
    return jsonify(logged_in_as=current_user), 200

# Inicia o servidor Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)  # Ou qualquer outra porta disponível

