import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.figure_factory as ff

st.title('Adding data in realtime?')

#empty space that will be updated
placeholder = st.empty()

#an ini
df = pd.DataFrame(np.random.randn(5,3), columns=['x', 'y', 'z'])

while True:
    #new data
    x = np.random.randn(1) -2
    y = np.random.randn(1)
    z = np.random.randn(1) + 2 
    dic = { 'x' : x,
            'y' : y,
            'z' : z}
   
    data = pd.DataFrame(data=dic)
    #appending dataframe
    df = pd.concat([df,data], axis = 0, ignore_index=True)
    #updating plot
    with placeholder.container():
        st.subheader('A scatter plot')
        scatter = st.scatter_chart(data=df, x='x', y='y', size='z')
        st.subheader('a Nice hist plot')
        hist = ff.create_distplot([df[c] for c in df.columns], group_labels=df.columns ,bin_size=0.1)
        st.plotly_chart(hist)
        #zzz
        time.sleep(3)

        