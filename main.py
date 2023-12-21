from converter import objidToTime
from converter import timeToId

import streamlit as st
st.set_page_config(page_title="MongoTimeX", page_icon="🕒")




st.markdown(
    f'<div style="text-align: center;"><h1>MongoTimeX</h1></div>', unsafe_allow_html=True
)



hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


with st.sidebar:
    id_to_time = st.checkbox("Convert Object ID to Time")
    time_to_id = st.checkbox("Convert Time to Object ID")




if id_to_time:
    with st.form(key="idToTime",border=True):
        obj_id = st.text_input("Object ID")
        submit_button = st.form_submit_button("Convert")
    if submit_button:
        try:

            utc_time,ist_time = objidToTime(obj_id=obj_id)
            st.write("Time in UTC")
            st.code(utc_time)
            st.write("Time in IST")
            st.code(ist_time)
        except ValueError as e:
            st.error(e)




if time_to_id:
    with st.form(key="timeToId",border=True):
        year = st.number_input(label="Year (Min Value should be 1970)",placeholder="XXXX",value=None,step=1,min_value=1970)
        month = st.number_input(label="Month",placeholder="1-12",value=None,step=1,min_value=1,max_value=12)
        date = st.number_input(label="Date",placeholder="1-31",value=None,step=1,min_value=1,max_value=31)
        hour = st.number_input(label="Hour",placeholder="0-23",value=None,step=1,min_value=0,max_value=59)
        minute = st.number_input(label="Minute",placeholder="0-59",value=None,step=1,min_value=0,max_value=59)
        second = st.number_input(label="Second",placeholder="0-59",value=None,step=1,min_value=0,max_value=59)
        submit_button = st.form_submit_button("Convert")

    if submit_button:
        
        try:
            objectId = timeToId(year=year,month=month,date=date,hour=hour,minute=minute,second=second)
            st.write("Object ID")
            st.code(objectId)


        except ValueError as e:
            st.error(e)

    

