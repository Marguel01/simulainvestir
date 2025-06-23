
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
        juros_acumulados = []

        total_investido = valor_inicial
        total_juros = 0

        for mes in range(1, tempo + 1):
            saldo *= (1 + taxa_juros)
            saldo += aporte_mensal

            total_investido += aporte_mensal
            total_juros = saldo - total_investido

            meses.append(mes)
            investido.append(round(saldo, 2))
            juros_acumulados.append(round(total_juros, 2))

        return jsonify({
            'meses': meses,
            'investido': investido,
            'juros': juros_acumulados,
            'total_investido': round(total_investido, 2),
            'valor_final': round(saldo, 2),
            'total_juros': round(total_juros, 2)
        })
    except Exception as e:
        return jsonify({'erro': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
