import streamlit as st
import pandas as pd

df = pd.read_csv("/Users/yenlinh/Desktop/car_data.csv")
st.title("Car Data")  # add a title

#text box (st.text_input) to input the car_name (optional)
car_name = st.sidebar.text_input("Input car name:")
#multiselect (st.multiselect) to choose between Manual and/or Automatic (default option is both)
multiselect = st.sidebar.multiselect("Choose",["Manual","Automatic"],default = ["Manual", "Automatic"])
#slider (st.slider) to choose a range of selling_price (default: 0 to 20)
price_slider = st.sidebar.slider("Range of selling price",0,20,(0,20))
#slider (st.slider) to choose a range of year (default: 2000 to 2024)
year_slider=st.sidebar.slider("Range of year",2000,2024,(2000,2024))
#submit button (st.button), which should show the **filtered** data in a table format on the main screen. If no filters are selected, show the original data as it is.
button = st.sidebar.button("Filter")

#Main screen should show the filtered data in table format or any human readable format.
filtered_df = df.copy()
if car_name:
    filtered_df = filtered_df[filtered_df['Car_Name'].str.contains(car_name,case = False)]
if multiselect:
    filtered_df = filtered_df[filtered_df['Transmission'].isin(multiselect)]
if year_slider:
    filtered_df = filtered_df[(filtered_df['Year'] >= year_slider[0]) & (filtered_df['Year'] <= year_slider[1])]
if price_slider:
    filtered_df = filtered_df[(filtered_df['Selling_Price'] >= price_slider[0]) & (filtered_df['Selling_Price'] <= price_slider[1])]
if button:
    st.write(filtered_df)