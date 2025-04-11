
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

x = np.array([350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500]).reshape(-1, 1)
y = np.array([70, 75, 78, 82, 85, 90, 95, 100, 105, 110, 115, 120, 130, 140, 150, 160])

model = LinearRegression()
model.fit(x, y)
predicted_y = model.predict(x)

r2 = r2_score(y, predicted_y)

plt.scatter(x, y, color='blue', label='Actual')
plt.plot(x, predicted_y, color='red', label='Predicted')
plt.xlabel('Sensor Reading')
plt.ylabel('Glucose Level (mg/dL)')
plt.legend()
plt.title('Glucose Prediction using MQ-138 Sensor')
plt.show()

print("R-Squared Value:", r2)
