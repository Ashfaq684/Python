import streamlit as st

st.title("Tea maker App")

if st.button("Make tea"):
    st.success("Your tea is being brewed")

add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("Masala added to your tea")

tea_type = st.radio("Pick your tea base: ", ["Milk", "Water", "Almond Milk"])
st.write(f"selected base {tea_type}")

flavour = st.selectbox("Choose flavour: ", ["Ginger", "Kesar", "Tulsi"])
st.write(f"Selected Flavour {flavour}")

suger = st.slider("Suger level (spoon)", 0, 5, 2)
st.write(f"Selected suger level {suger}")

cups = st.number_input("How many cups?", min_value=1, max_value=10, step=1)
st.write(f"Selected {cups} cups tea.")

name = st.text_input("Enter your name")
if name:
    st.write(f"Welcome, {name} ! Your tea is on the way")
    
dob = st.date_input("Select your date of birth")
st.write(f"Your date of birth {dob}")