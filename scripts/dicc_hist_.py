import matplotlib.pyplot as plt

def contar_vocales(texto: str) -> dict:
    """Cuenta la cantidad de veces que aparece cada vocal dentro de un texto."""
    histograma = {}
    histograma['a'] = texto.lower().count('a')
    histograma['e'] = texto.lower().count('e')
    histograma['i'] = texto.lower().count('i')
    histograma['o'] = texto.lower().count('o')
    histograma['u'] = texto.lower().count('u')
    return histograma

def visualizar_histograma_vocales(histograma: dict):
    """Visualiza el histograma de frecuencia de vocales como un gráfico de barras."""
    vocales = list(histograma.keys())
    frecuencias = list(histograma.values())

    plt.bar(vocales, frecuencias, color='skyblue')
    plt.title('Histograma de Frecuencia de Vocales')
    plt.xlabel('Vocales')
    plt.ylabel('Frecuencia')
    plt.show()

# Ejemplo de uso
texto_ejemplo = "Hola, cómo estás? Espero que todo esté bien."
resultado_histograma_vocales = contar_vocales(texto_ejemplo)
visualizar_histograma_vocales(resultado_histograma_vocales)
