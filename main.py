import streamlit as st

st.set_page_config(layout='wide')

st.title('Weather forcast for the next days')
place=st.text_input(label='place:',key='place')
st.text('Forcast Days')
days = st.slider('Select a value', min_value=0, max_value=5, value=0, step=1,help='select the number of forcasted days')



Dropdown = st.selectbox(label='Select data to view',options=['Temperature','sky'])

st.header(f'{Dropdown}for the next {days} in {place}')
