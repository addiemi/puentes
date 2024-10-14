import streamlit as st
import plotly.graph_objects as go
import math
import numpy as np

def es_par(n):
    """Función que verifica si un número es par."""
    return n % 2 == 0

def calcular_soluciones(a, b, c):
    """Calcula las soluciones de una ecuación cuadrática."""
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return None  # No hay soluciones reales
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return (x1, x2)

def main():
    st.set_page_config(page_title="Simulación de Puente", layout="centered")
    st.title("🏗️ Simulación de Puente con Distribución de Peso")
    
    # Sección de Instrucciones
    st.header("📋 Instrucciones para Usar la Aplicación")
    st.markdown("""    
    1. **Configurar los Parámetros del Puente**:
       - En la barra lateral, ajusta los valores de los coeficientes `a`, `b` y `c` para definir la forma del arco del puente.
       
    2. **Visualizar las Soluciones**:
       - La aplicación calculará las soluciones de la ecuación cuadrática y representará gráficamente el puente.
       
    3. **Evaluar las Soluciones**:
       - Usa los botones para verificar si alguna o todas las posiciones de los soportes son pares.
       
    4. **Interpretar el Gráfico**:
       - La **plataforma** del puente está representada por una línea negra.
       - El **arco** del puente está representado por una línea roja.
       
            
    5. **Experimentos**:
       - Cambia los valores de `a`, `b` y `c` para ver cómo afecta la estructura del puente y sus soportes.
    """)
    
    st.sidebar.header("🔧 Parámetros del Puente")
    
    # Entradas del usuario para los coeficientes de la ecuación cuadrática
    a = st.sidebar.number_input("Coeficiente a (curvatura del arco)", value=1)
    b = st.sidebar.number_input("Coeficiente b (altura máxima del arco)", value=-4)
    c = st.sidebar.number_input("Coeficiente c (posición del arco)", value=0)
    
    # Mostrar la ecuación en un cuadro subrayado
    st.markdown("### La ecuación del arco del puente es:")
    st.markdown(f"<h2 style='text-align: center; text-decoration: underline;'>{a}x² + ({b})x + ({c}) = 0</h2>", unsafe_allow_html=True)
    
    soluciones = calcular_soluciones(a, b, c)
    
    if soluciones:
        st.subheader("📊 Soluciones de la Ecuación")
        st.write(f"Solución 1: {soluciones[0]}")
        st.write(f"Solución 2: {soluciones[1]}")
        
        es_par_1 = es_par(soluciones[0])
        es_par_2 = es_par(soluciones[1])


        st.subheader("🔍 Evaluación de las Soluciones")
        st.write(f"La posición del primer soporte es {'par' if es_par_1 else 'impar'}.")
        st.write(f"La posición del segundo soporte es {'par' if es_par_2 else 'impar'}.")
        
        # Gráfico del puente usando Plotly
        fig = go.Figure()
        
        # Dibujar la carretera del puente
        fig.add_trace(go.Scatter(x=[soluciones[0], soluciones[1]], y=[0, 0],
                                 mode='lines',
                                 name='Plataforma',
                                 line=dict(color='black', width=4)))
        
        # Dibujar el arco del puente usando la ecuación cuadrática
        x_vals = np.linspace(min(soluciones) - 1, max(soluciones) + 1, 100)  # Rango más amplio
        y_vals = a * x_vals**2 + b * x_vals + c  # Ecuación del arco
        fig.add_trace(go.Scatter(x=x_vals, y=y_vals,
                                 mode='lines',
                                 name='Arco',
                                 line=dict(color='red', width=3)))
        
        # Configurar la gráfica
        fig.update_layout(title='Representación Simplificada del Puente',
                          xaxis_title='Posición (metros)',
                          yaxis_title='Altura (metros)',
                          showlegend=True,
                          width=700,
                          height=400)
        
        st.plotly_chart(fig)
        
        # Botones para evaluaciones
        if st.button("✅ ¿Existe alguna solución par?"):
            if es_par_1 or es_par_2:
                st.success("¡Sí! Al menos una de las posiciones de los soportes es par.")
            else:
                st.error("Ninguna de las posiciones es par.")
        
        if st.button("✅ ¿Son todas las posiciones pares?"):
            if es_par_1 and es_par_2:
                st.success("¡Sí! Ambas posiciones de los soportes son pares.")
            else:
                st.error("No, no todas las posiciones son pares.")
    else:
        st.error("La ecuación del arco del puente no tiene soluciones reales.")

if __name__ == "__main__":
    main()
