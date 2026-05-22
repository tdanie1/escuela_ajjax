import streamlit as st

# Configuración inicial
st.set_page_config(page_title="Escuela de Patinaje", layout="wide")

# Sidebar con menú principal
menu_principal = st.sidebar.radio(
    "Menú Principal",
    ["INICIO", "DEPORTISTA", "PAGOS", "TIENDA", "EVENTOS", "CLUB", "NOSOTROS"]
)

# Renderizado según menú seleccionado
if menu_principal == "INICIO":
    st.title("🏆 Escuela de Patinaje")
    st.write("Bienvenido a la aplicación de la Escuela de Patinaje")

    # Submenús horizontales con tabs
    tabs = st.tabs(["Presentación", "Video Introductorio", "Contacto"])
    with tabs[0]:
        st.subheader("Presentación")
        st.write("Aquí puedes mostrar información general de la escuela.")
    with tabs[1]:
        st.subheader("Video Introductorio")
        st.video("intro.mp4")
    with tabs[2]:
        st.subheader("Contacto")
        st.markdown("[📲 WhatsApp](https://wa.me/573001234567)")

elif menu_principal == "DEPORTISTA":
    tabs = st.tabs(["Inscripciones", "Ficha Deportista", "Póliza", "Documentación"])
    with tabs[0]:
        st.header("Formulario de Inscripción")
        with st.form("inscripcion"):
            nombres = st.text_input("Nombres")
            apellidos = st.text_input("Apellidos")
            id_documento = st.text_input("Documento")
            ciclo = st.selectbox("Ciclo", ["Escuela", "Pre-Club", "Club Profesional"])
            enviar = st.form_submit_button("Registrar")
            if enviar:
                st.success("Inscripción registrada correctamente")
    with tabs[1]:
        st.header("Ficha Deportista")
        st.write("Aquí se mostrará la información del deportista.")
    with tabs[2]:
        st.header("Póliza")
        st.write("Consulta y carga de pólizas.")
    with tabs[3]:
        st.header("Documentación")
        st.write("Gestión de documentos asociados.")

elif menu_principal == "PAGOS":
    tabs = st.tabs(["Realizar Pago", "Subir Soporte", "Solicitud de Reembolso"])
    with tabs[0]:
        st.header("Pagos disponibles")
        st.write("QR, Bancolombia, Nequi, Daviplata")
    with tabs[1]:
        st.header("Subir soporte de pago")
        soporte = st.file_uploader("Cargar soporte", type=["pdf","jpg","png"])
    with tabs[2]:
        st.header("Solicitud de Reembolso")
        st.text_area("Motivo de la solicitud")

elif menu_principal == "TIENDA":
    tabs = st.tabs(["Catálogo", "Carrito", "Historial de Compras"])
    with tabs[0]:
        st.header("🛒 Catálogo de productos")
        st.write("Aquí se mostrarán los artículos disponibles.")
    with tabs[1]:
        st.header("Carrito de compras")
    with tabs[2]:
        st.header("Historial de compras")

elif menu_principal == "EVENTOS":
    tabs = st.tabs(["Competencias", "Calendarios", "Galerías", "Noticias"])
    for i, nombre in enumerate(["Competencias", "Calendarios", "Galerías", "Noticias"]):
        with tabs[i]:
            st.header(nombre)
            st.write(f"Sección seleccionada: {nombre}")

elif menu_principal == "CLUB":
    tabs = st.tabs(["Historia", "Resoluciones", "Reglamento", "Manual de convivencia", "Nuestra misión"])
    for i, nombre in enumerate(["Historia", "Resoluciones", "Reglamento", "Manual de convivencia", "Nuestra misión"]):
        with tabs[i]:
            st.header(nombre)
            st.write(f"Contenido de {nombre}")

elif menu_principal == "NOSOTROS":
    tabs = st.tabs(["Nuestro equipo", "Política de datos", "PQRS", "Contáctanos"])
    for i, nombre in enumerate(["Nuestro equipo", "Política de datos", "PQRS", "Contáctanos"]):
        with tabs[i]:
            st.header(nombre)
            st.write(f"Sección seleccionada: {nombre}")
