import numpy as np
import matplotlib.pyplot as plt

def numerical_derivative (f, x, h):
    derivative = (f(x + h) - f(x - h)) / (2 * h)
    return derivative

if __name__ == "__main__":
    
    x = np.linspace (0, 2 * np.pi, 100)
    
    h = 0.01
    
    
    sin_numerical = numerical_derivative(np.sin, x, h)
    
    #deriv of sin is cos
    sin_known = np.cos(x)
    
    
    
    #plotting sin deriv
    plt.figure()
    plt.plot(x, sin_numerical, label="Numerical Derivative")
    plt.plot(x, sin_known, label="known_derivative")
    plt.xlabel ("x")
    plt.ylabel("f(x)")
    plt.title("Derivative of sin(x)")
    plt.show()
    
    
    
    
    
    #cos function
    
    cos_numerical = numerical_derivative(np.cos, x, h)
    
    # deriv of cos is -sin
    cos_known = -np.sin(x)
    
    #plotting cos deriv
    plt.figure()
    plt.plot(x, cos_numerical, label="Numerical Derivative")
    plt.plot(x, cos_known, label="Known derivative")
    plt.xlabel("x")
    plt.ylabel("f'(x)")
    plt.title("Derivative of cos(x)")
    plt.show()
    
    step_sizes = np.logspace(0, -6, 50)
    
    errors = []
    x_Val = 0
    for h in step_sizes:
        numerical = numerical_derivative(np.sin, x_Val, h)
        
        known = np.cos(x_Val)
        
        error = np.abs(numerical - known)
        
        errors.append(error)
        
    plt.figure()
        
        
    plt.loglog(step_sizes, errors, "o")
        
    reference = errors[0] * (step_sizes / step_sizes[0]) **2
        
    plt.loglog (step_sizes, reference)
        
    plt.xlabel("Step size h")
    plt.ylabel("Error")
    plt.title("3 point Derivative Error")
    plt.show()
