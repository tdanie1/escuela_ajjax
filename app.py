import streamlit as st

# Configuración inicial
st.set_page_config(page_title="Club de Patinaje AJJAX", layout="wide")

# Encabezado en el sidebar
st.sidebar.markdown(
    "<h1 style='text-align: center; color: #2E86C1;'>🏆 Club de Patinaje AJJAX</h1>",
    unsafe_allow_html=True
)

# Menú principal en sidebar con más espacio y estilo
menu_principal = st.sidebar.selectbox(
    "",
    ["INICIO", "DEPORTISTA", "PAGOS", "TIENDA", "EVENTOS", "CLUB", "NOSOTROS"],
    format_func=lambda x: f"➡️ {x}"
)

# Íconos de redes sociales en círculo
st.sidebar.markdown(
    """
    <div style='text-align: center; margin-top: 30px;'>
        <a href='https://facebook.com' target='_blank'>
            <img src='https://cdn-icons-png.flaticon.com/512/733/733547.png' width='40' style='border-radius:50%; margin:8px;'>
        </a>
        <a href='https://instagram.com' target='_blank'>
            <img src='https://cdn-icons-png.flaticon.com/512/2111/2111463.png' width='40' style='border-radius:50%; margin:8px;'>
        </a>
        <a href='https://wa.me/573001234567' target='_blank'>
            <img src='https://cdn-icons-png.flaticon.com/512/733/733585.png' width='40' style='border-radius:50%; margin:8px;'>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# Renderizado según menú seleccionado
if menu_principal == "INICIO":
    st.title("Bienvenido al Club de Patinaje AJJAX")
    tabs = st.tabs(["Presentación", "Video Introductorio", "Contacto"])
    with tabs[0]:
        st.subheader("Presentación")
        st.write("Información general del club.")
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
        st.write("Aquí se gestionará el carrito.")
    with tabs[2]:
        st.header("Historial de compras")
        st.write("Listado de compras anteriores.")

elif menu_principal == "EVENTOS":
    tabs = st.tabs(["Competencias", "Calendarios", "Galerías", "Noticias"])
    with tabs[0]:
        st.header("Competencias")
        st.write("Información sobre competencias.")
    with tabs[1]:
        st.header("Calendarios")
        st.write("Calendario de actividades.")
    with tabs[2]:
        st.header("Galerías")
        st.write("Fotos y videos de eventos.")
    with tabs[3]:
        st.header("Noticias")
        st.write("Últimas novedades del club.")

elif menu_principal == "CLUB":
    tabs = st.tabs(["Historia", "Resoluciones", "Reglamento", "Manual de convivencia", "Nuestra misión"])
    with tabs[0]:
        st.header("Historia")
        st.write("Reseña histórica del club.")
    with tabs[1]:
        st.header("Resoluciones")
        st.write("Resoluciones oficiales.")
    with tabs[2]:
        st.header("Reglamento")
        st.write("Normas del club.")
    with tabs[3]:
        st.header("Manual de convivencia")
        st.write("Reglas de convivencia.")
    with tabs[4]:
        st.header("Nuestra misión")
        st.write("Misión y visión del club.")

elif menu_principal == "NOSOTROS":
    tabs = st.tabs(["Nuestro equipo", "Política de datos", "PQRS", "Contáctanos"])
    with tabs[0]:
        st.header("Nuestro equipo")
        st.write("Información sobre el equipo de trabajo.")
    with tabs[1]:
        st.header("Política de datos")
        st.write("Política de tratamiento de datos personales.")
    with tabs[2]:
        st.header("PQRS")
        st.write("Formulario de Peticiones, Quejas, Reclamos y Sugerencias.")
    with tabs[3]:
        st.header("Contáctanos")
        st.write("Información de contacto del club.")

