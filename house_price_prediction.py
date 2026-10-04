import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Sample Dataset Creation
np.random.seed(42)
size = np.random.randint(500, 3500, 100)
bedrooms = np.random.randint(1, 6, 100)
age = np.random.randint(1, 30, 100)

price = (size * 150) + (bedrooms * 10000) - (age * 500) + np.random.normal(0, 15000, 100)

data = pd.DataFrame({'Size_sqft': size, 'Bedrooms': bedrooms, 'Age_years': age, 'Price': price})

# Features and Target
X = data[['Size_sqft', 'Bedrooms', 'Age_years']]
y = data['Price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# 3. Predict
y_pred = model.predict(X_test)

# 4. Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R2 Score: {r2:.4f}")

# 5. Plot Results
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual vs Predicted House Prices')
plt.savefig('house_price_plot.png')
