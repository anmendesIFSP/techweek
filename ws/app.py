#
#
#  Funções do servidor WEB - Arquivo principal
#  Autor: Antonio Mendes de Oliveira Neto
#
#

from flask import render_template
from settings import app


@app.route('/')
def index():
    
    return render_template('index.html')

if __name__ == '__main__':

    app.run(debug=True)