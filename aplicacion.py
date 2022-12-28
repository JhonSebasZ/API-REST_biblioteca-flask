from flask import Flask

app = Flask(__name__)

import controlador.libro
import controlador.resena
import controlador.libroDeseo
import controlador.carro