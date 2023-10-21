import streamlit as st
import plotly.express as px
import pandas as pd
from backend import get_data
st.set_page_config(layout='wide')

st.title('Weather forcast for the next days')
place= st.text_input('place:')
st.text('Forcast Days')
days = st.slider('Select a value', min_value=0, max_value=5, value=0, step=1,help='select the number of forcasted days')



option = st.selectbox(label='Select data to view',options=['Temperature','Sky'])

st.header(f'{option}for the next {days} days in {place}')


if place:
    filtered_context = get_data(place, days)
    if option == 'Temperature':
        temperatures = [dict['main']['temp'] for dict in filtered_context]
        dates = [dict['dt_txt'] for dict in filtered_context]
        figure = px.line(x=dates, y=temperatures,labels ={'x':'Date','y':'Temperature (C)'})
        st.plotly_chart(figure)
    if option == 'Sky':
        images ={
            'Clear':'images/clear.png',
            'Clouds':'images/cloud.png',
            'Rain': 'images/rain.png',
            'Snow': 'images/snow.png'
        }
        sky_conditons = [dic['weather'][0]['main'] for dic in filtered_context]
        print(sky_conditons)
        image_paths =[images[condition] for condition in sky_conditons]
        st.image(image_paths,width=115)
