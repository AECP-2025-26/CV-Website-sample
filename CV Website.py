import streamlit as st

# ---------- Page Config ----------
st.set_page_config(
    page_title="Asimanshu Samal | CV",
    page_icon="⛏️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Custom Header Styling ----------
st.markdown("""
<style>
.main-header {
    font-size: 64px;
    font-weight: 900;
    color: #1B4F72;
    text-align: center;
    padding: 15px 0;
    border-bottom: 4px solid #2E86C1;
    margin-bottom: 10px;
}
.sub-header {
    font-size: 20px;
    text-align: center;
    color: #566573;
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">Asimanshu Samal</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Mining Engineering Student | IIT (ISM) Dhanbad</p>', unsafe_allow_html=True)

# ---------- Sidebar Navigation ----------
st.sidebar.title("Navigate")
page = st.sidebar.radio(
    "Go to",
    ["Home", "About", "Education", "Hobbies", "Projects", "Contact"],
)

# ---------- Home ----------
if page == "Home":
    st.subheader("Welcome 👋")
    st.write(
        """
        I am on an eternal search for knowledge and information —
        reach out for anything, no professional jargon required.
        """
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Institute", value="IIT (ISM) Dhanbad")
    with col2:
        st.metric(label="Branch", value="Mining Engineering")
    with col3:
        st.metric(label="Hometown", value="Rourkela, Odisha")

# ---------- About ----------
elif page == "About":
    st.subheader("About Me")
    st.write(
        """
        I'm Asimanshu Samal, from Rourkela, Odisha, currently studying
        Mining Engineering at IIT (ISM) Dhanbad. I'm on an eternal
        search for knowledge and information — feel free to reach out
        for anything, no professional jargon needed.
        """
    )

# ---------- Education ----------
elif page == "Education":
    st.subheader("Education")

    with st.container(border=True):
        st.markdown("**Indian Institute of Technology (Indian School of Mines), Dhanbad**")
        st.write("B.Tech in Mining Engineering")

    with st.container(border=True):
        st.markdown("**12th Grade**")
        st.write("DPS E City")
        st.write("95.8%")

    with st.container(border=True):
        st.markdown("**10th Grade**")
        st.write("DPS E City")
        st.write("97.2% (best of 5)")

# ---------- Hobbies ----------
elif page == "Hobbies":
    st.subheader("Hobbies & Interests")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Video Editing**")
        st.write("Editing videos using Adobe After Effects and Premiere Pro.")
    with col2:
        st.markdown("**Software**")
        st.write("- Adobe After Effects")
        st.write("- Adobe Premiere Pro")

# ---------- Projects ----------
elif page == "Projects":
    st.subheader("Projects")
    st.write("Projects, internships, or fieldwork will go here.")

    with st.expander("Project / Internship Name", expanded=True):
        st.write("Short description of the project or internship.")
        st.write("[Link to report / repo / demo](#)")

# ---------- Contact ----------
elif page == "Contact":
    st.subheader("Contact")
    st.write("I am on an eternal search for knowledge and information — contact me here for anything, no professional jargon needed.")
    st.write("- Email: asimanshusamal@gmail.com")

# ---------- Footer ----------
st.sidebar.markdown("---")
st.sidebar.caption("© 2026 Asimanshu Samal")
