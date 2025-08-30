
# API de Análise de Trading (Day Trade)

Esta é uma API em Python para análise de trading baseada em dados de mercado como timestamp, preços de abertura, fechamento, máximas, mínimas e volume. Ela calcula indicadores técnicos como Média Móvel (SMA), RSI e MACD para ajudar a determinar o melhor momento para fazer uma operação de compra ou venda.

## Funcionalidades
- Recebe dados de mercado (preços, volumes, timestamps).
- Calcula indicadores técnicos (SMA, RSI, MACD).
- Retorna a recomendação de operação (compra, venda ou aguardar) com uma porcentagem de acerto.
- Responde com o melhor horário para a operação, baseado nos dados fornecidos.

## Endpoints

### `/analise`

Este é o endpoint principal que processa os dados de entrada e retorna a recomendação de operação.

#### Método: `POST`

#### Parâmetros:

- `timestamp` (Lista de Inteiros): Lista de timestamps dos candles.
- `precoAbertura` (Lista de Strings): Lista de preços de abertura.
- `precoFechamento` (Lista de Strings): Lista de preços de fechamento.
- `maximaPeriodo` (Lista de Strings): Lista de preços máximos do período.
- `minimoPeriodo` (Lista de Strings): Lista de preços mínimos do período.
- `volume` (Lista de Strings): Lista de volumes.
- `stoploss` (Opcional, String): Preço de stop loss (não implementado, mas pode ser integrado).
- `takeProfit` (Opcional, String): Preço de take profit (não implementado, mas pode ser integrado).

#### Exemplo de Requisição (JSON):

```json
{
  "timestamp": [1609459200, 1609459260, 1609459320, 1609459380, 1609459440],
  "precoAbertura": ["45000", "45200", "45300", "45500", "45700"],
  "precoFechamento": ["45100", "45300", "45450", "45600", "45800"],
  "maximaPeriodo": ["45200", "45400", "45550", "45700", "45900"],
  "minimoPeriodo": ["44800", "45000", "45150", "45300", "45500"],
  "volume": ["100", "150", "120", "130", "140"]
}
```

#### Exemplo de Resposta:

```json
{
  "decisao": "Comprar",
  "probabilidade": 80,
  "melhor_horario": 1609459440
}
```

## Como Rodar a API

### 1. Instale as dependências:

Crie um ambiente virtual (opcional, mas recomendado) e instale as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 2. Execute a API:

Execute o servidor local com o comando:

```bash
python app.py
```

O servidor estará rodando em `http://127.0.0.1:5000/`.

### 3. Teste a API:

Use uma ferramenta como [Postman](https://www.postman.com/) ou `curl` para enviar uma requisição `POST` para o endpoint `/analise` com um JSON contendo os dados do mercado.

## Dependências

- Flask==2.2.3
- pandas==1.5.3
- numpy==1.24.1
- pandas_ta==0.3.14b0

## Notas
- A API usa o pacote `pandas_ta` para calcular indicadores técnicos como Média Móvel (SMA), RSI e MACD. Não é necessária nenhuma instalação adicional de dependências nativas.
