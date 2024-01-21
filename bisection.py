import math

def bisection_method(func, a, b, tol=1e-3, max_iter=100):

    if func(a) * func(b) > 0:
        raise ValueError("The function values at the interval endpoints must have opposite signs.")

    iterations = 0
    while (b - a) / 2 > tol and iterations < max_iter:
        c = (a + b) / 2
        if func(c) == 0:
            return c, iterations
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c

        iterations += 1

    root = (a + b) / 2
    return round(root, 3), iterations

def target_function(x):
    return x**3 - x - 1

a, b = 0, 3

solution, num_iterations = bisection_method(target_function, a, b)

print(f"Approximate root: {solution}")
print(f"Number of iterations: {num_iterations}")
