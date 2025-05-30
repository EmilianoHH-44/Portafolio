print ("holamundo")
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import quantstats as qs
import plotly.express as px
from scipy.stats import norm
import random
import statsmodels.api as sm
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'NVDA', 'HD', 'JNJ', 'JPM', 'PG']
start = '2000-01-01'
end = '2025-05-01'
data = yf.download(tickers, start=start)
data_benchmark = yf.download('^GSPC', start=start)
precios_acciones = yf.download(tickers, start, end, auto_adjust=True)['Close']
precios_indice = yf.download('^GSPC', start, end, auto_adjust=True)['Close']


rendimientos_acciones = precios_acciones.pct_change().dropna()
rendimiento_mercado = precios_indice.pct_change().dropna()
rendimiento_mercado = rendimiento_mercado.reindex(rendimientos_acciones.index, method='ffill')
rendimiento_mercado = rendimiento_mercado.squeeze()

returns_df = data['Close'].pct_change(fill_method=None).dropna()
benchmark_returns_df = data_benchmark['Close'].pct_change(fill_method=None).dropna()
avg_returns = returns_df.mean() * 252
cov_mat = returns_df.cov() * 252

#Primer metodo calcular CAPM
# === Parámetros ===
rf = 0.05  # tasa libre de riesgo anual 5%

# === Calcular beta y CAPM para cada acción ===
betas = {}
expected_returns_capm = {}

# Rendimiento esperado anual del mercado
market_return = benchmark_returns_df.mean().item() * 252

for stock in tickers:
      # Unir X (benchmark) y y (stock) en un solo DataFrame con fechas alineadas
    temp_df = pd.concat([benchmark_returns_df, returns_df[stock]], axis=1, join='inner').dropna()
    temp_df.columns = ['Benchmark', 'Stock']

    X = sm.add_constant(temp_df['Benchmark'])  # Agregar constante
    y = temp_df['Stock']

    model = sm.OLS(y, X).fit()
    beta = model.params[1]
    betas[stock] = beta
    expected_return = rf + beta * (market_return - rf)
    expected_returns_capm[stock] = expected_return

# === Mostrar resultados en un DataFrame ===
capm_df = pd.DataFrame({
    'Beta': betas,
    'CAPM Expected Return': expected_returns_capm
})

# Convertir a porcentajes
capm_df['CAPM Expected Return (%)'] = capm_df['CAPM Expected Return'] * 100

# Mostrar
print("\n=== Rendimiento esperado por CAPM ===\n")
print(capm_df)

#segundo metodo para calcular CAPM
betas = {}
for accion in tickers:
    cov = np.cov(rendimientos_acciones[accion].values, rendimiento_mercado.values)[0,1]
    var = np.var(rendimiento_mercado.values)
    betas[accion] = cov / var

# Calcular rendimientos esperados usando CAPM
rendimiento_mercado_anual = rendimiento_mercado.mean() * 252
rendimientos_esperados = {}
for accion in tickers:
    E_Ri = rf + betas[accion] * (rendimiento_mercado_anual - rf)
    rendimientos_esperados[accion] = E_Ri
    print(f"Rendimiento esperado de {accion}: {E_Ri}")
print (betas)




#Optimización del portafolio
num_portfolios = 3000
valid_portfolios = 0
max_portfolios = num_portfolios
n_assets = len(tickers)

portf_rtns = []
portf_vol = []
portf_sharpe_ratio = []
portf_betas = []
portf_weights = []

beta_vector = np.array([betas[ticker] for ticker in tickers])  # vector de betas individuales

while valid_portfolios < max_portfolios:
    w = np.random.random(n_assets)
    w /= np.sum(w)  # Restricción 1: suma de pesos = 1
    portf_beta = np.dot(w, beta_vector)
    
    if portf_beta < 1:  # Restricción 3: beta < 1
        rtn = np.dot(w, avg_returns)
        vol = np.sqrt(np.dot(w.T, np.dot(cov_mat, w)))
        sharpe = rtn / vol

        portf_rtns.append(rtn)
        portf_vol.append(vol)
        portf_sharpe_ratio.append(sharpe)
        portf_betas.append(portf_beta)
        portf_weights.append(w)

        valid_portfolios += 1

# Convertir a DataFrame
portf_results_df = pd.DataFrame({
    'returns': portf_rtns,
    'volatility': portf_vol,
    'sharpe_ratio': portf_sharpe_ratio,
    'beta': portf_betas
})

# Encontrar portafolio óptimo (máxima Sharpe con beta < 1)
max_sharpe_ind = np.argmax(portf_results_df.sharpe_ratio)
max_sharpe_portf = portf_results_df.loc[max_sharpe_ind]
best_weights = portf_weights[max_sharpe_ind]

print('Maximum Sharpe Ratio Portfolio (with beta < 1)')
print('Performance:')
for index, value in max_sharpe_portf.items():
    if index != 'sharpe_ratio':
        print(f'\n{index}: {100 * value:.2f}%' if index != 'beta' else f'\n{index}: {value:.2f}', end="")
    else:
        print(f'\n{index}: {value:.2f}', end="")

print('\n\nWeights:')
for x, y in zip(tickers, best_weights):
    print(f'{x}: {100 * y:.2f}%', end=" ")
