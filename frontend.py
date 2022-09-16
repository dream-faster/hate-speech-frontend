import streamlit as st
from utils import get_prediction, get_hierarchy
st.set_page_config(page_title="Hate Speech detection", page_icon="😾")

st.title('Hate Speech detection with Modular Pipelines')

with st.form("my_form"):
    text = st.text_input('Text to analyze (use ; to add multiple)', 'Life of Brian')
    submitted = st.form_submit_button("Predict")
    
    pipeline = st.radio(
        "Which pipeline should we use?",
        ('random', 'all_0s', 'all_1s', 'sklearn_simple_nb'))
    
    
    if submitted:
        with st.spinner('Wait for it...'):
            data = get_prediction(text, pipeline)
            pipeline_hierarchy = get_hierarchy(pipeline)
            
        if data:
            st.subheader("Prediction(s)")
            st.text(f'Prediction with pipeline: {pipeline} are \n\t {data}')
            
            st.subheader(f"Hierarchy of pipeline: {pipeline}")
            st.text(pipeline_hierarchy.replace("┃       ",""))
        else:
            st.error("Error")

