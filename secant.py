import math
def secant_method(func, x0, x1, tol=1e-10, max_iter=100):
    num_iterations = 0

    while num_iterations < max_iter:
        f_x0 = func(x0)
        f_x1 = func(x1)

        if abs(f_x1 - f_x0) < tol:
            return round(x1, 6), num_iterations
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        if func(x2) == 0 or abs(x2 - x1) < tol:
            return round(x2, 6), num_iterations
        x0, x1 = x1, x2
        num_iterations += 1

    return round(x1, 6), num_iterations
def my_function(x):
    return 2*x**3 + x**2 - 20*x + 12
x0, x1 = 3, 4

result, iterations = secant_method(my_function, x0, x1)
print(f"Approximate root: {result}")
print(f"Number of iterations: {iterations}")
