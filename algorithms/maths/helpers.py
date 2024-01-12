from sympy import Symbol, Eq, Expr
from sympy.utilities.lambdify import implemented_function
from sympy import lambdify

import inspect

class Lambdified(Expr):

    def __init__(self, lhs, rhs, wrapped, symbols):
        self._lhs = lhs
        self._wrapped = wrapped
        self._rhs = rhs
        self._symbols = symbols

    def __call__(self, *args):
        return self._wrapped(*args)

    @property
    def printed(self):
        return Eq(
            self._lhs,
            self._rhs
        )

    def diff(self, only_lhs=False):
        new_lhs = self._lhs.diff()
        if only_lhs:
            new_rhs = self._rhs
        else:
            new_rhs = self._rhs.diff()
        return Lambdified(
            new_lhs,
            new_rhs,
            lambdify(self._symbols, new_lhs),
            self._symbols
        )


def lambdified(function) -> Lambdified:
    params = function.__code__.co_varnames

    f = implemented_function("f", function)

    symbols = [Symbol(it) for it in params]
    lhs = f(*symbols)
    wrapped = lambdify(symbols, lhs)
    rhs = wrapped(*symbols)

    return Lambdified(lhs, rhs, wrapped, symbols)