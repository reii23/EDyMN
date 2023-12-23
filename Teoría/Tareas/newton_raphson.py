import sympy as sp

def NR(f, x0, tolerancia=1e-7, max_iter=90):
    x = sp.symbols('x')
    df = sp.diff(f, x)
    funcion = sp.lambdify(x, f, 'numpy')
    derivada_funcion = sp.lambdify(x, df, 'numpy')
    xn = x0
    for i in range(max_iter):
        fn = funcion(xn)
        if abs(fn) < tolerancia:
            return xn
        dfn = derivada_funcion(xn)
        xn = xn - (fn / dfn)
    raise ValueError("ERROR, no se pudo encontrar una raiz")

x = sp.symbols('x')
funcion = x**3 - x - 2  # cambiar esta función en caso de querer evaluar otra
raiz = NR(funcion, x0 = 1)
print("La raíz es:", raiz)
