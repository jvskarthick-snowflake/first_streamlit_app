import streamlit

streamlit.title('🥣 My Parents new Healthy Breakfast/Lunch/Dinner')

streamlit.header('🥗 Breakfast Menu 🥗')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach  &  Rocket Smoothie')
streamlit.text('🥑🍞Hard-Biled  Free-Range Egg')

streamlit.header('🥗 Lunch Menu 🥗')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach  &  Rocket Smoothie')
streamlit.text('🥑🍞Hard-Biled  Free-Range Egg')

streamlit.header('🥗 Dinner Menu 🥗')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach  &  Rocket Smoothie')
streamlit.text('🥑🍞Hard-Biled  Free-Range Egg')

Import Pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
