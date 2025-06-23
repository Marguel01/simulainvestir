
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
        investido_total = valor_inicial
        meses = []
        acumulado = []
        investido = []
        juros = []

        for mes in range(1, tempo + 1):
            saldo *= (1 + taxa_juros)
            saldo += aporte_mensal
            investido_total += aporte_mensal
            meses.append(mes)
            acumulado.append(round(saldo, 2))
            investido.append(round(investido_total, 2))
            juros.append(round(saldo - investido_total, 2))

        return jsonify({
            'meses': meses,
            'acumulado': acumulado,
            'investido': investido,
            'juros': juros
        })
    except Exception as e:
        return jsonify({'erro': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
