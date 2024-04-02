import streamlit as st
import langchainFun
st.title("Random City And Dish Gen")
selected_letter=st.sidebar.selectbox("Pick A Letter",("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"))


    
if(selected_letter):
    response= langchainFun.city_selector_famous_dish(selected_letter)
    st.header(response['city']) 
    dish_items=response['dishes'].split('/n/n')
    st.write("**Menu List**")
    for item in dish_items:
        st.write(item)   