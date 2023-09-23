

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
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
                     
streamlit.header('fruityvice fruit advice')
try:                        
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
         streamlit.error("plz select a fruit to get information.")
    else:
        back_from_funtion = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_funtion)
                  
            
except URLError as e:
    streamlit.error()                 



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

streamlit.header("fruit load contains:")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * from fruit_load_list")
        return my_cur.fetchall()

if streamlit.button('get fruits list'):
   my_cnx =snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows= get_fruit_load_list()
   streamlit.dataframe(mt_data_rows)

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as mt_cur:
         my_cur.execute("insert into fruit_load_list values('" + fruit_load_list +"')")
         return " thanks for adding " + new_fruit













