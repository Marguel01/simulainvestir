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
        cdi_anual = 0.10
        inflacao_anual = 0.04

        cdi_mensal = (1 + cdi_anual) ** (1 / 12) - 1
        inflacao_mensal = (1 + inflacao_anual) ** (1 / 12) - 1

        meses = []
        investido = []
        cdi = []
        inflacao = []

        saldo_cdi = valor_inicial
        saldo_inflacao = valor_inicial

        for mes in range(1, tempo + 1):
            saldo *= (1 + taxa_juros)
            saldo += aporte_mensal
            investido.append(round(saldo, 2))

            saldo_cdi *= (1 + cdi_mensal)
            saldo_cdi += aporte_mensal
            cdi.append(round(saldo_cdi, 2))

            saldo_inflacao *= (1 + inflacao_mensal)
            saldo_inflacao += aporte_mensal
            inflacao.append(round(saldo_inflacao, 2))

            meses.append(f"{mes}")

        return jsonify({
            'meses': meses,
            'investido': investido,
            'cdi': cdi,
            'inflacao': inflacao
        })
    except:
        return jsonify({'erro': 'Erro ao calcular. Verifique os dados.'})

@app.route('/politica')
def politica():
    return render_template('politica.html')

@app.route('/termos')
def termos():
    return render_template('termos.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)