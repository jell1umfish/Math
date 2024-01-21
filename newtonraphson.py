def newton_raphson(func, derivative, initial_guess, tol=1e-10, max_iter=100):
    x = initial_guess
    num_iterations = 0

    while num_iterations < max_iter:
        x_old = x
        x = x - func(x) / derivative(x)
        if abs(x - x_old) < tol:
            return x, num_iterations
        num_iterations += 1

    return x, num_iterations
def my_function(x):
    return x**3 - 3*x +1
def my_derivative(x):
    return 3*x**2 -3

initial_guess = 3

result, iterations = newton_raphson(my_function, my_derivative, initial_guess)

print("Approximate root:", result)
print("Number of iterations:", iterations)
