import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

st.set_page_config(page_title="Start-X", page_icon=":chart_increasing:",layout="wide")

# Sidebar
with st.sidebar:
    st.header("👨‍💻 About the Authors")
    st.write("""
    **Phantom Troupe** is a group of tech enthusiasts and budding data analysts. Driven by passion and a love for gaining knowledge, we've created this app to get a insight into the world of Indian startups.

    Connect, contribute, or just say hi!
    """)

    st.divider()
    st.subheader("🔗 Connect with Me", anchor=False)
    st.markdown(
        """
        - [🐙 Source Code](https://github.com)
        - [☕ Buy me a Coffee](https://ko-fi.com)
        - [🌐 Personal Website](https://streamlit.com)
        - [👔 LinkedIn](https://www.linkedin.com)
        """
    )

    st.divider()
    st.subheader("🏆 Datahack 2.0 Datathon 2023", anchor=False)
    st.write("This app helps you to gain the current and previous insights of the leading Indian startups in the field of Artificial Intelligence and Electric Vehicle")

    st.divider()
    st.write("Made with ♥ in Mumbai, India")

image = """
    <img src='https://img.freepik.com/free-vector/people-analyzing-growth-charts_23-2148866843.jpg?w=1060&t=st=1698495346~exp=1698495946~hmac=e8cb0351e6ef29d51a5d1e6c74ba1c5a4db36eaded04acf01a1dc5df2a8d7b92' width='420px' alt='business analytics' style='border-radius: 12px;'>
""" 


with st.container():
    empty_column2, logo_column, empty_column1 = st.columns((4, 4, 4))
    
    # with image_column:
    #     st.markdown(image,unsafe_allow_html=True)

    with empty_column1:
        st.empty()
        
    with empty_column2:
        st.empty()

    with logo_column:
        logo = Image.open('my-image.png')
        st.image(logo)
        
        
with st.container():
    st.markdown("""
        ##
        ## Welcome to ***Start-X***, your one stop solution for all things data related. Here you can find resources and tools that will help you      
    """)

q1df = pd.read_csv('top10companies.csv')

company = np.array(q1df['Company Name'])
revenue = np.array(q1df['Percent Revenue'])

df = pd.DataFrame({'Companies': company, 'Revenue  Growth in % ': revenue})

with st.container():
    st.markdown(" ## Top 10 startups in the last 5 years are: ")
    emp_col1, tab_col, emp_col2 = st.columns((3,6,3))
    with emp_col1:
        st.empty()
    with tab_col:
        st.table(df)
    with emp_col2:
        st.empty()
    
q2df = pd.read_csv('locDist.csv')

arr = np.array(q2df['count'])

with st.container():
    st.markdown(" ## Location wise distribution of top 100 startups for the last 10 years is: ")
    # fig = px.imshow(arr.reshape(7,3))
    fig = go.Figure(data=[go.Scatter(
        x=q2df['Region'],
        y=q2df['count'],
        mode='markers',
        marker=dict(
        color=q2df['count'],
        size=q2df['count'],
        showscale=True
        )
    )])
    st.plotly_chart(fig, theme=None, use_container_width=True, text=True, aspect="auto")

q3df = pd.read_csv('Dataset_cleaned.csv')
arr1 = q3df['Domestic Funds in mil USD'].to_list()
arr2 = q3df['Foreign Funds'].to_list()

with st.container():
    st.markdown("## Comparison between foreign and domestic fundings is: ")
    
    fig = px.line(q3df, x='Unnamed: 0', y=['Domestic Funds in mil USD', 'Foreign Funds'])
    st.plotly_chart(fig, theme=None, use_container_width=True)

q4df = pd.read_csv('finAnalysis.csv')

revEighteen = q4df['Revenue 2018']
revNineteen = q4df['Revenue 2019']
revTwenty = q4df['Revenue 2020']
revTwentyOne = q4df['Revenue 2021']
revTwentyTwo = q4df['Revenue 2022']

domFund = q4df['Domestic Funds in mil USD']

name = q4df['Company Name']

with st.container():
    st.markdown("## Valuation based analysis on Fintech companies over the last 5 years is: ")
    st.markdown("##")
    for i in range(10):
        write = f'{name[i]} earned a revenue of {(revEighteen[i] + revNineteen[i] +revTwenty[i] +revTwentyOne[i] + revTwentyTwo[i]).round()} Cr over a period of 5 years. It\'s domestic funding is {domFund[i].round()} M.'
        st.markdown(f'> ### {write}')
       
q5df = pd.read_csv('temp.csv')

revEighteen = q5df['Revenue 2018']
revNineteen = q5df['Revenue 2019']
revTwenty = q5df['Revenue 2020']
revTwentyOne = q5df['Revenue 2021']
revTwentyTwo = q5df['Revenue 2022']

preCovidRev = [ (revEighteen[i] + revNineteen[i])/2 for i in range(len(revEighteen)) ]
covidRev = [ (revTwenty[i] + revTwentyOne[i])/3 for i in range(len(revTwenty)) ]
postCovidRev = revTwentyTwo
sector = q5df['Sector']

newDf = pd.DataFrame({'Sector':sector, 'PreCovidRev': preCovidRev, 'CovidRev': covidRev, 'PostCovidRev': postCovidRev})

with st.container():
    st.markdown("## How did Covid affect funding for startups across different sectors? ")
    st.markdown("##")
    fig = px.line(newDf, x='Sector', y = ['PreCovidRev', 'CovidRev', 'PostCovidRev'], markers = True)
    
    st.plotly_chart(fig, use_container_width=True)

estDf = pd.read_csv('emergingStartups2.csv')

with st.container():
    st.markdown("## Which sectors have had the most number of new and emerging startups: ")
    st.markdown("##")
    
    fig = px.bar(estDf, x='Sector', y='Average Revenue (%)', color='Sector')

    st.plotly_chart(fig, use_container_width=True)

q7df = pd.read_csv('q7.csv')

with st.container():
    st.markdown("## Comparison of the growth rate of startups with their age: ")
    st.markdown("##")
    
    import seaborn as sns
    fig = plt.figure(figsize=(10, 4))
    sns.lineplot(data=q7df,x='Age',y='Percentage Revenue')
    st.pyplot(fig, use_container_width=True)

tdf = pd.read_csv('q10.csv')
    
with st.container():
    st.markdown("##  Startups in which sectors have been stagnating or decreasing: ")
    st.markdown("##")
    
    fig = px.line(tdf, x='Sector', y ='Percent Revenue', markers = True)
    
    st.plotly_chart(fig, use_container_width=True)

    