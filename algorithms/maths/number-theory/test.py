from sympy import Symbol, Function, Limit, Eq

x = Symbol("x")
delta_x = Symbol("\\Delta{x}")
f = Function("f")

out = Eq(
    f(x).diff(x),
    Limit((f(x + delta_x) -f(x)) / delta_x, delta_x, 0)
)