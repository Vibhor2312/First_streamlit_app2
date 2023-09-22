

import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('my parets new healthy diner')

streamlit.header('Breakfast menu')
streamlit.text('🥣 Omega 3 & blueberry oatmeal')
streamlit.text(' 🥗 kale, spinach & Rocket smoothie')
streamlit.text(' 🐔 hard- Boiled Free-Range Egg')
streamlit.text('🥑🍞Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie ')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')


fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header('fruityvice fruit advice')

fruit_choice = streamlit.text_input('What fruit would you like information about?','kiwi')
streamlit.write('The user entered ', fruit_choice)


#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)


# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)



streamlit.stop()

#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("fruit load contains:")
streamlit.dataframe(my_data_rows)

Add_my_fruit=  streamlit.text_input('What fruit would you like to add','jackfruit')
streamlit.write('Thanks for adding jackfruit ', fruit_choice)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")

if streamlit.button('get fruits list'):
   my_cnx =snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows= get_fruit_load_list()
   my_cnx.close()
   streamlit.dataframe(mt_data_rows)

  












