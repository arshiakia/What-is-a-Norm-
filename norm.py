import numpy as np


def calculate_norm(vector_or_matrix, norm_type='L2'):
    data = np.array(vector_or_matrix)

    if norm_type == 'L0':
        return np.count_nonzero(data)

    elif norm_type == 'L1':
        return np.sum(np.abs(data))

    elif norm_type == 'L2':
        return np.linalg.norm(data)

    elif norm_type == 'Linf':
        return np.max(np.abs(data))

    elif norm_type == 'Frobenius':
        return np.linalg.norm(data, 'fro')

    elif norm_type == 'Nuclear':
        if data.ndim == 1:
            raise ValueError("Nuclear norm is defined for matrices, not vectors.")
        return np.sum(np.linalg.svd(data, compute_uv=False))

    elif norm_type == 'Spectral':
        if data.ndim == 1:
            raise ValueError("Spectral norm is defined for matrices, not vectors.")
        return np.linalg.svd(data, compute_uv=False)[0]

    elif norm_type == 'Induced_L2':
        return induced_norm(data, p=2)

    elif norm_type == 'Induced_L1':
        return induced_norm(data, p=1)

    elif norm_type == 'Induced_Linf':
        return induced_norm(data, p=np.inf)

    else:
        raise ValueError(f"Unsupported norm type: {norm_type}")


def induced_norm(matrix, p=2):
    if p == 2:
        return np.linalg.svd(matrix, compute_uv=False)[0]
    elif p == 1:
        return np.max(np.sum(np.abs(matrix), axis=0))
    elif p == np.inf:
        return np.max(np.sum(np.abs(matrix), axis=1))
    else:
        raise ValueError(f"Unsupported p value for induced norm: {p}")


def get_matrix_from_user():
    rows = int(input("Enter the number of rows for the matrix: "))
    cols = int(input("Enter the number of columns for the matrix: "))

    matrix = []
    print(f"Enter the matrix values row by row:")
    for i in range(rows):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        if len(row) != cols:
            print(f"Row {i + 1} should have {cols} elements. Please try again.")
            return get_matrix_from_user()
        matrix.append(row)

    return matrix


def detect_and_calculate():
    while True:
        matrix = get_matrix_from_user()

        print("Choose a norm type:")
        print(
            "Available options: 'L0', 'L1', 'L2', 'Linf', 'Frobenius', 'Nuclear', 'Spectral', 'Induced_L2', 'Induced_L1', 'Induced_Linf'")
        norm_type = input("Enter norm type: ").strip()

        try:
            result = calculate_norm(matrix, norm_type)
            print(f"The {norm_type} norm of the input is: {result}")
        except ValueError as e:
            print(e)

        # Ask if the user wants to repeat the process
        repeat = input("Do you want to calculate another norm for a different matrix? (yes/no): ").strip().lower()
        if repeat != 'yes':
            print("Exiting program...")
            break


detect_and_calculate()
