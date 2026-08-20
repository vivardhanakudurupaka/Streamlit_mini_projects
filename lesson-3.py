import streamlit as st

st.title("COLLEGE ADMISSION")
st.header("BVRIT HYDERABAD College of Engineering for Women")

with st.sidebar:
    name = st.text_input("Name")
    rollnumber = st.text_input("Roll-Number")
    branch = st.radio("Branch" , ["CSE","IT","ECE","EEE","MECH"])
    section = st.selectbox("Section",["A","B","C","D"])
c1,c2,c3 = st.columns([1,2,1])
with c2 :
    st.image("bvrith_image.jpeg",width=500)

with st.expander(" click to know more about the college "):
    st.markdown("""
Autonomous status ensures an updated, industry-ready curriculum focused on modern technologies.
Highest salary package reaches up to ₹59 LPA with top companies like Microsoft and Amazon.
Exclusive women-centric tech mentorship, hackathons, and global coding clubs empower female engineers.
Convenient Bachupally campus location provides extensive college bus connectivity across Hyderabad.
Vibrant college life features active student clubs and the famous annual fest, Medhanvesh.
""")

if st.button("submit"):
    st.write(f"{name} you got admission in {branch} branch .")
    st.success(f"CONGRATULATIONS {name} . Good Luck for your future .")