def gauss_seidel(A, b, initial_guess=None, tol=1e-10, max_iter=100):
    n = len(b)
    x = initial_guess or [0] * n
    num_iterations = 0

    while num_iterations < max_iter:
        x_old = x[:]
        for i in range(n):
            sigma = sum(A[i][j] * x[j] for j in range(i)) + sum(A[i][j] * x_old[j] for j in range(i + 1, n))
            x[i] = (b[i] - sigma) / A[i][i]
        if max(abs(x[i] - x_old[i]) for i in range(n)) < tol:
            return x, num_iterations
        num_iterations += 1

    return x, num_iterations
A = [
    [83, 11, -4],
    [7, 52, 13],
    [3, 8, 29]
]
b = [95, 104, 71]

initial_guess = [0, 0, 0]
solution, iterations = gauss_seidel(A, b, initial_guess)
print("Approximate solution:", solution)
print("Number of iterations:", iterations)
