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

if __name__ == "__main__":
    matrix_data = [
        # [1, 2, 3, 4],
        # [0, 1, 2, 3],
        # [0, 0, 1, 2],
        # [0, 0, 0, 1]
        [1, 1],
        [1, 0]
    ]

    matrix = Matrix(matrix_data)
    basis = matrix.gram_schmidt_basis()

    for vector in basis:
        print(vector)
