from flask import Flask, request, json
import sys, os
import base64

BASE_PATH = os.path.abspath(__file__+ './')
sys.path.append(BASE_PATH)

from inc.classes.lib.Request import RequestLib
from inc.classes.db.Conteudos import DbConteudos
from inc.classes.db.Formacoes import DbFormacoes
from inc.classes.db.Paises import DbPaises
from inc.classes.db.Perfis import DbPerfis

# App init
app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/'
)

# Classes
Conteudos = DbConteudos()
Formacoes = DbFormacoes()
Paises = DbPaises()
Perfis = DbPerfis()
Request_lib = RequestLib()

# App Routes
@app.route('/')
def index():
  return 'GestME index'

# PERFIS
@app.route('/login', methods=['POST'])
def login():
    resp = Request_lib.get_authorization(request, type='Basic', decode64=True)
    credentials = resp if resp else {}
    resp = Perfis.r_login(credentials)
    status = 200 if resp['ok'] else 401    
    response = app.response_class(
        response= json.dumps(resp),
        status=status,
        mimetype='application/json'
    )
    # return f'{credentials}'
    return response


@app.route('/perfis/add', methods=['POST'])
def c_perfil():
    input = request.json
    resp = Perfis.c_perfil(input)
    status = 200 if resp['ok'] else 401
    response = app.response_class(
        response= json.dumps(resp),
        status=status,
        mimetype='application/json'
    )
    return response

@app.route('/perfis/update', methods=['POST'])
def u_perfil():
    input = request.json
    resp = Request_lib.get_authorization(request, type='Bearer', decode64=False)
    input['authToken'] = resp if resp else ''
    resp = Perfis.u_perfil(input)
    status = 200 if resp['ok'] else 401
    response = app.response_class(
        response= json.dumps(resp),
        status=status,
        mimetype='application/json'
    )
    # response = input
    return response

@app.route('/perfis/perfil', methods=['POST'])
def r_perfil():
    input = {}
    resp = Request_lib.get_authorization(request, type='Bearer', decode64=False)
    input['authToken'] = resp if resp else ''
    resp = Perfis.r_perfil(input)
    status = 200 if resp['ok'] else 401
    response = app.response_class(
        response= json.dumps(resp),
        status=status,
        mimetype='application/json'
    )
    return response

@app.route('/perfis/historico', methods=['POST'])
def r_historico_perfil():
    input = {}
    resp = Request_lib.get_authorization(request, type='Bearer', decode64=False)
    input['authToken'] = resp if resp else ''
    resp = Perfis.r_historico_perfil(input)
    status = 200 if resp['ok'] else 401
    response = app.response_class(
        response= json.dumps(resp),
        status=status,
        mimetype='application/json'
    )
    return response

# CONTEUDOS
@app.route('/conteudos/id', methods=['POST'])
def r_conteudo_id():
    input = request.json
    resp = Request_lib.get_authorization(request, type='Bearer', decode64=False)
    input['authToken'] = resp if resp else ''
    resp = Conteudos.r_conteudo_id(input)
    status = 200 if resp['ok'] else 401
    response = app.response_class(
        response= json.dumps(resp),
        status=status,
        mimetype='application/json'
    )
    return response


# CONTEUDOS
@app.route('/paises/id', methods=['POST'])
def r_pais_id():
    input = request.json
    id_pais = input['pai_pk'] if 'pai_pk' in  input else 0
    resp = Paises.r_pais(id_pais)
    status = 200 if resp['ok'] else 401
    response = app.response_class(
        response= json.dumps(resp),
        status=status,
        mimetype='application/json'
    )
    return response

@app.route('/paises', methods=['GET'])
def r_paises():
    resp = Paises.r_paises()
    status = 200 if resp['ok'] else 404
    response = app.response_class(
        response= json.dumps(resp),
        status=status,
        mimetype='application/json'
    )
    return response

@app.route('/paises/nome', methods=['POST'])
def r_pais_nome():
    input = request.json
    resp = Paises.r_pais_nome(input)
    status = 200 if resp['ok'] else 401
    response = app.response_class(
        response= json.dumps(resp),
        status=status,
        mimetype='application/json'
    )
    return response

# FORMACOES
@app.route('/formacoes', methods=['GET'])
def r_formacoes():
    resp = Formacoes.r_formacoes()
    status = 200 if resp['ok'] else 404
    response = app.response_class(
        response= json.dumps(resp),
        status=status,
        mimetype='application/json'
    )
    return response

@app.route('/formacoes/id', methods=['POST'])
def r_formacao_id():
    input = request.json
    id_formacao = input['for_pk'] if 'for_pk' in  input else 0
    resp = Formacoes.r_formacao(id_formacao)
    status = 200 if resp['ok'] else 401
    response = app.response_class(
        response= json.dumps(resp),
        status=status,
        mimetype='application/json'
    )
    return response

@app.route('/formacoes/nome', methods=['POST'])
def r_formacao_nome():
    input = request.json
    resp = Formacoes.r_formacao_nome(input)
    status = 200 if resp['ok'] else 401
    response = app.response_class(
        response= json.dumps(resp),
        status=status,
        mimetype='application/json'
    )
    return response


if __name__  == '__main__':
    app.run(debug=True)
    # app.run(host='192.168.100.8', debug=True)