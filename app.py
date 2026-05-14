import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Modelo Gordon Growth", layout="wide")

# Estilos personalizados en azul, naranja y verde
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #f0f8ff; /* azul claro */
    }
    .stButton>button {
        background-color: #ff8c00; /* naranja intenso */
        color: white;
        font-weight: bold;
    }
    .stMetric {
        background-color: #000000; /* fondo negro */
        color: #ffffff; /* letras blancas */
        padding: 10px;
        border-radius: 8px;
    }
    .stSuccess {
        color: #006400; /* verde fuerte */
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Modelo Gordon Growth Interactivo")

# Inputs en el marco lateral
st.sidebar.header("🔧 Parámetros de entrada")
dividendo_actual = st.sidebar.number_input("Dividendo actual (D0)", value=4.80, step=0.01)
g = st.sidebar.number_input("Tasa de crecimiento del dividendo (%)", value=5.5, step=0.1)
precio = st.sidebar.number_input("Precio de la acción (P)", value=42.09, step=0.01)

# Botón para correr el cálculo
if st.sidebar.button("Calcular Costo de Capital (Ke)"):
    # Cálculo del dividendo esperado
    D1 = dividendo_actual * (1 + g/100)

    # Fórmula Gordon Growth Model: Ke = (D1 / P) + g
    ke = (D1 / precio) + (g / 100)

    st.subheader("📈 Resultado del Gordon Growth Model")
    st.metric(label="Costo de capital (Ke)", value=f"{round(ke*100, 2)} %")
    st.success("✅ Cálculo completado")
else:
    st.info("Introduce los parámetros y presiona **Calcular Costo de Capital**")
