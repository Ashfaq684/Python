import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Tea Taste Poll",
    page_icon="☕",
    layout="wide"
)

# Main title
st.title("☕ Tea Taste Poll")

# Create two columns for the poll
col1, col2 = st.columns(2)

# First column - Masala Tea
with col1:
    st.header("Masala Tea")
    st.image(
        "https://img.freepik.com/free-photo/steaming-cup-masala-chai-with-spices-coffee-beans-dark-surface_9975-124574.jpg?t=st=1745232690~exp=1745236290~hmac=1f3b83d676e8e4103824a026bfd252e0d99fffae240b2492ecd1300ac5a179b9&w=1380",
        width=200
    )
    vote1 = st.button("Vote Masala Tea")

# Second column - Ginger Tea
with col2:
    st.header("Ginger Tea")
    st.image(
        "https://img.freepik.com/free-photo/hot-ginger-juice-ginger-sliced-wooden-table_1150-18396.jpg?t=st=1745232724~exp=1745236324~hmac=e211f99fe4232006192b9559ae7b30c3b9747bb1a0347ce4bfaba7f6ec467fc7&w=1060",
        width=200
    )
    vote2 = st.button("Vote Ginger Tea")

# Handle votes
if vote1:
    st.success("Thanks for voting Masala Tea")
elif vote2:
    st.success("Thanks for voting Ginger Tea")

# Sidebar
with st.sidebar:
    st.header("🍵 Personalize Your Tea")
    name = st.text_input("Enter your name")
    tea = st.selectbox(
        "Choose your tea",
        ["Masala", "Kesar", "Ginger"]
    )

# Welcome message
if name:
    st.write(f"👋 Welcome {name}! Your {tea} tea is getting ready...")

# Tea instructions
with st.expander("📝 Show Tea Making Instructions"):
    st.write("""
    1. Boil water with tea leaves
    2. Add milk and spices
    3. Serve hot
    """)

# Additional information
st.markdown("""
# Welcome to Tea App
> "There is no trouble so great or grave that cannot be much diminished by a nice cup of tea."
> - Bernard-Paul Heroux
""")