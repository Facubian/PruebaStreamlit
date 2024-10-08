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
  import joblib
  from scipy.stats import boxcox
  import pandas as pd

  def modelo(var,ovr):
    pred = ovr.predict(var)
    return pred

  ovr = joblib.load("modelo/modeloEntrenado.pkl")

  st.title('Arbol de desicion simple')
  st.markdown("""En esta página se puede probar un árbol de decisión 
    entrenado para predecir los óvulos que se recuperarán de una aspiración folicular 
    a partir de distintos datos clínicos del paciente""")

  st.subheader('Variables utilizadas')

  st.markdown("""Para el modelo utilizamos como variables predictoras la **hormona anti-mülleriana(AMH)**, 
  **el recuento de folículos antrales (RFA)**, 
  **la edad del paciente**, 
  **las unidades de lh suministradas**, 
  **las unidades suministradas totales (lh + fsh)**, 
  **los dias de estimulacion** y 
  **dos posibles diagnósticos**""")

  diagnosticos=["Ninguno","Edt","Femenino Anatomico","Femenino Endocrino","Insuficiencia Ovarica","Masculino","Otro"]

  #col1, col2 = st.columns(2)

  amh = st.number_input('Hormona antimülereana', min_value=0.0)
  rfa = st.number_input('Recuento de foliculos antrales',min_value=0)
  edad = st.number_input('Edad del paciente', min_value=18, help="Tiene que ser mayor 18")

  
  #fsh = col1.number_input('Unidades de fsh',min_value=0)
  
  #dia_1 = col1.selectbox('Primer diagnostico', diagnosticos)
  
  #edad = col2.number_input('Edad del paciente', min_value=18, help="Tiene que ser mayor 18")
  #dias = col2.number_input('Cantidad de dias de estimulacion',min_value=0)
  #lh = col2.number_input('Unidades de lh suministradas',min_value=0)

  #if(dia_1 != "Ninguno"):
   # dia_2 = col2.selectbox('Segundo diagnostico', diagnosticos)
  #else:
   # dia_2 = col2.selectbox('Segundo diagnostico', ["Ninguno"])
    #dia_2 = "Ninguno"
  

  
  if st.button("Calcular"):
    
    #lh_d = 0
    
    #if(lh<1):
     # lh_d = 0
    #else:
     # lh_d = 1
    
    #dias_d = 0
    #if(dias<12):
     # dias_d=0
    #else:
     # dias_d=1
    
    #dia1=diagnosticos.index(dia_1)+1
    #dia2=diagnosticos.index(dia_2)+1

    #unidades= fsh+lh
    
    variables={
      "edadboxcox": edad,
      "amh_boxcox": amh,
      "total rfa": rfa,
      "diagnostico 1": 0,
      "diagnostico 2": 0,
      "unidades": 0,
      "dias_dis": 0,
      "lh_dis": 0}
    
    variables = pd.DataFrame([variables])
    pred = modelo(variables,ovr)
    
    if(pred==1):
      st.markdown("Con un **67%** de probabilidad, se esperan obtener entre **0 y 4**")
    elif(pred==2):
      st.markdown("Con un **67%** de probabilidad, se esperan obtener entre **5 y 9**")
    else:
      st.markdown("Con un **67%** de probabilidad, se esperan obtener entre **mas de 10**")

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
