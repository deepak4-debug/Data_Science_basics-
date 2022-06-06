from cProfile import label
from turtle import color
from click import option
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#set the style for seaborn
sns.set_style('darkgrid')

st.title('App for Data Visualization')
st.balloons()

st.write('We are going to Explore and Visualize the following DataFrame. Check on *Show DataFrame* button on sidebar to see data.')
df = pd.read_csv('C:/Users/deefo/Downloads/omdena/adult.csv')
numeric_columns = df.select_dtypes(['float64', 'float32', 'int32', 'int64']).columns
categorical_columns = df.select_dtypes(include=['object']).columns.tolist()

#checkbox widget
checkbox = st.sidebar.checkbox('Show DataFrame')
if checkbox:
    st.write(df.head())
    
        
#Create scatterplots
st.write('* Use X-axis and Y-axis on sidebar to visualize the relation between different Numerical Data' )
st.sidebar.subheader('Scatter Plot setup')
select_box1 = st.sidebar.selectbox(label='X-axis', options=numeric_columns)
select_box2 = st.sidebar.selectbox(label='Y-axis', options=numeric_columns)
   
sns.relplot(x=select_box1, y=select_box2, data=df)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

#Create Histogram
st.write('* Select numeric column on sidebar to see distribution of different features' )
st.sidebar.subheader('Histogram')
select_box3 = st.sidebar.selectbox(label='Feature', options=numeric_columns)
sns.distplot(df[select_box3])
st.pyplot()

#creat countplot
st.write('* Select categorical column on sidebar to visualize coutplot of different features' )
st.sidebar.subheader('Countplots')
select_box4 = st.sidebar.selectbox(label='Categorical_feature', options=categorical_columns)
sns.countplot(x=select_box4, data=df)
st.pyplot()


#create boxplot 
st.write('* Use X-axis and Y-axis on sidebar to plot box plot and visualize the relation between different Numerical Data' )
sns.boxplot(x='income', y='age', data=df)
st.pyplot()

 
 
 
 
    
#uploaded_file = st.file_uploader("Choose a file to upload")
#if uploaded_file is not None:
 #   df = pd.read_csv(uploaded_file)
  #  st.write(df)



st.write('The following Histogram shows people with different age group.')  
fig, ax = plt.subplots()
df.hist(
    bins=8,
    column='age',
    grid=False,
    figsize=(8,8),
    color='#86bf91',
    zorder= 2,
    rwidth=0.9,
    ax=ax,
)

st.write(fig)

