import streamlit as st

# ---------- Page Config ----------
st.set_page_config(
    page_title="Asimanshu Samal | Resume & Portfolio",
    page_icon="⛏️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Custom Modern CSS ----------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Hero Banner Styling */
    .header-container {
        background: linear-gradient(135deg, #0F2027 0%, #203A43 50%, #2C5364 100%);
        padding: 2.8rem 2rem;
        border-radius: 20px;
        color: #FFFFFF;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        margin-bottom: 2rem;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .header-name {
        font-size: 3.5rem;
        font-weight: 800;
        letter-spacing: -1px;
        margin: 0;
        background: linear-gradient(90deg, #FFFFFF, #B2FEFA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .header-subtitle {
        font-size: 1.25rem;
        color: #E2E8F0;
        margin-top: 0.6rem;
        font-weight: 400;
    }

    .badge-container {
        margin-top: 1rem;
        display: flex;
        justify-content: center;
        gap: 10px;
        flex-wrap: wrap;
    }

    .badge {
        display: inline-block;
        padding: 0.3rem 0.9rem;
        background: rgba(255, 255, 255, 0.12);
        border-radius: 50px;
        font-size: 0.85rem;
        color: #E2E8F0;
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.15);
    }

    /* Custom Glassmorphism Cards */
    .custom-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 1.6rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    
    .custom-card:hover {
        transform: translateY(-2px);
        border-color: rgba(56, 178, 172, 0.4);
    }

    @media (prefers-color-scheme: light) {
        .custom-card {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.04);
        }
    }

    .card-title {
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
        color: #319795;
    }

    .card-subtitle {
        font-size: 0.95rem;
        color: #A0AEC0;
        margin-bottom: 1rem;
        font-weight: 500;
    }

    .card-body {
        font-size: 0.98rem;
        line-height: 1.65;
    }

    /* Styled Metrics */
    .metric-card {
        background: linear-gradient(135deg, rgba(49, 151, 149, 0.1) 0%, rgba(49, 151, 149, 0.02) 100%);
        border-left: 4px solid #319795;
        padding: 1.2rem;
        border-radius: 12px;
        text-align: left;
        margin-bottom: 1rem;
    }
    .metric-label {
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        color: #718096;
        font-weight: 600;
    }
    .metric-value {
        font-size: 1.25rem;
        font-weight: 700;
        margin-top: 0.3rem;
    }

    /* List styling inside cards */
    .custom-card ul {
        padding-left: 1.2rem;
        margin-bottom: 0;
    }
    .custom-card li {
        margin-bottom: 0.4rem;
    }

    /* Image styling */
    .profile-img-container img {
        border-radius: 18px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.18);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# ---------- Hero Header ----------
st.markdown("""
<div class="header-container">
    <div class="header-name">Asimanshu Samal</div>
    <div class="header-subtitle">Mining Engineering Student • Video Content Creator • Tech Enthusiast</div>
    <div class="badge-container">
        <span class="badge">📍 IIT (ISM) Dhanbad</span>
        <span class="badge">🎓 B.Tech Mining Engineering</span>
        <span class="badge">🏠 Rourkela, Odisha</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- Sidebar Navigation ----------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select Page",
    ["Home", "About", "Education", "Skills & Hobbies", "Projects & Experience", "Contact"],
    index=0
)

# ---------- Home Page ----------
if page == "Home":
    col1, col2 = st.columns([1.3, 1], gap="large")
    
    with col1:
        st.subheader("Welcome 👋")
        st.write(
            """
            Welcome to my personal interactive platform! I am an undergraduate Mining Engineering student at 
            **IIT (ISM) Dhanbad** with an appetite for learning across engineering, technology, and visual media creation.
            
            Whether analyzing subsurface mechanics, crafting motion graphics in Adobe After Effects, or exploring software automation, 
            I operate with a simple ethos: **stay curious, communicate directly, and build value.**
            """
        )
        
        st.markdown("### Highlights at a Glance")
        
        m_col1, m_col2 = st.columns(2)
        with m_col1:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-label">Institution</div>
                <div class="metric-value">IIT (ISM) Dhanbad</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Secondary (12th)</div>
                <div class="metric-value">95.8% (DPS E City)</div>
            </div>
            """, unsafe_allow_html=True)
            
        with m_col2:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-label">Specialization</div>
                <div class="metric-value">Mining Engineering</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">High School (10th)</div>
                <div class="metric-value">97.2% (Best of 5)</div>
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
                Hailing from <b>Rourkela, Odisha</b>—a city rich in industrial heritage—I naturally developed an interest in core engineering systems and resource extraction technologies early on. This led me to pursue my B.Tech in Mining Engineering at the premier <b>Indian Institute of Technology (Indian School of Mines), Dhanbad</b>.
                <br><br>
                Beyond standard academic curricula, I consider myself a lifelong learner on an eternal search for knowledge. I believe the best engineering outcomes happen when rigorous technical analysis meets effective visual communication.
            </div>
        </div>

        <div class="custom-card">
            <div class="card-title">Core Interests & Goals</div>
            <div class="card-body">
                <ul>
                    <li><b>Resource Optimization & Mining Tech:</b> Understanding modern geomechanics, underground and surface extraction method planning, and sustainable mining solutions.</li>
                    <li><b>Digital Content Creation:</b> Advanced video editing, visual effects, and post-production workflows utilizing industry-standard toolsets.</li>
                    <li><b>Interdisciplinary Problem Solving:</b> Bridging core field engineering with modern software, simulation tools, and media storytelling.</li>
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
            Enrolled in one of Asia's most historic mining education departments. The curriculum blends foundational engineering principles with specialized mineral industry training.
            <br><br>
            <b>Key Focus Areas:</b>
            <ul>
                <li>Surface & Underground Mining Methods</li>
                <li>Mine Automation, Safety, & Environmental Engineering</li>
                <li>Geomechanics, Rock Mechanics, and Excavation Technologies</li>
                <li>Mineral Resource Estimation & Mine Planning</li>
            </ul>
        </div>
    </div>
    
    <div class="custom-card">
        <div class="card-title">Delhi Public School (DPS), Electronic City</div>
        <div class="card-subtitle">Senior Secondary Education (Class XII - CBSE) | <b>95.8%</b></div>
        <div class="card-body">
            Demonstrated academic excellence in Physics, Chemistry, and Mathematics (PCM), achieving top academic tier ranking.
        </div>
    </div>

    <div class="custom-card">
        <div class="card-title">Delhi Public School (DPS), Electronic City</div>
        <div class="card-subtitle">Secondary Education (Class X - CBSE) | <b>97.2%</b> (Best of 5)</div>
        <div class="card-body">
            Graduated with distinction, laying a robust foundation in quantitative sciences, mathematics, and analytical reasoning.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------- Skills & Hobbies Page ----------
elif page == "Skills & Hobbies":
    st.subheader("Skills, Tools & Hobbies")
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.markdown("""
        <div class="custom-card">
            <div class="card-title">🎬 Post-Production & Motion Graphics</div>
            <div class="card-body">
                I specialize in high-end video post-production, transforming raw footage into compelling narrative and visual content.
                <br><br>
                <b>Primary Tools:</b>
                <ul>
                    <li><b>Adobe After Effects:</b> Motion graphics design, VFX compositing, dynamic typography, expression scripts, and speed ramping.</li>
                    <li><b>Adobe Premiere Pro:</b> Narrative editing, audio normalization, multi-camera syncing, color grading, and timeline workflow management.</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="custom-card">
            <div class="card-title">🛠️ Technical & Academic Competencies</div>
            <div class="card-body">
                Alongside multimedia editing, my engineering toolkit encompasses quantitative analysis and technical computing:
                <ul>
                    <li><b>Engineering Fundamentals:</b> Mine design principles, survey data processing, and rock mechanics.</li>
                    <li><b>Software & Productivity:</b> Python scripting, Streamlit UI development, Git version control, LaTeX documentation.</li>
                    <li><b>Analytical Thinking:</b> Structured problem-solving, quantitative modeling, and technical reporting.</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ---------- Projects & Experience Page ----------
elif page == "Projects & Experience":
    st.subheader("Projects & Technical Work")
    
    st.write("A selection of academic projects, technical exploration, and creative work.")

    with st.expander("📌 Streamlit Portfolio & CV Web Application", expanded=True):
        st.markdown("""
        * **Role:** Developer
        * **Tech Stack:** Python, Streamlit, HTML5/Custom CSS
        * **Overview:** Designed and built an interactive, glassmorphism-themed personal web app featuring real-time state navigation, custom metrics, and dynamic rendering.
        * **Key Outcome:** Created a responsive, user-friendly digital resume eliminating the need for static PDFs.
        """)
        st.write("[📄 View Source Code / Repo](#)")

    with st.expander("📌 Advanced Motion Graphics & Editing Projects"):
        st.markdown("""
        * **Role:** Video Editor / Visual Effects Designer
        * **Software:** Adobe After Effects, Premiere Pro
        * **Overview:** Created short-form and long-form video edits incorporating custom motion graphics, kinetic typography, seamless transitions, and color grading.
        * **Key Outcome:** Developed an efficient visual workflow for rapid video assembly without sacrificing rendering quality.
        """)

    with st.expander("📌 Mining Engineering Fieldwork & Lab Studies"):
        st.markdown("""
        * **Role:** Student Researcher / Trainee
        * **Focus Area:** Underground & Open-pit Mining Operations
        * **Overview:** Practical laboratory analysis and theoretical evaluations covering rock specimen testing, ventilation design parameters, and heavy machinery utilization in modern extraction sites.
        """)

# ---------- Contact Page ----------
elif page == "Contact":
    st.subheader("Get In Touch")
    
    col1, col2 = st.columns([1.5, 1], gap="large")
    
    with col1:
        st.markdown("""
        <div class="custom-card">
            <div class="card-title">Reach Out</div>
            <div class="card-body">
                I am always open to discussing new opportunities, academic collaborations, creative video projects, or general engineering topics. No formal jargon needed—feel free to drop a message!
                <br><br>
                📧 <b>Email:</b> <a href="mailto:asimanshusamal@gmail.com">asimanshusamal@gmail.com</a><br>
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
