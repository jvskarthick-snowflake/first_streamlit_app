import streamlit

streamlit.title('π₯£ My Parents new Healthy Breakfast/Lunch/Dinner')

streamlit.header('π₯ Breakfast Menu π₯')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach  &  Rocket Smoothie')
streamlit.text('π₯πHard-Biled  Free-Range Egg')

streamlit.header('π₯ Lunch Menu π₯')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach  &  Rocket Smoothie')
streamlit.text('π₯πHard-Biled  Free-Range Egg')

streamlit.header('π₯ Dinner Menu π₯')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach  &  Rocket Smoothie')
streamlit.text('π₯πHard-Biled  Free-Range Egg')
streamlit.text('π₯πRice')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Display the table on the page.
#streamlit.dataframe(my_fruit_list)
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


streamlit.header('fruityvice fruit Advice')

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
streamlit.text(fruityvice_response.json())



fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
