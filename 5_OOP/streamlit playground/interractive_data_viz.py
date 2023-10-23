import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.title('Experimenting with multiselect')
file = st.file_uploader('Choose a CSV file', type='csv')

if file is not None:
        df = pd.read_csv(file)

        #header
        st.header('Dataframe Head')
        st.write(df.head())

        #select columns
        columns = st.multiselect('Select dataframe columns', df.columns)

        if columns:
                st.write(df[columns])

        #plot : 
        st.subheader('Plotting with selected data')
        x = st.selectbox('Abcisse', df.columns)
        y = st.selectbox('Ordonnée', df.columns)

        if x and y:
            fig = plt.figure(figsize=(5,5))
            sns.scatterplot(data=df, x=x, y=y)
            st.pyplot(fig)