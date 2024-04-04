from flask import Flask, jsonify, request
from flask import Blueprint
import controllers.userController as userController
from flask import render_template

from db import conectar

user_api = Blueprint('user_api', __name__)

@user_api.route("/usuario", methods=['GET'])
def getUsuario():
    parametros = request.args
    email = parametros['email']
    password = parametros['password']
    result = userController.seleccionarUsuario(email, password)
    
    return render_template('index.html', result=result)
   