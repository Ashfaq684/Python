import streamlit as st

st.title("Hello App")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first interactive app")
st.write("Choose your favourite variety of tea")

tea = st.selectbox("Your fav tea: ", ["Masala tea", "Lemon Tea", "Ginger Tea", "Milk tea"])

st.write(f"You choose {tea}. Excellent choise")

st.success("Your tea has been brewed")