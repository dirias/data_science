import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error
import matplotlib.pyplot as plt

# Cargar los datos
data = pd.read_excel('EJEMPLO.xlsx', parse_dates=['FECHA'], index_col='FECHA')

# Dividir los datos en conjuntos de entrenamiento y prueba
train = data.loc['2015':'2017']
test = data.loc['2015']
# Modelo de regresión múltiple
X_train = np.array([np.arange(len(train)), train.index.month]).T
y_train = train['Facturacion'].values.reshape(-1, 1)
reg = LinearRegression().fit(X_train, y_train)

# Predecir los valores de prueba
X_test = np.array([np.arange(len(test)), test.index.month]).T
y_pred_reg = reg.predict(X_test)

# Calcular el MAPE y MSE para el modelo de regresión múltiple
mape_reg = mean_absolute_percentage_error(test['Facturacion'], y_pred_reg)
mse_reg = mean_squared_error(test['Facturacion'], y_pred_reg)
#import pdb; pdb.set_trace()

# Modelo de Holt Winters
hw_model = ExponentialSmoothing(train['Facturacion'], seasonal_periods=12, trend='add', seasonal='add').fit()

# Predecir los valores de prueba
y_pred_hw = hw_model.predict(start=test.index[0], end=test.index[-1])

# Calcular el MAPE y MSE para el modelo de Holt Winters
mape_hw = mean_absolute_percentage_error(test['Facturacion'], y_pred_hw)
mse_hw = mean_squared_error(test['Facturacion'], y_pred_hw)

# Modelo de SARIMA
sarima_model = SARIMAX(train['Facturacion'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12)).fit()

# Predecir los valores de prueba
y_pred_sarima = sarima_model.predict(start=test.index[0], end=test.index[-1])

# Calcular el MAPE y MSE para el modelo de SARIMA
mape_sarima = mean_absolute_percentage_error(test['Facturacion'], y_pred_sarima)
mse_sarima = mean_squared_error(test['Facturacion'], y_pred_sarima)

# Imprimir los resultados
print('MAPE Regresión Múltiple:', mape_reg)
print('MSE Regresión Múltiple:', mse_reg)
print('MAPE Holt Winters:', mape_hw)
print('MSE Holt Winters:', mse_hw)
print('MAPE SARIMA:', mape_sarima)
print('MSE SARIMA:', mse_sarima)

# Testing

# Datos
modelos = ['Regresión Múltiple', 'Holt Winters', 'SARIMA']
mape_scores = [mape_reg, mape_hw, mape_sarima]
mse_scores = [mape_reg, mse_hw, mse_sarima]

# Gráfico de barras para MAPE
plt.figure(figsize=(8, 6))
plt.bar(modelos, mape_scores, color='blue')
plt.title('MAPE Scores')
plt.xlabel('Modelos')
plt.ylabel('MAPE')
plt.ylim([0, 30])
plt.show()

# Gráfico de barras para MSE
plt.figure(figsize=(8, 6))
plt.bar(modelos, mse_scores, color='red')
plt.title('MSE Scores')
plt.xlabel('Modelos')
plt.ylabel('MSE')
plt.ylim([0, 300000000])
plt.show()

# Making projection for 2019# make forecast for 12 months (2019)

# Predecir los valores de 2019
start = pd.to_datetime('2019-01-01')
end = pd.to_datetime('2019-12-01')
y_pred_hw = hw_model.predict(start=start, end=end)

# Imprimir los valores proyectados para 2019
print(y_pred_hw)