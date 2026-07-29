import streamlit as st

# ---------- Page Config ----------
st.set_page_config(
    page_title="Asimanshu Samal | Resume & Portfolio",
    page_icon="⛏️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Dark Mode Custom CSS with Full Gradient Background ----------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Full Page Fixed Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #090D16 0%, #111827 35%, #1E1B4B 70%, #0F172A 100%) !important;
        background-attachment: fixed !important;
        color: #FFFFFF !important;
        font-family: 'Inter', sans-serif;
    }

    /* Target Streamlit default paragraph/text elements for high contrast */
    .stApp p, .stApp span, .stApp div {
        color: #F8FAFC;
    }

    /* Glassmorphism Hero Banner */
    .header-container {
        background: rgba(15, 23, 42, 0.65);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        padding: 3rem 2rem;
        border-radius: 20px;
        color: #FFFFFF;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        margin-bottom: 2rem;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.15);
    }
    
    .header-name {
        font-size: 3.6rem;
        font-weight: 800;
        letter-spacing: -1px;
        margin: 0;
        background: linear-gradient(90deg, #38BDF8, #818CF8, #E0E7FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .header-subtitle {
        font-size: 1.3rem;
        color: #E2E8F0 !important;
        margin-top: 0.6rem;
        font-weight: 500;
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
        padding: 0.4rem 1.1rem;
        background: rgba(255, 255, 255, 0.08);
        border-radius: 50px;
        font-size: 0.9rem;
        color: #F1F5F9 !important;
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* Glass Cards */
    .custom-card {
        background: rgba(17, 24, 39, 0.7);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 16px;
        padding: 1.8rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.37);
        transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
    }
    
    .custom-card:hover {
        transform: translateY(-3px);
        border-color: #38BDF8;
        box-shadow: 0 12px 40px rgba(56, 189, 248, 0.15);
    }

    /* Highlight Card for AECP Project */
    .featured-card {
        background: linear-gradient(135deg, rgba(30, 27, 75, 0.75) 0%, rgba(15, 23, 42, 0.85) 100%);
        backdrop-filter: blur(14px);
        border: 1.5px solid #818CF8;
        border-radius: 16px;
        padding: 1.8rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 35px rgba(129, 140, 248, 0.2);
    }

    .card-title {
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: #38BDF8 !important;
    }

    .featured-title {
        font-size: 1.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        color: #A5B4FC !important;
    }

    .card-subtitle {
        font-size: 1rem;
        color: #CBD5E1 !important;
        margin-bottom: 1rem;
        font-weight: 500;
    }

    .card-body {
        font-size: 1.02rem;
        line-height: 1.7;
        color: #FFFFFF !important;
    }

    /* Metric Cards */
    .metric-card {
        background: rgba(15, 23, 42, 0.75);
        backdrop-filter: blur(10px);
        border-left: 4px solid #38BDF8;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        padding: 1.2rem;
        border-radius: 12px;
        text-align: left;
        margin-bottom: 1rem;
    }
    .metric-label {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        color: #94A3B8 !important;
        font-weight: 600;
    }
    .metric-value {
        font-size: 1.3rem;
        font-weight: 700;
        margin-top: 0.3rem;
        color: #FFFFFF !important;
    }

    /* Sidebar Customization */
    section[data-testid="stSidebar"] {
        background-color: rgba(11, 15, 23, 0.7) !important;
        backdrop-filter: blur(15px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Action Link Button */
    a.action-button {
        display: inline-block;
        background: linear-gradient(90deg, #4F46E5, #6366F1);
        color: #FFFFFF !important;
        padding: 0.65rem 1.3rem;
        border-radius: 10px;
        text-decoration: none;
        font-weight: 600;
        margin-top: 0.8rem;
        box-shadow: 0 4px 15px rgba(79, 70, 229, 0.4);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    a.action-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(79, 70, 229, 0.6);
    }

    /* Styled Lists */
    .custom-card ul, .featured-card ul {
        padding-left: 1.2rem;
        margin-bottom: 0;
    }
    .custom-card li, .featured-card li {
        margin-bottom: 0.4rem;
        color: #F8FAFC !important;
    }

    /* Profile Image Container */
    .profile-img-container img {
        border-radius: 18px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# ---------- Hero Header ----------
st.markdown("""
<div class="header-container">
    <div class="header-name">Asimanshu Samal</div>
    <div class="header-subtitle">Mining Engineering Student • AECP AI Lead • Conservation Enthusiast</div>
    <div class="badge-container">
        <span class="badge">📍 IIT (ISM) Dhanbad</span>
        <span class="badge">🎓 B.Tech Mining Engineering</span>
        <span class="badge">🤖 AECP Project</span>
        <span class="badge">🌱 Sustainable Mining</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- Sidebar Navigation ----------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select Page",
    ["Home", "About", "Education", "Projects & Experience", "Hobbies & Interests", "Contact"],
    index=0
)

# ---------- Home Page ----------
if page == "Home":
    col1, col2 = st.columns([1.3, 1], gap="large")
    
    with col1:
        st.subheader("Welcome 👋")
        st.markdown(
            """
            Welcome to my personal digital portfolio! I am an undergraduate Mining Engineering student at 
            **IIT (ISM) Dhanbad** on an eternal search for knowledge and information.
            
            My focus centers on **AECP (AI-driven platform)**, technical mechanics of **sustainable resource extraction**, 
            **environmental conservation**, reading, and digital content creation.
            """
        )
        
        st.markdown("### Featured Highlight")
        st.markdown("""
        <div class="featured-card">
            <div class="featured-title">🚀 AECP Project</div>
            <div class="card-subtitle">AI & Educational Technology Initiative</div>
            <div class="card-body">
                Working on AECP to leverage artificial intelligence for enhanced learning and practical frameworks.
                <br><br>
                <a href="https://sites.google.com/view/aecp-ai/home" target="_blank" class="action-button">🌐 Visit AECP Website</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="profile-img-container">', unsafe_allow_html=True)
        try:
            st.image("Screenshot 2026-07-29 183446.png", use_container_width=True)
        except Exception:
            st.info("Image file `Screenshot 2026-07-29 183446.png` not found in root directory.")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="metric-card" style="margin-top: 1rem;">
            <div class="metric-label">Institution</div>
            <div class="metric-value">IIT (ISM) Dhanbad</div>
        </div>
        <div class="metric-card">
            <div class="metric-label">Branch</div>
            <div class="metric-value">Mining Engineering</div>
        </div>
        """, unsafe_allow_html=True)

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
                I am driven by an unending curiosity to learn across disciplines—from core mining mechanics to AI tools like AECP. Reach out for anything—no professional jargon required!
            </div>
        </div>

        <div class="custom-card">
            <div class="card-title">Core Focus Areas</div>
            <div class="card-body">
                <ul>
                    <li><b>AECP Initiative:</b> Developing AI-integrated resources for technical accessibility and streamlined learning.</li>
                    <li><b>Sustainable Mining & Conservation:</b> Interested in eco-friendly mineral extraction, land reclamation, and environmental stewardship in core engineering.</li>
                    <li><b>Continuous Learning & Editing:</b> Avid reader with background experience in video editing (such as <i>Dark Reaper Edits</i>).</li>
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

# ---------- Projects & Experience Page ----------
elif page == "Projects & Experience":
    st.subheader("Key Projects & Experience")

    # Flagship AECP Project
    st.markdown("""
    <div class="featured-card">
        <div class="featured-title">🌟 AECP (AI Platform)</div>
        <div class="card-subtitle">Flagship Project | <a href="https://sites.google.com/view/aecp-ai/home" target="_blank" style="color: #A5B4FC;">sites.google.com/view/aecp-ai</a></div>
        <div class="card-body">
            AECP is an AI-driven platform focused on empowering technical research, streamlining workflow accessibility, and deploying modern artificial intelligence tools for educational and domain-specific applications.
            <br><br>
            <b>Highlights:</b>
            <ul>
                <li>Designed for accessible AI integration across academic workflows.</li>
                <li>Structured knowledge hubs for rapid exploration and learning.</li>
            </ul>
            <a href="https://sites.google.com/view/aecp-ai/home" target="_blank" class="action-button">🔗 Open AECP Site</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🌱 Sustainable Mining & Conservation Studies"):
        st.markdown("""
        * **Domain:** Environmental Engineering & Sustainable Extraction
        * **Focus:** Researching zero-harm mining techniques, mine void reclamation, dust control technologies, and eco-friendly tailings management.
        """)

    with st.expander("📌 Streamlit Glassmorphism Web App"):
        st.markdown("""
        * **Role:** Developer
        * **Tech Stack:** Python, Streamlit, Custom CSS
        * **Overview:** Designed and deployed a dynamic personal application featuring high-contrast gradient UI elements and glassmorphism styling.
        """)

    with st.expander("🎥 Media Production & Video Editing"):
        st.markdown("""
        * **Projects:** Video edits under *@darkreaperedits*
        * **Tech Stack:** Adobe After Effects, Adobe Premiere Pro
        * **Overview:** Content creation and post-production video editing experience.
        """)

# ---------- Hobbies & Interests Page ----------
elif page == "Hobbies & Interests":
    st.subheader("Hobbies & Personal Interests")
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.markdown("""
        <div class="custom-card">
            <div class="card-title">📚 Reading & Conservation</div>
            <div class="card-body">
                <ul>
                    <li><b>Avid Reading:</b> Passionate about exploring books across non-fiction, technology, and literature.</li>
                    <li><b>Environmental Conservation:</b> Keen interest in sustainable engineering methods that minimize ecological footprints in resource sectors.</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="custom-card">
            <div class="card-title">🎬 Video Editing</div>
            <div class="card-body">
                Casual editing and motion graphics creation using industry-standard tools:
                <ul>
                    <li><b>Adobe After Effects:</b> Visual effects, dynamic keyframing.</li>
                    <li><b>Adobe Premiere Pro:</b> Post-production and sound editing.</li>
                    <li><b>YouTube Channel:</b> <a href="https://youtube.com/@darkreaperedits?si=X2zeEeIXC9luzx-s" target="_blank" style="color: #38BDF8;">@darkreaperedits</a></li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

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
                📧 <b>Email:</b> <a href="mailto:asimanshusamal@gmail.com" style="color: #38BDF8; font-weight: 600;">asimanshusamal@gmail.com</a><br>
                🤖 <b>AECP Project:</b> <a href="https://sites.google.com/view/aecp-ai/home" target="_blank" style="color: #A5B4FC; font-weight: 600;">sites.google.com/view/aecp-ai</a><br>
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
