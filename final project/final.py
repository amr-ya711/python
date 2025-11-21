# 1) Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 2) Load Dataset

df = pd.read_csv("Salary_Data.csv")   # لازم الملف يكون جنب final.py
print("First 5 rows:")
print(df.head())

# 3) Dataset Info

print("\nDataset Info:")
print(df.info())
print("\nMissing Values:")
print(df.isna().sum())
df = df.dropna()

# 4) Plot 1 — Scatter Plot

plt.figure("Experience vs Salary")   
plt.scatter(df["YearsExperience"], df["Salary"])
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Experience vs Salary")
plt.show(block=False)   # افتح أول نافذة من غير ما توقف البرنامج

# 5) Linear Regression Model

X = df[["YearsExperience"]]
y = df["Salary"]
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, Y_train)
y_pred = model.predict(X_test)

print("\nModel Evaluation:")
print("Mean Squared Error (MSE):", mean_squared_error(Y_test, y_pred))
print("R²:", r2_score(Y_test, y_pred))

# 6) Plot 2 — Regression Line

plt.figure("Linear Regression Fit")  
plt.scatter(df["YearsExperience"], df["Salary"], label="Data")
plt.plot(df["YearsExperience"], model.predict(df[["YearsExperience"]]), 
         color="red", label="Regression Line")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Linear Regression Fit")
plt.legend()
plt.show()   
