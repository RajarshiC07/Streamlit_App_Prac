import streamlit as st


st.markdown(":violet[ Moon Viewer]")

quality_list  = ["144p", "240p", "480p", "720p", "1080p"]
quality = st.selectbox("View the Moon",quality_list)
submit = st.button("Submit")
if submit:   
    image_path = rf"moon{quality}.jpg"
    st.image(image_path)