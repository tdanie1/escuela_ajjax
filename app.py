import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración inicial de la página
st.set_page_config(
    page_title="Club de Patinaje - Gestión Integral",
    page_icon="🛼",
    layout="wide"
)

# --- SIMULACIÓN DE BASE DE DATOS (MOCK DATA PARA DEPLOY INMEDIATO) ---
# En producción, aquí conectarías con st.connection("supabase", type="sql")
if 'deportistas' not in st.session_state:
    st.session_state.deportistas = []
if 'pagos' not in st.session_state:
    st.session_state.pagos = []
if 'tienda' not in st.session_state:
    st.session_state.tienda = [
        {"ref": "UNI-01", "producto": "Uniforme Oficial", "valor": 120000, "tallas": "S, M, L", "color": "Azul/Blanco"},
        {"ref": "LIC-02", "producto": "Licra de Entrenamiento", "valor": 45000, "tallas": "XS, S, M", "color": "Negro"}
    ]

st.title("🛼 Sistema de Gestión - Escuela de Patinaje")
st.markdown("Bienvenido al panel de control y administración de la escuela.")

# --- MENÚ DE NAVEGACIÓN PRINCIPAL ---
tabs = st.tabs(["📝 Inscripciones", "💰 Pagos", "🛍️ Tienda", "📅 Eventos & Noticias", "📈 Historial y Rendimiento", "🏢 El Club"])

# ==========================================
# MÓDULO 1: INSCRIPCIONES
# ==========================================
with tabs[0]:
    st.header("Formulario de Inscripción y Niveles")
    
    with st.form("form_inscripcion", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Datos Personales")
            doc = st.text_input("Documento de Identidad*")
            nombres = st.text_input("Nombres*")
            apellidos = st.text_input("Apellidos*")
            direccion = st.text_input("Dirección")
            barrio = st.text_input("Barrio")
            localidad = st.selectbox("Localidad", ["Usaquén", "Chapinero", "Santa Fe", "Suba", "Kennedy", "Bosa", "Otra"])
            tipo_estudio = st.radio("Institución Actual", ["Colegio", "Universidad", "Ninguno"])
            fecha_nac = st.date_input("Fecha de Nacimiento", min_value=datetime(1950, 1, 1))
            genero = st.selectbox("Género", ["Femenino", "Masculino", "Otro"])
            correo = st.text_input("Correo Electrónico")
            celular = st.text_input("Celular")
            nivel = st.selectbox("Nivel de Patinaje", ["Iniciación", "Intermedio", "Avanzado", "Alta Competencia"])
            
        with col2:
            st.subheader("Información Médica")
            eps = st.text_input("EPS")
            tipo_sangre = st.selectbox("Tipo de Sangre", ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"])
            estatura = st.number_input("Estatura (cm)", min_value=50, max_value=250, value=150)
            peso = st.number_input("Peso (kg)", min_value=10, max_value=150, value=50)
            enf_resp = st.checkbox("¿Sufre de enfermedad respiratoria?")
            gafas = st.checkbox("¿Usa gafas?")
            alergias = st.text_area("Alergias (si aplica)", placeholder="Ninguna")
            medicamentos = st.text_area("Medicamentos actuales", placeholder="Ninguno")
            centro_atencion = st.text_input("Centro de Atención de Emergencias Preferido")
            
            st.markdown("**Declaraciones Juradas**")
            acepta_infecto = st.checkbox("Acepto y declaro NO padecer enfermedades infectocontagiosas.")
            acepta_fisico = st.checkbox("Acepto y declaro NO tener impedimentos físicos para la práctica del patinaje.")

        st.divider()
        st.subheader("Información de Acudientes (Mínimo 1 Obligatorio)")
        col_acu1, col_acu2 = st.columns(2)
        with col_acu1:
            st.markdown("**Acudiente 1**")
            acu1_nom = st.text_input("Nombre Completo A1")
            acu1_parentesco = st.text_input("Parentesco A1")
            acu1_cel = st.text_input("Celular A1")
            acu1_correo = st.text_input("Correo A1")
        with col_acu2:
            st.markdown("**Acudiente 2 (Opcional)**")
            acu2_nom = st.text_input("Nombre Completo A2")
            acu2_parentesco = st.text_input("Parentesco A2")
            acu2_cel = st.text_input("Celular A2")
            acu2_correo = st.text_input("Correo A2")

        st.divider()
        st.subheader("Documentación Asociada (Soportes)")
        foto_perfil = st.file_uploader("Foto del Deportista", type=["jpg", "png", "jpeg"])
        doc_identidad = st.file_uploader("Copia Documento de Identidad (PDF/Imagen)", type=["pdf", "png", "jpg"])
        cert_eps = st.file_uploader("Certificado EPS", type=["pdf", "png", "jpg"])
        poliza = st.file_uploader("Póliza de Seguro", type=["pdf", "png", "jpg"])

        submit_inscripcion = st.form_submit_button("Registrar e Inscribir Deportista")
        
        if submit_inscripcion:
            if not doc or not nombres or not apellidos:
                st.error("Por favor llena los campos obligatorios (Documento, Nombres, Apellidos)")
            elif not acepta_infecto or not acepta_fisico:
                st.error("Debe aceptar las declaraciones médicas y físicas para continuar.")
            else:
                # Aquí se simula el guardado. Las imágenes en producción se subirían al Storage primero.
                nuevo_deportista = {
                    "documento": doc, "nombres": nombres, "apellidos": apellidos, "nivel": nivel,
                    "fecha_registro": datetime.now().strftime("%Y-%m-%d %H:%M"), "celular": celular, "correo": correo,
                    "foto_url": "Simulado://url_foto_storage.jpg" if foto_perfil else None
                }
                st.session_state.deportistas.append(nuevo_deportista)
                st.success(f"¡Deportista {nombres} {apellidos} registrado exitosamente en el nivel {nivel}!")

# ==========================================
# MÓDULO 2: CONTROL DE PAGOS
# ==========================================
with tabs[1]:
    st.header("Control Transaccional de Pagos")
    
    col_p1, col_p2 = st.columns([1, 2])
    
    with col_p1:
        st.subheader("Registrar Transacción")
        with st.form("form_pago", clear_on_submit=True):
            id_dep = st.text_input("Documento Identidad del Deportista*")
            concepto = st.selectbox("Concepto de Pago", ["Inscripción", "Mensualidad", "Tienda (Uniformes/Artículos)", "Evento/Competencia", "Otro"])
            monto = st.number_input("Monto ($)", min_value=0, value=0, step=5000)
            medio_pago = st.selectbox("Medio de Pago", ["Nequi", "Daviplata", "Transferencia Bancaria", "Código QR", "Bre-B", "Efectivo"])
            soporte_pago = st.file_uploader("Soporte de Pago (Imagen/PDF)", type=["pdf", "png", "jpg"])
            estado_pago = st.selectbox("Control de Estado", ["Pendiente", "En proceso", "Pagado"])
            
            submit_pago = st.form_submit_button("Registrar Pago")
            if submit_pago:
                nuevo_pago = {
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "deportista": id_dep, "concepto": concepto, "monto": monto,
                    "medio": medio_pago, "estado": estado_pago
                }
                st.session_state.pagos.append(nuevo_pago)
                st.success("Transacción registrada en el sistema.")
                
    with col_p2:
        st.subheader("Historial de Transacciones Recientes")
        if st.session_state.pagos:
            df_pagos = pd.DataFrame(st.session_state.pagos)
            st.dataframe(df_pagos, use_container_width=True)
            
            # Filtro rápido analítico
            st.markdown("**Resumen de Caja Rápido:**")
            total_pagado = df_pagos[df_pagos['estado'] == 'Pagado']['monto'].sum()
            st.metric(label="Total Recaudado (Estado: Pagado)", value=f"${total_pagado:,} COP")
        else:
            st.info("No se han registrado transacciones aún.")

# ==========================================
# MÓDULO 3: TIENDA
# ==========================================
with tabs[2]:
    st.header("Tienda e Inventario del Club")
    
    # Vista de Catálogo en formato Grid
    st.subheader("Catálogo de Productos")
    cols_tienda = st.columns(2)
    for idx, item in enumerate(st.session_state.tienda):
        with cols_tienda[idx % 2]:
            st.code(f"Ref: {item['ref']}")
            st.markdown(f"### {item['producto']}")
            st.markdown(f"**Valor:** ${item['valor']:,} COP")
            st.text(f"Tallas disponibles: {item['tallas']} | Colores: {item['color']}")
            # Botón simulador de venta rápida
            if st.button(f"Registrar venta de {item['producto']}", key=f"btn_{item['ref']}"):
                st.success(f"Venta pre-registrada para {item['producto']}. Recuerda asentar el pago en la pestaña de Control de Pagos.")

# ==========================================
# MÓDULO 4: EVENTOS & NOTICIAS
# ==========================================
with tabs[3]:
    st.header("Calendario, Competencias y Noticias")
    
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.subheader("Próximos Eventos del Calendario")
        eventos = pd.DataFrame([
            {"Fecha": "2026-06-15", "Evento": "Torneo Interno Interescuelas", "Lugar": "Pista Principal"},
            {"Fecha": "2026-07-04", "Evento": "Clasificatorio Nacional de Velocidad", "Lugar": "Patinódromo Departamental"}
        ])
        st.table(eventos)
        
    with col_e2:
        st.subheader("Galería de Fotos Recientes")
        st.info("Espacio para renderizar el carrusel de fotos del Storage de los últimos eventos.")

# ==========================================
# MÓDULO 5: HISTORIAL Y RENDIMIENTO
# ==========================================
with tabs[4]:
    st.header("Seguimiento de Rendimiento y Métricas del Deportista")
    
    # Buscador de deportista para ver su ficha
    if st.session_state.deportistas:
        lista_deportistas = [d['documento'] for d in st.session_state.deportistas]
        buscar_dep = st.selectbox("Seleccione el documento del deportista para ver seguimiento:", lista_deportistas)
        
        # Simulación de Ficha de Rendimiento
        st.subheader("Métricas de Evolución")
        col_m1, col_m2, col_m3 = st.columns(3)
        col_m1.metric(label="Asistencia este mes", value="92%", delta="⚡ Excelente")
        col_m2.metric(label="Tiempo 100m Meta contra Meta", value="11.4 seg", delta="-0.3 seg (Mejora)")
        col_m3.metric(label="Evaluación Técnica General", value="Avanzado B", delta="Promovido")
        
        st.text_area("Observaciones del Entrenador:", value="Muestra gran técnica en curvas. Se recomienda seguir fortaleciendo potencia en la salida.")
    else:
        st.info("Registra deportistas en la pestaña de 'Inscripciones' para habilitar el seguimiento de rendimiento.")

# ==========================================
# MÓDULO 6: EL CLUB
# ==========================================
with tabs[5]:
    st.header("Información Institucional del Club")
    
    with st.expander("📖 Historia, Misión y Visión", expanded=True):
        st.write("""
        **Misión:** Formar deportistas integrales en el patinaje de carreras y recreativo, promoviendo la disciplina y la salud física.
        \n**Historia:** Fundada con el fin de masificar el deporte sobre ruedas y proyectar talentos a nivel nacional...
        """)
        
    with st.expander("👥 Nuestro Equipo (Entrenadores y Dirección)"):
        st.markdown("""
        *   **Director General:** Lic. Carlos Mendoza
        *   **Entrenadora Nivel Iniciación:** Andrea Gómez
        *   **Entrenador Alta Competencia:** Prof. Luis Fernando Plaza
        """)
        
    with st.expander("⚖️ Reglamentos del Club"):
        st.write("Es de carácter obligatorio el uso de casco, protecciones completas y puntualidad en los entrenamientos...")
        
    with st.expander("📩 Contacto y PQRS"):
        st.write("¿Tienes dudas o peticiones? Escríbenos a: contacto@clubpatinaje.com")
        st.text_input("Deja tu PQRS de manera anónima o identificada aquí:")
        if st.button("Enviar PQRS"):
            st.success("PQRS enviada con éxito al comité administrativo.")
