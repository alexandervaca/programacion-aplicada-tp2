from flask import Flask
from flask import request
from flask import jsonify
from modelo import Concurso

app = Flask(__name__)

@app.route('/')
def inicio():
  return 'Api Rest con Flask'

#http://localhost:5000/flask/api/v2/ALEX/24.6
@app.route('/flask/api/v2//<nombre_del_ganador>/<float:mejor_disparo>', methods=['GET'])
def premioGanador(nombre_del_ganador, mejor_disparo):
  if request.method == 'GET':
    mensajePremio = Concurso().obtenerPremio(nombre_del_ganador, mejor_disparo)
    return jsonify(mensajePremio)

  if request.method == 'POST':
    return jsonify({'mensaje':'Method not supported'})

  return jsonify({'mensaje':'Error'})

if __name__ == '__main__':
  app.run(debug=True)

