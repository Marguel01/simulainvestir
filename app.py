
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
        periodo = request.form.get('periodo', 'meses')

        if periodo == "anos":
            tempo *= 12

        saldo = valor_inicial
        meses = []
        investido = []

        for mes in range(1, tempo + 1):
            saldo *= (1 + taxa_juros)
            saldo += aporte_mensal
            meses.append(mes)
            investido.append(round(saldo, 2))

        return jsonify({'meses': meses, 'investido': investido})
    except:
        return jsonify({'erro': 'Erro ao calcular. Verifique os dados.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
