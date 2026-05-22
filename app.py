import streamlit as st

# Configuración inicial
st.set_page_config(page_title="Escuela de Patinaje", layout="wide")

# Sidebar principal
menu_principal = st.sidebar.radio(
    "Menú Principal",
    ["INICIO", "DEPORTISTA", "PAGOS", "TIENDA", "EVENTOS", "CLUB", "NOSOTROS"]
)

# Renderizado según menú seleccionado
if menu_principal == "INICIO":
    st.title("🏆 Escuela de Patinaje")
    st.write("Bienvenido a la aplicación de la Escuela de Patinaje")
    st.video("intro.mp4")  # video introductorio
    st.markdown("[📲 WhatsApp](https://wa.me/573001234567)")

elif menu_principal == "DEPORTISTA":
    submenu = st.sidebar.radio(
        "Opciones Deportista",
        ["Inscripciones", "Ficha Deportista", "Póliza", "Documentación"]
    )
    if submenu == "Inscripciones":
        st.header("Formulario de Inscripción")
        with st.form("inscripcion"):
            nombres = st.text_input("Nombres")
            apellidos = st.text_input("Apellidos")
            id_documento = st.text_input("Documento")
            ciclo = st.selectbox("Ciclo", ["Escuela", "Pre-Club", "Club Profesional"])
            enviar = st.form_submit_button("Registrar")
            if enviar:
                st.success("Inscripción registrada correctamente")

elif menu_principal == "PAGOS":
    submenu = st.sidebar.radio(
        "Opciones de Pago",
        ["Realizar Pago", "Subir Soporte", "Solicitud de Reembolso"]
    )
    if submenu == "Realizar Pago":
        st.header("Pagos disponibles")
        st.write("QR, Bancolombia, Nequi, Daviplata")

elif menu_principal == "TIENDA":
    st.header("🛒 Catálogo de productos")
    st.write("Aquí se mostrarán los artículos disponibles.")

elif menu_principal == "EVENTOS":
    submenu = st.sidebar.radio(
        "Eventos",
        ["Competencias", "Calendarios", "Galerías", "Noticias"]
    )
    st.write(f"Sección seleccionada: {submenu}")

elif menu_principal == "CLUB":
    submenu = st.sidebar.radio(
        "Club",
        ["Historia", "Resoluciones", "Reglamento", "Manual de convivencia", "Nuestra misión"]
    )
    st.write(f"Sección seleccionada: {submenu}")

elif menu_principal == "NOSOTROS":
    submenu = st.sidebar.radio(
        "Nosotros",
        ["Nuestro equipo", "Política de datos", "PQRS", "Contáctanos"]
    )
    st.write(f"Sección seleccionada: {submenu}")
