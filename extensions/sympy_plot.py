from sympy import symbols
from sympy.plotting import plot
z = symbols('z')

def sympy_plot(function):
    f = function(z)
    plot(f)
