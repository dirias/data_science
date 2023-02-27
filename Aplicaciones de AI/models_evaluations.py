from sklearn.linear_model import LinearRegression
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from pmdarima.arima import auto_arima
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error
import pandas as pd

# cargar los datos históricos y de prueba
historico = pd.read_csv("datos_historicos.csv")
prueba = pd.read_csv("datos_prueba.csv")

# modelo de regresión múltiple
regresion = LinearRegression()
regresion.fit(historico[["variable1", "variable2", "variable3"]], historico["objetivo"])
prediccion_regresion = regresion.predict(prueba[["variable1", "variable2", "variable3"]])
mape_regresion = mean_absolute_percentage_error(prueba["objetivo"], prediccion_regresion)
mse_regresion = mean_squared_error(prueba["objetivo"], prediccion_regresion)

# modelo de Holt-Winters
holt_winters = ExponentialSmoothing(historico["objetivo"], seasonal_periods=12, trend="add", seasonal="add")
holt_winters.fit()
prediccion_holt_winters = holt_winters.forecast(len(prueba))
mape_holt_winters = mean_absolute_percentage_error(prueba["objetivo"], prediccion_holt_winters)
mse_holt_winters = mean_squared_error(prueba["objetivo"], prediccion_holt_winters)

# modelo SARIMA
sarima = auto_arima(historico["objetivo"], seasonal=True, m=12, trace=True)
prediccion_sarima = sarima.predict(n_periods=len(prueba))
mape_sarima = mean_absolute_percentage_error(prueba["objetivo"], prediccion_sarima)
mse_sarima = mean_squared_error(prueba["objetivo"], prediccion_sarima)

# imprimir los resultados
print("MAPE regresión múltiple:", mape_regresion)
print("MSE regresión múltiple:", mse_regresion)
print("MAPE Holt-Winters:", mape_holt_winters)
print("MSE Holt-Winters:", mse_holt_winters)
print("MAPE SARIMA:", mape_sarima)
print("MSE SARIMA:", mse_sarima)
#En este ejemplo, se ajustan tres modelos diferentes y se calculan el MAPE y MSE para cada uno de ellos. Los resultados se imprimen en la consola. El modelo que tenga el MAPE y MSE más bajo será el mejor modelo según estas métricas. Sin embargo, es importante tener en cuenta que otras métricas y factores también pueden ser importantes al seleccionar el mejor modelo para un conjunto de datos específico.




