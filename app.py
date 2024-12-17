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

# # Education Section
# section_header("Education")
# st.markdown("""
# <div class="education-card">
#     <h3>B.Tech. in Artificial Intelligence and Machine Learning</h3>
#     <h4>Vivekananda Institute of Professional Studies - Technical Campus</h4>
#     <p>2022-2026</p>
#     <p><strong>CGPA: 8.608</strong></p>
#     <h4>Relevant Coursework:</h4>
#     <ul>
#         <li>Data Structures</li>
#         <li>Software Methodology</li>
#         <li>Artificial Intelligence</li>
#         <li>Database Management</li>
#         <li>Data Science</li>
#         <li>Internet Networks</li>
#         <li>Machine Learning</li>
#         <li>Statistics</li>
#     </ul>
# </div>
# """, unsafe_allow_html=True)

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
            <li>Developed a web application to automate the grading process, reducing manual grading time by 70% for teachers.</li>
            <li>Implemented the model using PyTorch and BERT architecture, improving grading accuracy by 15% compared to traditional keyword-based methods.</li>
            <li>Used Kmeans clustering to group similar student responses together and identify common patterns and themes.</li>
            <li>Graded student responses using cosine similarity to compare their vector representations with the correct answer vectors.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="project-card">
        <h3>Financial News Sentiment Analysis</h3>
        <p><strong>Python, FINBERT | Sep. 2024</strong></p>
        <ul>
            <li>Automated real-time financial news scraping from Yahoo Finance using BeautifulSoup for data acquisition.</li>
            <li>Built a sentiment analysis pipeline with FinBERT, transformers, and PyTorch to classify sentiments as negative, neutral, or positive.</li>
            <li>Visualized sentiment distributions using matplotlib, seaborn, and pywaffle through bar charts, pie charts, heatmaps, and bubble plots.</li>
            <li>Processed and transformed the scraped data using pandas and numpy to prepare it for sentiment analysis.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="project-card">
        <h3>Phishing Email Detector</h3>
        <p><strong>Python, NLP | Jul. 2024</strong></p>
        <ul>
            <li>Developed a machine learning model to detect phishing emails with high accuracy of 97%.</li>
            <li>Designed and implemented the front-end using the Streamlit framework to provide a user-friendly web interface for real-time email phishing detection.</li>
            <li>Utilized Pandas and NLTK for data preprocessing, TfidfVectorizer from Scikit-learn for feature extraction, and a Multinomial Naive Bayes classifier to classify emails as phishing or non-phishing.</li>
            <li> Achieved high model performance, evaluated using accuracy score and classification report metrics. </li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-card">
        <h3>Flexion: AI-Powered Fitness Coach</h3>
        <p><strong>Python, HTML, CSS, React | Nov. 2024</strong></p>
        <ul>
            <li>Built an interactive React-based front-end to support real-time posture correction, progress tracking, and adaptive workout recommendations.</li>
            <li>Collaborated on AI integration, leveraging Generative AI (GPT-2) for dynamic workout planning and TensorFlow for pose estimation, achieving 90%+ accuracy in real-time posture recognition.</li>
            <li>Ensured seamless frontend-backend communication via FastAPI, reducing response latency by 30%, and enabling personalized fitness guidance and live feedback.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


# Education Section
section_header("Education")
st.markdown("""
<div class="education-card">
    <h3>B.Tech. in Artificial Intelligence and Machine Learning</h3>
    <h4>Vivekananda Institute of Professional Studies - Technical Campus</h4>
    <p>2022-2026</p>
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
