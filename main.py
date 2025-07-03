import streamlit as st

# Read HTML file content
with open("app.html", "r") as f:
    html_content = f.read()

# Display in Streamlit
st.markdown(html_content, unsafe_allow_html=True)
