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
rf = st.sidebar.number_input("Tasa libre de riesgo (%)", value=2.0, step=0.1)
beta = st.sidebar.number_input("Beta", value=1.0, step=0.1)
rm = st.sidebar.number_input("Rendimiento de mercado (%)", value=8.0, step=0.1)

# Botón para correr el cálculo
if st.sidebar.button("Calcular Gordon Growth"):
    # Fórmula CAPM para calcular el costo de capital (Ke)
    ke = rf + beta * (rm - rf)

    # Fórmula Gordon Growth Model: P = D1 / (Ke - g)
    # Para simplificar, asumimos D1 = 1 y g = 2%
    D1 = 1.0
    g = 0.02
    if ke > g:
        price = D1 / (ke/100 - g)
        st.subheader("📈 Resultado del Gordon Growth Model")
        st.metric(label="Precio estimado de la acción", value=round(price, 2))
        st.success("✅ Cálculo completado")
    else:
        st.error("❌ El costo de capital debe ser mayor al crecimiento (g).")
else:
    st.info("Introduce los parámetros y presiona **Calcular Gordon Growth**")
