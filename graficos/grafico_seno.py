import matplotlib.pyplot as plt

def graficar_funcion_seno(x, y, funcion):
    plt.plot(x, y)
    plt.title(f"Gráfica de y = {funcion}")
    plt.xlabel("x (radianes)")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()
