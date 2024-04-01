import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
st.title("Palmer's Penguins")
st.markdown('Use this Streamlit app to make your own scatterplot aboutpenguins!')
selected_species = st.selectbox('What species would you like tovisualize?',
                                ['Adelie', 'Gentoo', 'Chinstrap'])
selected_x_var = st.selectbox('What do you want the x variable to be?',
                              ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
selected_y_var = st.selectbox('What about the y?',
                              ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
selected_gender = st.selectbox('What gender do you want to filter for?',
                               ['all penguins', 'male penguins', 'femalepenguins'])

penguin_file = st.file_uploader("Select Your Local Penguins CSV (defaultprovided)")
#if penguin_file is not None:
#    penguins_df = pd.read_csv(penguin_file)
#else:
#    penguins_df = pd.read_csv("data/penguins.csv")
#penguins_df = penguins_df[penguins_df['species'] == selected_species]

penguin_file = st.file_uploader('Select Your Local Penguins CSV')
if penguin_file is not None:
    penguins_df = pd.read_csv(penguin_file)
else:
    st.stop()

if selected_gender == 'male penguins':
    penguins_df = penguins_df[penguins_df['sex'] == 'male']
elif selected_gender == 'female penguins':
    penguins_df = penguins_df[penguins_df['sex'] == 'female']
else:
    pass

sns.set_style('darkgrid')
markers = {"Adelie": "X", "Gentoo": "s", "Chinstrap":'o'}

alt_chart = (
alt.Chart(penguins_df, title=f"Scatterplot of {selected_species}Penguins").mark_circle().encode(
    x=selected_x_var,
    y=selected_y_var,
    color="species").interactive()
)
st.altair_chart(alt_chart, use_container_width=True)