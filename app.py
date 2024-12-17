import streamlit as st

# Set page config
st.set_page_config(page_title="Sanya Behera - Portfolio", layout="wide")

# Custom CSS
def local_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

# Helper function for section headers
def section_header(title):
    st.markdown(f'<h2 class="section-header">{title}</h2>', unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">Sanya Behera</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">AI and Machine Learning Enthusiast</p>', unsafe_allow_html=True)

# Contact information
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('[Email](mailto:sanyabehera13@gmail.com)')
with col2:
    st.markdown('[LinkedIn](https://linkedin.com/in/sanya-behera)')
with col3:
    st.markdown('[GitHub](https://github.com/SanyaB1801)')

# About
section_header("About Me")
st.write("""
I'm a B.Tech. student in Artificial Intelligence and Machine Learning at Vivekananda Institute of Professional Studies - Technical Campus. 
Passionate about AI, machine learning, and data science, I'm constantly working on innovative projects and expanding my skills in these cutting-edge fields.
""")

# Education
section_header("Education")
st.markdown("""
### B.Tech. in Artificial Intelligence and Machine Learning
**Vivekananda Institute of Professional Studies - Technical Campus**
- 2022-2026
- CGPA: 8.608

#### Relevant Coursework:
- Data Structures
- Software Methodology
- Artificial Intelligence
- Database Management
- Data Science
- Internet Networks
- Machine Learning
- Statistics
""")

# Experience
section_header("Experience")
st.markdown("""
### Summer Intern
**IIT Guwahati | Jul. 2024 – Aug. 2024**
- Worked under the guidance of a talented team of educators to enhance knowledge of secure coding, system security, and cybersecurity protocols.
- Created, deployed and refined a Streamlit-based Phishing Email Detector using machine learning and NLP, achieving 95%+ detection accuracy on a dataset of 10,000+ emails.

### Contributor in Girlscript Summer of Code
**Girlscript Foundation | May 2024 – Aug. 2024**
- Contributed to diverse projects, collaborating with developers and learning through real-world coding challenges.
- Achieved top 20% ranking among contributors, earning 510 points and 6 badges for contributions.
- Refined understanding of open-source development and honed coding skills.
""")

# Projects
section_header("Projects")
st.markdown("""
### Automated Grading System in Python
**Python, SQL | Apr. 2024**
- Developed a web application to automate the grading process, reducing manual grading time by 70% for teachers.
- Designed the front-end using Streamlit framework in Python to make a simple user interface for teachers and students.
- Implemented the model using PyTorch and BERT architecture, improving grading accuracy by 15% compared to traditional keyword-based methods.
- Used K-means clustering to group 200+ student responses, identifying common themes and improving feedback efficiency.
- Graded student responses with cosine similarity, achieving a grading consistency rate of 90% compared to human evaluations.

### Flexion: Your AI-Powered Fitness Coach
**Python, HTML, CSS, React | Nov. 2024**
- Built an interactive React-based front-end to support real-time posture correction, progress tracking, and adaptive workout recommendations.
- Collaborated on AI integration, leveraging Generative AI (GPT-2) for dynamic workout planning and TensorFlow for pose estimation, achieving 90%+ accuracy in real-time posture recognition.
- Ensured seamless frontend-backend communication via FastAPI, reducing response latency by 30%, and enabling personalized fitness guidance and live feedback.
""")

# Skills
section_header("Technical Skills")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    ### Languages
    Python, Java, C, Dart, SQL

    ### Web
    HTML, CSS, JavaScript, React
    """)
with col2:
    st.markdown("""
    ### ML and Data Science
    TensorFlow, PyTorch, Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn, NLTK, SpaCy, FinBERT, Transformers, OpenCV

    ### UI/UX
    Figma, Tkinter, Streamlit
    """)

# Extracurricular
section_header("Extracurricular Activities")
st.markdown("""
- **Newsletter Editorial Team** - Core Member | Mar. 2024 – Jul. 2024
- **Antarman - The Yoga and Meditation club official** - Social Media Team | Jun. 2024 – Present
- **Career Development Cell** - Creative Team | May 2024 – Present
""")

# Footer
st.markdown('---')
st.markdown('<p class="footer">© 2023 Sanya Behera. All rights reserved.</p>', unsafe_allow_html=True)

