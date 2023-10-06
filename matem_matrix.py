import numpy as np

class Matrix:
    def __init__(self, data):
        self.data = np.array(data)

    def gram_schmidt_basis(self):
        vectors = [self.data[:, i] for i in range(self.data.shape[1])]
        basis = []

        for vector in vectors:
            for orthogonal_vector in basis:
                projection = np.dot(vector, orthogonal_vector) / np.dot(orthogonal_vector, orthogonal_vector) * orthogonal_vector
                vector = vector - projection

            if not np.allclose(vector, 0):
                basis.append(vector)

        normalized_basis = [vector / np.linalg.norm(vector) for vector in basis]

        return normalized_basis

def input_matrix():
    while True:
        matrix_data = input("Введите матрицу в формате [[], [], ...]: ")
    
        try:
            matrix_data = eval(matrix_data)  # Преобразуем введенную строку в список списков
            if not isinstance(matrix_data, list):
                raise ValueError("Ошибка! Введите матрицу в правильном формате.")
            if not all(isinstance(row, list) for row in matrix_data):
                raise ValueError("Ошибка! Введите матрицу в правильном формате.")
            if not matrix_data:
                raise ValueError("Ошибка! Матрица не может быть пустой.")
            break
        except Exception as e:
            print(f"Ошибка: {e}")

    return matrix_data

if __name__ == "__main__":
    matrix_data = input_matrix()
    if matrix_data:
        matrix = Matrix(matrix_data)
        basis = matrix.gram_schmidt_basis()

        for vector in basis:
            print(vector)
