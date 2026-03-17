import streamlit as st

# 1. Page Configuration (Is se app full screen aur professional lagegi)
st.set_page_config(page_title="Falcon Digital Hub", layout="wide")

# 2. Sidebar (Navigation menu)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Kahan jana chahte hain?", ["Dashboard Home", "Cricket Records", "E-commerce Store Idea"])

# 3. Main Pages Logic
if page == "Dashboard Home":
    st.title("🚀 Welcome to Your Professional Dashboard")
    st.write("---")
    
    # Professional Metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("Daily Visitors", "1,250", "+12%")
    c2.metric("Total Sales", "PKR 45,600", "+5%")
    c3.metric("Project Status", "85%", "Running")
    
    st.write("---")
    if st.button("Celebrate Success! 🎈"):
        st.balloons()

elif page == "Cricket Records":
    st.header("🏏 Cricket Historical Stats")
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Babar Azam")
        st.info("Record: 3 Centuries in 3 consecutive matches!")
    with col_b:
        st.subheader("World Records")
        st.write("Current Ranking: No. 1 in ODIs")

elif page == "E-commerce Store Idea":
    st.header("🛍️ Sports Store Project")
    st.success("Platform: Shopify")
    st.warning("Color Scheme: Red & Green")
    st.write("Status: Design phase mein hai.")