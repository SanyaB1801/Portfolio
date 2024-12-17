import streamlit as st
from streamlit_timeline import timeline
from streamlit_lottie import st_lottie
import requests

# Set page config
st.set_page_config(page_title="Sanya Behera - Portfolio", layout="wide")

# Custom CSS
def local_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

# Helper function for section headers
def section_header(title, custom_class="section-header"):
    st.markdown(f'<h2 class="{custom_class}">{title}</h2>', unsafe_allow_html=True)

# Lottie Animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Header Section
st.markdown('<h1 class="main-header">Sanya Behera</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">AI and Machine Learning Enthusiast</p>', unsafe_allow_html=True)

# Lottie Animation
lottie_url = "https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json"
lottie_json = load_lottieurl(lottie_url)
st_lottie(lottie_json, height=200, key="coding")

# Contact Information - Updated for neat columns
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<a href="mailto:sanyabehera13@gmail.com" class="contact-link"><i class="fas fa-envelope"></i> Email</a>', unsafe_allow_html=True)
with col2:
    st.markdown('<a href="https://linkedin.com/in/sanya-behera" class="contact-link"><i class="fab fa-linkedin"></i> LinkedIn</a>', unsafe_allow_html=True)
with col3:
    st.markdown('<a href="https://github.com/SanyaB1801" class="contact-link"><i class="fab fa-github"></i> GitHub</a>', unsafe_allow_html=True)

# About Me Section
section_header("About Me")
st.info("""
I'm a B.Tech. student in Artificial Intelligence and Machine Learning at Vivekananda Institute of Professional Studies - Technical Campus. 
Passionate about AI, machine learning, and data science, I'm constantly working on innovative projects and expanding my skills in these cutting-edge fields.
""")

# Education Section
section_header("Education")
st.markdown("""
<div class="education-card">
    <h3>B.Tech. in Artificial Intelligence and Machine Learning</h3>
    <h4>Vivekananda Institute of Professional Studies - Technical Campus</h4>
    <p>2022-2026</p>
    <p><strong>CGPA: 8.608</strong></p>
    <h4>Relevant Coursework:</h4>
    <ul>
        <li>Data Structures</li>
        <li>Software Methodology</li>
        <li>Artificial Intelligence</li>
        <li>Database Management</li>
        <li>Data Science</li>
        <li>Internet Networks</li>
        <li>Machine Learning</li>
        <li>Statistics</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Experience Section
section_header("Experience")
timeline_data = [
    {
        "title": "Summer Intern",
        "content": "IIT Guwahati",
        "date": "Jul 2024 – Aug 2024",
        "description": "Enhanced knowledge of secure coding, system security, and cybersecurity protocols. Created a Streamlit-based Phishing Email Detector with 95%+ accuracy."
    },
    {
        "title": "Contributor",
        "content": "Girlscript Summer of Code",
        "date": "May 2024 – Aug 2024",
        "description": "Contributed to diverse projects, achieved top 20% ranking, and refined open-source development skills."
    }
]
timeline(timeline_data, height=400)

# Projects Section
section_header("Projects")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="project-card">
        <h3>Automated Grading System</h3>
        <p><strong>Python, SQL | Apr. 2024</strong></p>
        <ul>
            <li>Reduced manual grading time by 70%</li>
            <li>Improved grading accuracy by 15%</li>
            <li>Achieved 90% grading consistency rate</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="project-card">
        <h3>Flexion: AI-Powered Fitness Coach</h3>
        <p><strong>Python, HTML, CSS, React | Nov. 2024</strong></p>
        <ul>
            <li>90%+ accuracy in real-time posture recognition</li>
            <li>Reduced response latency by 30%</li>
            <li>Implemented dynamic workout planning with GPT-2</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Skills Section
section_header("Technical Skills")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="skills-card">
        <h3>Languages</h3>
        <p>Python, Java, C, Dart, SQL</p>
        <h3>Web</h3>
        <p>HTML, CSS, JavaScript, React</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="skills-card">
        <h3>ML and Data Science</h3>
        <p>TensorFlow, PyTorch, Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn, NLTK, SpaCy, FinBERT, Transformers, OpenCV</p>
        <h3>UI/UX</h3>
        <p>Figma, Tkinter, Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

# Extracurricular Activities Section
section_header("Extracurricular Activities")
st.markdown("""
<div class="extracurricular-card">
    <div class="activity">
        <h3>Newsletter Editorial Team</h3>
        <p>Core Member | Mar. 2024 – Jul. 2024</p>
    </div>
    <div class="activity">
        <h3>Antarman - The Yoga and Meditation club</h3>
        <p>Social Media Team | Jun. 2024 – Present</p>
    </div>
    <div class="activity">
        <h3>Career Development Cell</h3>
        <p>Creative Team | May 2024 – Present</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer Section
st.markdown('---')
st.markdown('<p class="footer">© 2023 Sanya Behera. All rights reserved.</p>', unsafe_allow_html=True)
