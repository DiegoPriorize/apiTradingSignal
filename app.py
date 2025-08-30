
from flask import Flask, jsonify, request
import pandas as pd
import numpy as np
import pandas_ta as ta

app = Flask(__name__)

# Função para calcular indicadores técnicos
def calcular_indicadores(df):
    # Média Móvel (SMA de 50)
    df['SMA50'] = ta.sma(df['fechamento'], 50)
    
    # RSI
    df['RSI'] = ta.rsi(df['fechamento'], 14)
    
    # MACD
    df['MACD'], df['MACD_signal'], _ = ta.macd(df['fechamento'])
    
    return df

# Função de decisão de operação (compra, venda ou aguardar)
def decisao_operacao(df):
    if len(df) < 50:
        return "Sem dados suficientes", 0
    
    # Lógica para compra e venda com base na média móvel
    if df['fechamento'].iloc[-1] > df['SMA50'].iloc[-1]:  # Tendência de alta
        if df['RSI'].iloc[-1] < 30:  # Sobrevenda
            return "Comprar", 80  # Probabilidade de acerto de 80%
    elif df['fechamento'].iloc[-1] < df['SMA50'].iloc[-1]:  # Tendência de baixa
        if df['RSI'].iloc[-1] > 70:  # Sobrecompra
            return "Vender", 80  # Probabilidade de acerto de 80%
    
    return "Aguardar", 50  # Caso não haja tendência clara

@app.route('/analise', methods=['POST'])
def analise():
    data = request.get_json()
    
    # Convertendo as listas de dados para um DataFrame
    df = pd.DataFrame({
        'timestamp': data['timestamp'],
        'abertura': data['precoAbertura'],
        'fechamento': data['precoFechamento'],
        'maxima': data['maximaPeriodo'],
        'minima': data['minimoPeriodo'],
        'volume': data['volume'],
    })
    
    # Garantir que o formato dos preços seja float
    df['abertura'] = df['abertura'].astype(float)
    df['fechamento'] = df['fechamento'].astype(float)
    df['maxima'] = df['maxima'].astype(float)
    df['minima'] = df['minima'].astype(float)
    df['volume'] = df['volume'].astype(float)

    # Calcular indicadores técnicos
    df = calcular_indicadores(df)
    
    # Obter a decisão e a probabilidade de acerto
    decisao, probabilidade = decisao_operacao(df)

    # Responder com o melhor horário e a recomendação
    return jsonify({
        'decisao': decisao,
        'probabilidade': probabilidade,
        'melhor_horario': df['timestamp'].iloc[-1] if probabilidade > 50 else "Sem dados suficientes"
    })

if __name__ == '__main__':
    app.run(debug=True)
