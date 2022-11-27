from flask import Flask

app = Flask(__name__)

import controlador.libro
import controlador.usuario
import controlador.resena