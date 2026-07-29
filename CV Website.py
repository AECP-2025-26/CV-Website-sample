import streamlit as st

# ---------- Page Config ----------
st.set_page_config(
    page_title="Asimanshu Samal | Resume & Portfolio",
    page_icon="⛏️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Dark Mode Custom CSS ----------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Force Dark Backgrounds */
    .stApp {
        background-color: #0B0F17;
        color: #E2E8F0;
        font-family: 'Inter', sans-serif;
    }

    /* Dark Modern Hero Banner */
    .header-container {
        background: linear-gradient(135deg, #0F172A 0%, #1E1B4B 50%, #0F172A 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        color: #FFFFFF;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        margin-bottom: 2rem;
        text-align: center;
        border: 1px solid rgba(99, 102, 241, 0.2);
    }
    
    .header-name {
        font-size: 3.5rem;
        font-weight: 800;
        letter-spacing: -1px;
        margin: 0;
        background: linear-gradient(90deg, #38BDF8, #818CF8, #C084FC);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .header-subtitle {
        font-size: 1.25rem;
        color: #94A3B8;
        margin-top: 0.6rem;
        font-weight: 400;
    }

    .badge-container {
        margin-top: 1.2rem;
        display: flex;
        justify-content: center;
        gap: 12px;
        flex-wrap: wrap;
    }

    .badge {
        display: inline-block;
        padding: 0.4rem 1rem;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 50px;
        font-size: 0.85rem;
        color: #CBD5E1;
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Dark Glassmorphism Cards */
    .custom-card {
        background: #111827;
        border: 1px solid #1F2937;
        border-radius: 16px;
        padding: 1.8rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    
    .custom-card:hover {
        transform: translateY(-3px);
        border-color: #6366F1;
    }

    .card-title {
        font-size: 1.35rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: #38BDF8;
    }

    .card-subtitle {
        font-size: 0.95rem;
        color: #94A3B8;
        margin-bottom: 1rem;
        font-weight: 500;
    }

    .card-body {
        font-size: 0.98rem;
        line-height: 1.7;
        color: #CBD5E1;
    }

    /* Dark Metric Cards */
    .metric-card {
        background: rgba(17, 24, 39, 0.8);
        border-left: 4px solid #818CF8;
        border-top: 1px solid #1F2937;
        border-right: 1px solid #1F2937;
        border-bottom: 1px solid #1F2937;
        padding: 1.2rem;
        border-radius: 12px;
        text-align: left;
        margin-bottom: 1rem;
    }
    .metric-label {
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        color: #64748B;
        font-weight: 600;
    }
    .metric-value {
        font-size: 1.25rem;
        font-weight: 700;
        margin-top: 0.3rem;
        color: #F8FAFC;
    }

    /* YouTube Promo Box */
    .yt-card {
        background: linear-gradient(135deg, #18181B 0%, #27272A 100%);
        border: 1px solid #DC2626;
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }
    .yt-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #EF4444;
        margin-bottom: 0.5rem;
    }

    /* Sidebar Customization */
    section[data-testid="stSidebar"] {
        background-color: #0F172A !important;
        border-right: 1px solid #1E293B;
    }

    /* Custom Buttons / Links */
    a.yt-button {
        display: inline-block;
        background-color: #FF0000;
        color: white !important;
        padding: 0.6rem 1.2rem;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        margin-top: 0.5rem;
        transition: background-color 0.2s ease;
    }
    a.yt-button:hover {
        background-color: #CC0000;
    }

    /* Styled lists */
    .custom-card ul {
        padding-left: 1.2rem;
        margin-bottom: 0;
    }
    .custom-card li {
        margin-bottom: 0.4rem;
    }

    /* Profile Image Container */
    .profile-img-container img {
        border-radius: 18px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.6);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# ---------- Hero Header ----------
st.markdown("""
<div class="header-container">
    <div class="header-name">Asimanshu Samal</div>
    <div class="header-subtitle">Mining Engineering Student • Video Creator (@darkreaperedits) • Conservation Enthusiast</div>
    <div class="badge-container">
        <span class="badge">📍 IIT (ISM) Dhanbad</span>
        <span class="badge">🎓 B.Tech Mining Engineering</span>
        <span class="badge">🎬 Dark Reaper Edits</span>
        <span class="badge">🌱 Sustainable Mining</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- Sidebar Navigation ----------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select Page",
    ["Home", "About", "Education", "Hobbies & Interests", "Projects & Experience", "Contact"],
    index=0
)

# ---------- Home Page ----------
if page == "Home":
    col1, col2 = st.columns([1.3, 1], gap="large")
    
    with col1:
        st.subheader("Welcome 👋")
        st.write(
            """
            Welcome to my personal digital portfolio! I am an undergraduate Mining Engineering student at 
            **IIT (ISM) Dhanbad** on an eternal search for knowledge and information.
            
            My passions span the technical mechanics of **sustainable resource extraction**, 
            **environmental conservation**, reading, and **high-end video post-production**.
            """
        )
        
        st.markdown("### Quick Overview")
        
        m_col1, m_col2 = st.columns(2)
        with m_col1:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-label">Institution</div>
                <div class="metric-value">IIT (ISM) Dhanbad</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">YouTube Channel</div>
                <div class="metric-value">@darkreaperedits</div>
            </div>
            """, unsafe_allow_html=True)
            
        with m_col2:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-label">Specialization</div>
                <div class="metric-value">Mining Engineering</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Core Focus</div>
                <div class="metric-value">Sustainable Mining</div>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="profile-img-container">', unsafe_allow_html=True)
        try:
            st.image("Screenshot 2026-07-29 183446.png", use_container_width=True)
        except Exception:
            st.info("Image file `Screenshot 2026-07-29 183446.png` not found in root directory.")
        st.markdown('</div>', unsafe_allow_html=True)

# ---------- About Page ----------
elif page == "About":
    st.subheader("About Me")
    
    col1, col2 = st.columns([2, 1], gap="large")
    with col1:
        st.markdown("""
        <div class="custom-card">
            <div class="card-title">Background & Philosophy</div>
            <div class="card-body">
                Originally from <b>Rourkela, Odisha</b>, I developed an early interest in heavy industries and core engineering systems. Currently, I am pursuing my B.Tech in Mining Engineering at <b>IIT (ISM) Dhanbad</b>.
                <br><br>
                I am driven by an unending curiosity to learn across disciplines. Reach out for anything—no professional jargon required!
            </div>
        </div>

        <div class="custom-card">
            <div class="card-title">Key Interests & Philosophy</div>
            <div class="card-body">
                <ul>
                    <li><b>Sustainable Mining & Conservation:</b> Strongly interested in eco-friendly mineral extraction methods, land reclamation, mine safety, and environmental stewardship in engineering.</li>
                    <li><b>Avid Reading:</b> Passionate about continuous learning through literature, technical papers, and non-fiction.</li>
                    <li><b>Video Editing & Content Creation:</b> Founder and creator behind <b>Dark Reaper Edits</b>, focusing on high-octane editing, motion graphics, and post-production workflows.</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        try:
            st.image("Screenshot 2026-07-29 183446.png", use_container_width=True)
        except Exception:
            pass

# ---------- Education Page ----------
elif page == "Education":
    st.subheader("Academic History")
    
    st.markdown("""
    <div class="custom-card">
        <div class="card-title">Indian Institute of Technology (Indian School of Mines), Dhanbad</div>
        <div class="card-subtitle">Bachelor of Technology (B.Tech) in Mining Engineering | Current</div>
        <div class="card-body">
            Studying at one of India's premier mining engineering institutions.
            <br><br>
            <b>Key Focus Areas:</b>
            <ul>
                <li>Sustainable Surface & Underground Mining Operations</li>
                <li>Geomechanics, Rock Mechanics & Excavation</li>
                <li>Environmental Impacts of Mining & Mine Safety</li>
                <li>Mineral Economics & Resource Optimization</li>
            </ul>
        </div>
    </div>
    
    <div class="custom-card">
        <div class="card-title">Delhi Public School (DPS), Electronic City</div>
        <div class="card-subtitle">Senior Secondary Education (Class XII - CBSE) | <b>95.8%</b></div>
        <div class="card-body">
            Graduated with high distinction in Physics, Chemistry, and Mathematics (PCM).
        </div>
    </div>

    <div class="custom-card">
        <div class="card-title">Delhi Public School (DPS), Electronic City</div>
        <div class="card-subtitle">Secondary Education (Class X - CBSE) | <b>97.2%</b> (Best of 5)</div>
        <div class="card-body">
            Achieved top-tier academic standing across core sciences and mathematics.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------- Hobbies & Interests Page ----------
elif page == "Hobbies & Interests":
    st.subheader("Hobbies, Interests & Creative Work")
    
    # YouTube Featured Section
    st.markdown("""
    <div class="yt-card">
        <div class="yt-title">🎬 Dark Reaper Edits (YouTube)</div>
        <div style="color: #E4E4E7; line-height: 1.6;">
            I run an active video editing channel <b>@darkreaperedits</b> where I post high-quality edit edits, motion graphics, dynamic typography, and video transitions.
            <br><br>
            <a href="https://youtube.com/@darkreaperedits?si=X2zeEeIXC9luzx-s" target="_blank" class="yt-button">▶ Visit YouTube Channel</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.markdown("""
        <div class="custom-card">
            <div class="card-title">🎥 Video Editing & Software</div>
            <div class="card-body">
                Mastering industry-standard post-production tools to produce visually compelling content:
                <ul>
                    <li><b>Adobe After Effects:</b> Motion graphics, compositing, expression scripts, VFX, visual syncing.</li>
                    <li><b>Adobe Premiere Pro:</b> Timeline editing, sound design, color grading, sequence assembling.</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="custom-card">
            <div class="card-title">📚 Reading & Environmental Conservation</div>
            <div class="card-body">
                Outside of engineering and editing:
                <ul>
                    <li><b>Avid Reader:</b> Constantly exploring books across diverse genres, scientific publications, and technical literature.</li>
                    <li><b>Conservation & Sustainability:</b> Deep interest in integrating ecological conservation techniques into modern mining frameworks to minimize carbon footprint and environmental degradation.</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ---------- Projects & Experience Page ----------
elif page == "Projects & Experience":
    st.subheader("Projects & Creative Experience")

    with st.expander("🎥 Dark Reaper Edits - Channel & Video Production", expanded=True):
        st.markdown("""
        * **Platform:** [YouTube (@darkreaperedits)](https://youtube.com/@darkreaperedits?si=X2zeEeIXC9luzx-s)
        * **Role:** Content Creator, Editor, VFX Artist
        * **Tech Stack:** Adobe After Effects, Adobe Premiere Pro
        * **Overview:** Crafting high-grade video edits using complex keyframing, speed ramping, audio sync, and visual effects.
        """)

    with st.expander("🌱 Sustainable Mining & Conservation Studies"):
        st.markdown("""
        * **Domain:** Environmental Engineering & Sustainable Extraction
        * **Focus:** Researching zero-harm mining techniques, mine void reclamation, dust control technologies, and eco-friendly tailings management.
        """)

    with st.expander("📌 Streamlit Dark-Themed CV App"):
        st.markdown("""
        * **Role:** Developer
        * **Tech Stack:** Python, Streamlit, Custom Dark Mode CSS
        * **Overview:** Designed and deployed a custom interactive dark-mode portfolio showcasing academic credentials, projects, and social links.
        """)

# ---------- Contact Page ----------
elif page == "Contact":
    st.subheader("Get In Touch")
    
    col1, col2 = st.columns([1.5, 1], gap="large")
    
    with col1:
        st.markdown("""
        <div class="custom-card">
            <div class="card-title">Let's Connect</div>
            <div class="card-body">
                I am on an eternal search for knowledge and information — feel free to reach out for anything, no professional jargon needed!
                <br><br>
                📧 <b>Email:</b> <a href="mailto:asimanshusamal@gmail.com" style="color: #38BDF8;">asimanshusamal@gmail.com</a><br>
                🎬 <b>YouTube:</b> <a href="https://youtube.com/@darkreaperedits?si=X2zeEeIXC9luzx-s" target="_blank" style="color: #EF4444;">@darkreaperedits</a><br>
                📍 <b>Location:</b> IIT (ISM) Dhanbad, Jharkhand, India<br>
                🏠 <b>Hometown:</b> Rourkela, Odisha, India
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
