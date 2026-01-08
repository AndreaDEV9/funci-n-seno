import numpy as np
import sympy as sp

def resolver_funcion_seno(funcion_texto, inicio=-2*np.pi, fin=2*np.pi, puntos=200):
    x = sp.symbols('x')

    # Reemplazar sen por sin
    funcion_texto = funcion_texto.replace("sen", "sin")

    funcion = sp.sympify(funcion_texto)

    # Extraer coeficientes
    a = funcion.as_coeff_Mul()[0]
    resto = funcion / a

    b = resto.args[0].coeff(x) if resto.has(x) else 1
    c = resto.args[0].subs(x, 0) if resto.has(x) else 0

    # Dominio y rango
    dominio = "ℝ"
    rango_min = -abs(a)
    rango_max = abs(a)

    # Crear función numérica
    funcion_numerica = sp.lambdify(x, funcion, "numpy")

    x_vals = np.linspace(inicio, fin, puntos)
    y_vals = funcion_numerica(x_vals)

    procedimiento = f"""
1. Función ingresada:
   y = {funcion}

2. Forma general:
   y = a·sen(bx + c)

3. Identificación de parámetros:
   a = {a}  → amplitud
   b = {b}  → frecuencia
   c = {c}  → desplazamiento horizontal

4. Dominio:
   {dominio}

5. Rango:
   [{rango_min}, {rango_max}]

6. Evaluación:
   Se reemplazan los valores de x en la función
   y = {funcion}

7. Interpretación:
   La gráfica es una onda senoidal con amplitud {abs(a)}
"""

    return x_vals, y_vals, funcion, procedimiento
