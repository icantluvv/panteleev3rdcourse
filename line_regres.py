import numpy as np
import pandas as pd

# Загрузка данных из файла
data = pd.read_csv("insurance.csv")

# Предварительная обработка данных
# Преобразование категориальных признаков в числовые (например, пол и регион)
data = pd.get_dummies(data, columns=["sex", "region", "smoker"], drop_first=True)

# Нормализация числовых признаков
numeric_features = ["age", "bmi", "children"]
data[numeric_features] = (data[numeric_features] - data[numeric_features].mean()) / data[numeric_features].std()

# Разделение данных на обучающий и тестовый наборы
train_size = int(0.8 * len(data))
train_data = data[:train_size]
test_data = data[train_size:]

# Извлечение признаков и целевой переменной
X_train = train_data.drop("charges", axis=1).values
y_train = train_data["charges"].values
X_test = test_data.drop("charges", axis=1).values
y_test = test_data["charges"].values

# Добавление столбца с "единицами" для учета смещения
X_train = np.column_stack([np.ones(X_train.shape[0]), X_train])
X_test = np.column_stack([np.ones(X_test.shape[0]), X_test])

# Определение модели линейной регрессии
def linear_regression(X, theta):
    return np.dot(X, theta)

# Определение функции потерь (MSE)
def mean_squared_error(y, y_pred):
    return np.mean((y - y_pred) ** 2)

# Градиент функции потерь по параметрам модели
def gradient(X, y, y_pred):
    return np.dot(X.T, y_pred - y) / len(y)

# Градиентный спуск для обновления параметров модели
def gradient_descent(X, y, theta, learning_rate, num_iterations):
    for i in range(num_iterations):
        y_pred = linear_regression(X, theta)
        grad = gradient(X, y, y_pred)
        grad = grad.astype(np.float64)  # Привести grad к типу float64
        theta -= learning_rate * grad
    return theta


# Настройка параметров
learning_rate = 0.0001  # Уменьшили скорость обучения
num_iterations = 100000
theta = np.random.rand(X_train.shape[1])  # Инициализация случайными значениями

# Обучение модели
theta = gradient_descent(X_train, y_train, theta, learning_rate, num_iterations)

# Предсказание на тестовом наборе
y_pred_test = linear_regression(X_test, theta)

# Оценка модели (например, MSE)
mse = mean_squared_error(y_test, y_pred_test)
print("Mean Squared Error on Test Data:", mse)
