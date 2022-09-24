import streamlit

streamlit.title('My Mom\'s New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('\N{stuffed flatbread}Omega 3 & Blueberry Oatmeal')
streamlit.text('\N{green salad}Kale, Spinach & Rocket Smoothie')
streamlit.text('\N{chicken}Hard-Boiled Free-Range Egg')
streamlit.text('\N{avocado}{toast}Avocado Toast')

streamlit.header('\N{banana}{mango}Build Your Own Fruit Smoothie{kiwi fruit}{grapes}')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:", list (my_fruit_list.index))

#display the table on the page
streamlit.dataframe(my_fruit_list)
