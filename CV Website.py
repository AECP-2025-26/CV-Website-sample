import streamlit as st

# ---------- Page Config ----------
st.set_page_config(
    page_title="Asimanshu Samal | CV",
    page_icon="⛏️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Custom Modern CSS ----------
st.markdown("""
<style>
    /* Global Styling & Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Subtle Animated Gradient Header */
    .header-container {
        background: linear-gradient(135deg, #0F2027 0%, #203A43 50%, #2C5364 100%);
        padding: 2.5rem 1.5rem;
        border-radius: 20px;
        color: #FFFFFF;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        margin-bottom: 2rem;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .header-name {
        font-size: 3.2rem;
        font-weight: 800;
        letter-spacing: -1px;
        margin: 0;
        background: linear-gradient(90deg, #FFFFFF, #E0EFCF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .header-subtitle {
        font-size: 1.15rem;
        color: #A0AEC0;
        margin-top: 0.5rem;
        font-weight: 400;
    }

    .badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        background: rgba(255, 255, 255, 0.15);
        border-radius: 50px;
        font-size: 0.85rem;
        color: #E2E8F0;
        margin-top: 0.8rem;
        backdrop-filter: blur(5px);
    }

    /* Cards / Glassmorphism */
    .custom-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .custom-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        border-color: rgba(66, 153, 225, 0.3);
    }

    /* Soft light theme support fallback */
    @media (prefers-color-scheme: light) {
        .custom-card {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
        }
    }

    .card-title {
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
        color: #3182CE;
    }

    .card-subtitle {
        font-size: 0.95rem;
        color: #A0AEC0;
        margin-bottom: 0.8rem;
    }

    .card-body {
        font-size: 1rem;
        line-height: 1.6;
    }

    /* Custom Metric Cards */
    .metric-card {
        background: linear-gradient(135deg, rgba(49, 130, 206, 0.08) 0%, rgba(49, 130, 206, 0.02) 100%);
        border-left: 4px solid #3182CE;
        padding: 1.2rem;
        border-radius: 12px;
        text-align: left;
    }
    .metric-label {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #718096;
        font-weight: 600;
    }
    .metric-value {
        font-size: 1.35rem;
        font-weight: 700;
        margin-top: 0.3rem;
    }

    /* Sidebar Tweaks */
    section[data-testid="stSidebar"] {
        background-color: rgba(15, 23, 42, 0.02);
    }

    /* Image styling */
    .profile-img-container img {
        border-radius: 16px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# ---------- Hero Header ----------
st.markdown("""
<div class="header-container">
    <div class="header-name">Asimanshu Samal</div>
    <div class="header-subtitle">Mining Engineering Student & Tech Enthusiast</div>
    <div class="badge">📍 IIT (ISM) Dhanbad</div>
</div>
""", unsafe_allow_html=True)

# ---------- Sidebar Navigation ----------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select Page",
    ["Home", "About", "Education", "Hobbies", "Projects", "Contact"],
    index=0
)

# ---------- Home Page ----------
if page == "Home":
    col1, col2 = st.columns([1.2, 1], gap="large")
    
    with col1:
        st.subheader("Welcome 👋")
        st.write(
            """
            Welcome to my personal digital resume! I am on an eternal search for knowledge 
            and information—always looking to connect, learn, and collaborate. 
            Feel free to explore my background, academic credentials, projects, and interests.
            """
        )
        
        st.markdown("### Quick Stats")
        m_col1, m_col2 = st.columns(2)
        with m_col1:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-label">Institute</div>
                <div class="metric-value">IIT (ISM) Dhanbad</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("""
            <div class="metric-card">
                <div class="metric-label">Hometown</div>
                <div class="metric-value">Rourkela, Odisha</div>
            </div>
            """, unsafe_allow_html=True)
            
        with m_col2:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-label">Branch</div>
                <div class="metric-value">Mining Eng.</div>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="profile-img-container">', unsafe_allow_html=True)
        try:
            st.image("Screenshot 2026-07-29 183446.png", use_container_width=True)
        except Exception:
            st.info("Image file `Screenshot 2026-07-29 183446.png` not found in current directory.")
        st.markdown('</div>', unsafe_allow_html=True)

# ---------- About ----------
elif page == "About":
    st.subheader("About Me")
    
    col1, col2 = st.columns([2, 1], gap="large")
    with col1:
        st.markdown("""
        <div class="custom-card">
            <div class="card-title">Who I Am</div>
            <div class="card-body">
                I'm <b>Asimanshu Samal</b>, originally from Rourkela, Odisha, and currently pursuing my undergraduate degree in 
                <b>Mining Engineering at IIT (ISM) Dhanbad</b>.<br><br>
                Driven by curiosity, I'm on a continuous quest to acquire new skills, explore diverse domains—from heavy engineering to digital media production—and connect with like-minded individuals.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        try:
            st.image("Screenshot 2026-07-29 183446.png", use_container_width=True)
        except Exception:
            pass

# ---------- Education ----------
elif page == "Education":
    st.subheader("Education")
    
    st.markdown("""
    <div class="custom-card">
        <div class="card-title">Indian Institute of Technology/ISM Dhanbad</div>
        <div class="card-subtitle">B.Tech in Mining Engineering</div>
        <div class="card-body">
            Currently pursuing undergraduate studies with a focus on mining techniques, geo-mechanics, and engineering fundamentals.
        </div>
    </div>
    
    <div class="custom-card">
        <div class="card-title">Senior Secondary (12th Grade)</div>
        <div class="card-subtitle">DPS E City | <b>95.8%</b></div>
        <div class="card-body">
            Completed Class XII with distinction under CBSE curriculum.
        </div>
    </div>

    <div class="custom-card">
        <div class="card-title">Secondary School (10th Grade)</div>
        <div class="card-subtitle">DPS E City | <b>97.2%</b> (Best of 5)</div>
        <div class="card-body">
            Completed Class X with high academic standing.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------- Hobbies ----------
elif page == "Hobbies":
    st.subheader("Hobbies & Technical Interests")
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.markdown("""
        <div class="custom-card">
            <div class="card-title">🎬 Video Editing & Post-Production</div>
            <div class="card-body">
                Passionate about visual storytelling, motion design, and audio-visual timing. 
                I create and refine content with industry-standard toolsets.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="custom-card">
            <div class="card-title">🛠️ Software & Tools</div>
            <div class="card-body">
                <ul>
                    <li><b>Adobe After Effects:</b> Motion graphics, compositing, visual FX.</li>
                    <li><b>Adobe Premiere Pro:</b> Timeline editing, color grading, sound mixing.</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ---------- Projects ----------
elif page == "Projects":
    st.subheader("Projects & Fieldwork")
    
    with st.expander("🚀 Project / Internship Title", expanded=True):
        st.write("Short detailed description of your project, internship responsibilities, or mining site fieldwork.")
        st.markdown("**Key Skills Used:** Python, Data Analysis, CAD, Field Research")
        st.write("[📄 View Project Report / Repository](#)")

# ---------- Contact ----------
elif page == "Contact":
    st.subheader("Get In Touch")
    
    col1, col2 = st.columns([1.5, 1], gap="large")
    
    with col1:
        st.markdown("""
        <div class="custom-card">
            <div class="card-title">Let's Connect</div>
            <div class="card-body">
                I am on an eternal search for knowledge and information — feel free to reach out for anything, no professional jargon required!
                <br><br>
                📧 <b>Email:</b> <a href="mailto:asimanshusamal@gmail.com">asimanshusamal@gmail.com</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        try:
            st.image("Screenshot 2026-07-29 183446.png", use_container_width=True)
        except Exception:
            pass

# ---------- Footer ----------
st.sidebar.markdown("---")
st.sidebar.caption("© 2026 Asimanshu Samal • Built with Streamlit")
