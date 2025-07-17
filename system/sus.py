try:
    import scipy.stats
    print("scipy.stats está instalado.")
    print(f"Versão do SciPy: {scipy.__version__}")
except ImportError:
    print("scipy.stats NÃO está instalado ou não pode ser encontrado.")