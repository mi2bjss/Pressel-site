from flask import Flask, jsonify, request
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

# Chave secreta para a codificação do JWT (em produção, coloque uma chave mais forte)
app.config['SECRET_KEY'] = 'minha_chave_secreta'

# Função para verificar o token JWT
def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None

        # Verifica se o token está na solicitação
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]

        if not token:
            return jsonify({'message': 'Token é necessário!'}), 403

        try:
            # Decodifica o token
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data['sub']
        except:
            return jsonify({'message': 'Token inválido!'}), 403

        return f(current_user, *args, **kwargs)

    return decorated_function

# Rota para login, onde o token JWT é gerado
@app.route('/login', methods=['POST'])
def login():
    auth = request.get_json()

    if not auth or not auth.get('username') or not auth.get('password'):
        return jsonify({'message': 'Credenciais ausentes!'}), 400

    # Usuário fixo para fins de exemplo
    if auth['username'] == 'usuario_teste' and auth['password'] == 'senha_teste':
        token = jwt.encode({
            'sub': auth['username'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, app.config['SECRET_KEY'], algorithm="HS256")

        return jsonify({'access_token': token})

    return jsonify({'message': 'Credenciais inválidas!'}), 401

# Rota protegida que só pode ser acessada com um token válido
@app.route('/protegida', methods=['GET'])
@token_required
def protegida(current_user):
    return jsonify({'message': f'Olá, {current_user}! Você tem acesso ao conteúdo protegido.'})

# Rota para validar os dados do cartão de crédito
@app.route('/validar_cartao', methods=['POST'])
@token_required
def validar_cartao(current_user):
    data = request.get_json()

    # Verificar se os dados do cartão foram passados corretamente
    numero_cartao = data.get('numero')
    data_validade = data.get('validade')
    cvv = data.get('cvv')

    if not numero_cartao or not data_validade or not cvv:
        return jsonify({'message': 'Dados do cartão incompletos!'}), 400

    # Aqui você pode adicionar a lógica de validação real do cartão, por exemplo,
    # verificando o número do cartão com alguma API de pagamento
    # Para fins de exemplo, vamos apenas retornar os dados como válidos.
    
    return jsonify({
        'message': 'Cartão validado com sucesso!',
        'numero': numero_cartao,
        'validade': data_validade,
        'cvv': cvv
    })

# Rota inicial
@app.route('/')
def home():
    return jsonify({'message': 'Bem-vindo ao Validador de Cartões!'})

if __name__ == '__main__':
    # Usando a porta 8080 conforme sua solicitação
    app.run(host="0.0.0.0", port=8080)

