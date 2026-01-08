import streamlit as st
import matplotlib.pyplot as plt
from calculos.seno import resolver_funcion_seno

st.set_page_config(page_title="Sistema Función Seno", layout="centered")

st.title(" Sistema de Resolución de Funciones Seno")

st.write("""
Ingrese una función seno y el sistema mostrará:
- El procedimiento matemático
- La gráfica correspondiente
""")

funcion = st.text_input(
    "Ingrese la función seno (ejemplo: 2*sen(x), 3*sen(2*x + 1))",
    value="sen(x)"
)

if st.button("Resolver función"):
    try:
        x, y, funcion_simbolica, procedimiento = resolver_funcion_seno(funcion)

        st.subheader(" Procedimiento de resolución")
        st.text(procedimiento)

        st.subheader(" Gráfica de la función")
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title(f"y = {funcion_simbolica}")
        ax.set_xlabel("x (radianes)")
        ax.set_ylabel("y")
        ax.grid(True)

        st.pyplot(fig)

    except Exception:
        st.error("Error en la función ingresada. Use una sintaxis válida.")
