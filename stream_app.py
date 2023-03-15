import streamlit
import pandas

streamlit.title('My parents new healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Oatmeal with fruites')
streamlit.text('Green Smoothie')
streamlit.text('Hard boiled eggs')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.dataframe(my_fruit_list)
