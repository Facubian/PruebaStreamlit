import streamlit as st

@st.cache_resource

def intro():
    import streamlit as st

    st.write("# Modelos de aprenidzaje para prediccion en embriologia 👋")
    st.sidebar.success("Seleccionar una demo")

    st.markdown(
        """
        En esta pagina se muestran todos los modelos desarrollados para predecir los ovulos que se obtendran luego de un tratamiento de fecundacion in vitro(FIV)

        **👈 Selecciona una de nuestras demos en la izquierda** para ver en que estuvimos trabajando!

        ### ¿Queres saber mas de nosotros?

        - Visita la pagina oficial de [Embryoxite](https://embryoxite.life/)
        - Revisa nuestro [Linkedin](https://www.linkedin.com/company/embryoxite)

        ### Mira otros de nuestros trabajos
    """
    )

def primer_arbol():
  import streamlit as st
  import numpy as np

  st.title('Arbol de desicion simple')
  st.write("""En esta pagina se puede probar un arbol de desicion 
    entrenado para peredecir los ovolus que se recuperaran de una aspiracion folicular 
    a partir de distintos datos clinicos del paciente""")

  st.write("""Para el modelos utilizamos como variables predictoras la hormona anti-mülleriana(AMH),
  el recuento de foliculos antrales(RFA), la edad del paciente y las unidades suministradas totales(lh + fsh) y dos posibles diagnosticos""")

  diagnosticos=["Ninguno","Edt","Femenino Anatomico","Femenino Endocrino","Insuficiencia Ovarica","Masculino","Otro"]

  col1, col2 = st.columns(2)

  amh = col1.number_input('Hormona antimülereana', min_value=0)
  rfa = col1.number_input('Total de recuento de foliculos antrales',min_value=0)
  dia_1 = col1.selectbox('Primer diagnostico', diagnosticos)
  
  edad = col2.number_input('Edad del paciente', min_value=18, help="Tiene que ser mayor 18")
  unidades = col2.number_input('Unidades',min_value=0)

  if(dia_1 != "Ninguno"):
    dia_2 = col2.selectbox('Segundo diagnostico', diagnosticos)
  else:
    dia_2 = col2.selectbox('Segundo diagnostico', ["Ninguno"])
    dia_2 = "Ninguno"
  
  x=5
  ovs="0 a 2"
  if st.button("Calcular"):
    st.write(f"Con un {x}% de probabilidad, la cantidad de ovulos que se esperan capturar son entre {ovs}")

  st.button("Reset", type="primary")

page_names_to_funcs = {
    "Inicio": intro,
    "Arbol de desicion": primer_arbol,
}

st.set_page_config(
    page_title="Embryoxite",
    page_icon="🧬",
)
demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()