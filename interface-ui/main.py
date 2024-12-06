import flet as ft


def main(page: ft.Page):
    # Establecer tamaño de ventana por defecto
    page.window_width = 800  # Ancho
    page.window_height = 600  # Alto
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Centrar horizontalmente
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Centrar verticalmente

    # Datos mockeados de rendimientos
    mock_rendimientos = [
        {"nombre": "Bitcoin", "inicial": 30000, "actual": 35000},
        {"nombre": "Ethereum", "inicial": 2000, "actual": 1800},
        {"nombre": "Solana", "inicial": 20, "actual": 25},
    ]

    # Función para calcular el porcentaje de cambio
    def calcular_cambio_porcentaje(inicial, actual):
        return ((actual - inicial) / inicial) * 100

    # Filtrar rendimientos
    def filtrar_rendimientos(e):
        filtro = search_box.value.lower()
        tabla_rendimientos.controls.clear()
        tabla_rendimientos.controls.append(fila_encabezado)  # Agregar encabezados
        for item in mock_rendimientos:
            if filtro in item["nombre"].lower():
                tabla_rendimientos.controls.append(crear_fila_rendimiento(item))
        page.update()

    # Crear fila para cada rendimiento
    def crear_fila_rendimiento(item):
        cambio_porcentaje = calcular_cambio_porcentaje(item["inicial"], item["actual"])
        es_positivo = cambio_porcentaje >= 0

        return ft.Row(
            [
                ft.Text(item["nombre"], size=16),
                ft.Text(f"${item['inicial']:.2f}", size=14),
                ft.Text(f"${item['actual']:.2f}", size=14),
                ft.Text(
                    f"{cambio_porcentaje:.2f}%",
                    size=14,
                    color=ft.colors.GREEN if es_positivo else ft.colors.RED,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            spacing=20,
        )

    # Crear fila de encabezado
    fila_encabezado = ft.Row(
        [
            ft.Text("Inversión", size=16, weight="bold"),
            ft.Text("Precio Original", size=16, weight="bold"),
            ft.Text("Precio Actual", size=16, weight="bold"),
            ft.Text("Rendimiento", size=16, weight="bold"),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        spacing=20,
    )

    # Caja de búsqueda
    search_box = ft.TextField(
        hint_text="Buscar criptomoneda...",
        on_change=filtrar_rendimientos,
    )

    # Contenedor de tabla
    tabla_rendimientos = ft.Column(
        [fila_encabezado]
        + [crear_fila_rendimiento(item) for item in mock_rendimientos],
        spacing=10,
    )

    # Agregar elementos a la página
    page.title = "Rendimientos Criptomonedas"
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Rendimientos de Criptomonedas", size=20, weight="bold"),
                    search_box,
                    ft.Divider(),
                    tabla_rendimientos,
                ],
                spacing=15,
                width=600,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,  # Centrar todo el contenedor en la pantalla
        )
    )


# Ejecutar la aplicación Flet
ft.app(target=main)
