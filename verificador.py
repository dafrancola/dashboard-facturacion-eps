import streamlit as st

st.title("🔍 Verificador de instalación")

try:
    import plotly.express as px
    st.success("✅ plotly está instalado correctamente.")
except ImportError as e:
    st.error(f"❌ plotly NO está instalado.\n\n{e}")
