
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        valor_inicial = float(request.form['valor_inicial'])
        aporte_mensal = float(request.form['aporte_mensal'])
        taxa_juros = float(request.form['taxa_juros']) / 100
        tempo = int(request.form['tempo'])
        periodo = request.form['periodo']

        if periodo == 'anos':
            tempo *= 12
            taxa_juros /= 12

        montante = valor_inicial
        montantes = []

        for _ in range(tempo):
            montante *= (1 + taxa_juros)
            montante += aporte_mensal
            montantes.append(round(montante, 2))

        return jsonify({'montantes': montantes})
    except Exception as e:
        return jsonify({'erro': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
