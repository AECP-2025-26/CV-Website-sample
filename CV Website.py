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
    ["Home", "About", "Education", "Skills", "Projects", "Contact"],
)

# ---------- Home ----------
if page == "Home":
    st.subheader("Welcome 👋")
    st.write(
        """
        This is my personal CV site, built with Streamlit and deployed on
        Streamlit Community Cloud. I'm a Mining Engineering student at
        IIT (ISM) Dhanbad. Browse through the sections in the sidebar to
        learn more about my background, skills, and projects.
        """
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Institute", value="IIT (ISM) Dhanbad")
    with col2:
        st.metric(label="Branch", value="Mining Engineering")
    with col3:
        st.metric(label="Status", value="Student")

# ---------- About ----------
elif page == "About":
    st.subheader("About Me")
    st.write(
        """
        Add a short bio here — where you're from, what drew you to mining
        engineering, and what you're currently focused on (coursework,
        interests, or long-term goals).
        """
    )

# ---------- Education ----------
elif page == "Education":
    st.subheader("Education")
    with st.container(border=True):
        st.markdown("**Indian Institute of Technology (Indian School of Mines), Dhanbad**")
        st.write("B.Tech in Mining Engineering")
        st.write("Add your batch/year and CGPA here.")

    with st.container(border=True):
        st.markdown("**Schooling**")
        st.write("Add your 10th / 12th details here (school name, board, year, percentage).")

# ---------- Skills ----------
elif page == "Skills":
    st.subheader("Skills")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Technical**")
        st.write("- Add technical/mining-related skills (e.g. mine planning software, surveying, geology tools)")
        st.write("- Add programming/data tools if relevant")
    with col2:
        st.markdown("**Other**")
        st.write("- Add soft skills, leadership roles, certifications")

# ---------- Projects ----------
elif page == "Projects":
    st.subheader("Projects")
    st.write("List your projects, internships, or fieldwork here.")

    with st.expander("Project / Internship Name", expanded=True):
        st.write("Short description of the project or internship.")
        st.write("[Link to report / repo / demo](#)")

# ---------- Contact ----------
elif page == "Contact":
    st.subheader("Contact")
    st.write("Add your email, LinkedIn, GitHub, or any other links here.")
    st.write("- Email: your-email@example.com")
    st.write("- LinkedIn: https://linkedin.com/in/your-profile")
    st.write("- GitHub: https://github.com/your-username")

# ---------- Footer ----------
st.sidebar.markdown("---")
st.sidebar.caption("© 2026 Asimanshu Samal")
