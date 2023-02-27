import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("data_task1.csv")
# import pdb; pdb.set_trace()
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%b-%y')
df['mes'] = df['Fecha'].dt.month
df['año'] = df['Fecha'].dt.year
df = pd.concat([df, pd.get_dummies(df['mes'], prefix='mes')], axis=1)
df = pd.concat([df, pd.get_dummies(df['año'], prefix='año')], axis=1)

df['Datos'] = df['Datos'].apply(lambda x: float(x[:-1])/100)

X = df.drop(['Fecha', 'Datos', 'mes', 'año'], axis=1)
y = df['Datos']

reg = LinearRegression().fit(X, y)

y_pred = reg.predict(X)

rmse = np.sqrt(mean_squared_error(y, y_pred))
r2 = r2_score(y, y_pred)
print("Raíz del Error Cuadrático Medio:", rmse)
print("Coeficiente de Determinación (R2):", r2)

tendencia = reg.coef_[0] * X.index + reg.intercept_

plt.plot(X.index, y, 'o')
plt.plot(X.index, tendencia, '-', label='Tendencia')
plt.legend()
plt.show()

proyeccion = reg.predict(np.array([X.iloc[-1]]))[0]
print("Proyección:", proyeccion)