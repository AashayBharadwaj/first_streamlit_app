
import streamlit

# Entering text on the page
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spniach & Rocket Smoothie')
streamlit.text('🐔Hard Boiled Free-Range Egg')
streamlit.text('🥑🍞Avacado Toast')

#  Importing pandas and reading a CSV file
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# streamlit.dataframe(my_fruit_list)

# Set an index to use it for displaying selections
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
 
