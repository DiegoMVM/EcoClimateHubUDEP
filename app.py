import main_loop
from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    # Aquí puedes llamar a tus funciones
    main_loop.Loop
    return '¡Página web y funciones ejecutadas con éxito!'

if __name__ == '__main__':
    app.run(debug=True)
