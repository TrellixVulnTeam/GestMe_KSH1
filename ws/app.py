from flask import Flask, request, json
import sys
import base64

sys.path.append('./')
from inc.classes.db.Perfis import DbPerfis
from inc.classes.lib.Request import RequestLib

# App init
app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/'
)

# Classes
Perfis = DbPerfis()
Request_lib = RequestLib()

# App Routes
@app.route('/')
def index():
  return 'This is RECOMMENDIT API index'

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
    return response


@app.route('/perfis/add', methods=['POST'])
def c_perfil():
    input = request.json
    # auth_token = Request_lib.get_authorization(request, type='Bearer')
    # input['authToken'] = auth_token if auth_token else ''
    resp = Perfis.c_perfil(input)
    status = 200 if resp['ok'] else 401
    response = app.response_class(
        response= json.dumps(resp),
        status=status,
        mimetype='application/json'
    )
    return response


if __name__  == '__main__':
    app.run(debug=True)