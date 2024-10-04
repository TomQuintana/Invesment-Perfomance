import tkinter as tk
from tkinter import ttk


# Función para calcular el rendimiento
def calcular_rendimiento():
    try:
        inversion_inicial = float(inversion_entry.get())
        cotizacion_inicial = float(cotizacion_entry.get())
        cotizacion_actual = float(cotizacion_actual_entry.get())

        rendimiento = (
            (cotizacion_actual - cotizacion_inicial)
            * inversion_inicial
            / cotizacion_inicial
        )
        resultado_label.config(text=f"Rendimiento: ${rendimiento:.2f}")
    except ValueError:
        resultado_label.config(text="Por favor, ingresa valores numéricos válidos")


# Crear la ventana principal
root = tk.Tk()
root.title("Inversiones en Criptomonedas")
root.geometry("400x400")

# Crear un widget Notebook (pestañas)
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Crear los marcos (frames) para cada pestaña
tab_inversiones = ttk.Frame(notebook, width=400, height=300)
tab_rendimiento = ttk.Frame(notebook, width=400, height=300)
tab_add_investment = ttk.Frame(notebook, width=400, height=300)

# Empaquetar los frames
tab_inversiones.pack(fill="both", expand=True)
tab_rendimiento.pack(fill="both", expand=True)
tab_add_investment.pack(fill="both", expand=True)

# Agregar las pestañas al Notebook
notebook.add(tab_inversiones, text="Mis Inversiones")

notebook.add(tab_rendimiento, text="Calcular Rendimiento")

notebook.add(tab_add_investment, text="Agregar Inversion")

### Contenido de la pestaña "Mis Inversiones"
inversiones_label = ttk.Label(tab_inversiones, text="Tus Inversiones:")
inversiones_label.pack(pady=10)

# Ejemplo de inversiones
inversion_bitcoin = ttk.Label(tab_inversiones, text="Bitcoin: $2000 a $30,000 por BTC")
inversion_bitcoin.pack(pady=5)

inversion_ethereum = ttk.Label(tab_inversiones, text="Ethereum: $1000 a $2000 por ETH")
inversion_ethereum.pack(pady=5)

### Contenido de la pestaña "Calcular Rendimiento"
inversion_label = ttk.Label(tab_rendimiento, text="Inversión Inicial ($):")
inversion_label.pack(pady=5)
inversion_entry = ttk.Entry(tab_rendimiento)
inversion_entry.pack(pady=5)

cotizacion_label = ttk.Label(tab_rendimiento, text="Cotización de la Inversión ($):")
cotizacion_label.pack(pady=5)
cotizacion_entry = ttk.Entry(tab_rendimiento)
cotizacion_entry.pack(pady=5)

cotizacion_actual_label = ttk.Label(tab_rendimiento, text="Cotización Actual ($):")
cotizacion_actual_label.pack(pady=5)
cotizacion_actual_entry = ttk.Entry(tab_rendimiento)
cotizacion_actual_entry.pack(pady=5)

# Botón para calcular el rendimiento
calcular_button = ttk.Button(
    tab_rendimiento, text="Calcular Rendimiento", command=calcular_rendimiento
)
calcular_button.pack(pady=10)

# Resultado del cálculo
resultado_label = ttk.Label(tab_rendimiento, text="Rendimiento: $0.00")
resultado_label.pack(pady=10)

# Ejecutar la ventana principal
root.mainloop()
