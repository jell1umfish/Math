def false_position_method(func, a, b, tol=1e-3, max_iter=100):

    if func(a) * func(b) > 0:
        raise ValueError("The function values at the interval endpoints must have opposite signs.")

    iterations = 0
    while iterations < max_iter:
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))
        
        if abs(func(c)) < tol:
            return round(c, 3), iterations
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
        iterations += 1

    root = (a * func(b) - b * func(a)) / (func(b) - func(a))
    return round(root, 3), iterations

# Example usage:
def target_function(x):
    return x**3 - 5*x + 1

# Set initial interval [a, b]
a, b = -2, 2

# Call false position method
solution, num_iterations = false_position_method(target_function, a, b)

# Display the result
print(f"Approximate root: {solution}")
print(f"Number of iterations: {num_iterations}")
