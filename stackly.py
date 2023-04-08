
import streamlit as st
import pandas as pd


st.set_page_config(page_title="Stackly", page_icon=":books:", layout="wide", initial_sidebar_state="expanded", theme="dark")

[theme]
primaryColor="#F63366"
backgroundColor="#FFFFFF"
textColor="#262730"
font="monospace"

# Page setup
st.set_page_config(page_title="Stackly", page_icon="🐍", layout="wide")
st.title("Stackly - Learn Smart, Stack Fast")

# Connect to the Google Sheet
sheet_id = "15ago01u5VzLpDuVJGcYG0cfflxKw9bVWoYphvrnFiUs"

# Construct the URL to download the CSV file
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv"

df = pd.read_csv(url, dtype=str).fillna("None")

# Show the dataframe (we'll delete this later)
# st.write(df)

# Use a text_input to get the keywords to filter the dataframe
text_search = st.text_input("Search videos by topics, course name, level or domain", value="")

# Filter the dataframe using masks
m1 = df["Course Name"].str.contains(text_search)
m2 = df["Topics Covered"].str.contains(text_search)
m3 = df["Level"].str.contains(text_search)
m4 = df["Domain"].str.contains(text_search)
df_search = df[m1 | m2 | m3 | m4]

# if text_search:
#     st.write(df_search)

# Another way to show the filtered results
# Show the cards
N_cards_per_row = 3
if text_search:
    for n_row, row in df_search.reset_index().iterrows():
        i = n_row%N_cards_per_row
        if i==0:
            st.write("---")
            cols = st.columns(N_cards_per_row, gap="large")
        # draw the card

        with cols[n_row%N_cards_per_row]:
            st.caption(f"{row['Course Name'].strip()}")
            st.caption(f"{row['University'].strip()}")
            st.caption(f"{row['Prerequisites'].strip()} ")
            st.markdown(f"**{row['Level'].strip()}**")
            st.markdown(f"*{row['Domain'].strip()}*")
            st.markdown(f"**{row['Links']}**")








