import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Researcher Profile | Rhulani Malape",
    page_icon="🎓",
    layout="wide"
)

# ---------------- NAVIGATION ----------------
def render_navigation():
    st.markdown(
        """
        <style>
        .nav {
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .nav a {
            color: #16A085;
            margin: 0 15px;
            text-decoration: none;
            transition: color 0.3s ease;
        }
        .nav a:hover {
            color: #2C3E50;
        }
        </style>
        <div class="nav">
            <a href="#about">About</a> |
            <a href="#research">Research</a> |
            <a href="#skills">Skills</a> |
            <a href="#projects">Projects</a> |
            <a href="#contact">Contact</a>
        </div>
        """,
        unsafe_allow_html=True
    )

render_navigation()

# ---------------- HERO SECTION ----------------
col1, col2 = st.columns([1, 3])

with col1:
    st.image("Ruske.jpeg", width=220)

with col2:
    st.markdown(
        """
        <h1 style='font-size: 42px; color: #2C3E50;'>🎓 Rhulani Malape</h1>
        <h3 style='color: #16A085;'>ICT Graduate | Aspiring Researcher & Software Developer</h3>
        <p style='font-size: 18px; color: #555;'>
        Bachelor of Information and Communication Technology (BICT) | University of Mpumalanga
        </p>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# ---------------- ABOUT ----------------
st.markdown('<a id="about"></a>', unsafe_allow_html=True)
st.header("👤 About Me")
st.write(
    """
I am an ICT graduate with a strong interest in research, software development, and data-driven
solutions. My academic journey has equipped me with a solid foundation in programming,
information systems, and problem-solving.

I am highly motivated, eager to learn, and committed to continuous improvement. I thrive in
collaborative environments and enjoy working on innovative solutions that address real-world challenges.
"""
)

# ---------------- RESEARCH INTERESTS ----------------
st.markdown('<a id="research"></a>', unsafe_allow_html=True)
st.header("🔬 Research Interests")
st.markdown(
    """
- Software Engineering and Web-Based Systems  
- Data Analysis and Information Systems  
- Artificial Intelligence and Emerging Technologies  
- ICT for Education and Socio-Economic Development  
"""
)
# ---------------- SKILLS ----------------
st.markdown('<a id="skills"></a>', unsafe_allow_html=True)
st.header("💡 Technical Skills")

skill_html = """
<style>
.skill-container {
  width: 80%;
  margin: 15px 0;
}
.skill-label {
  font-weight: bold;
  margin-bottom: 5px;
  color: #2C3E50;
}
.skill-bar {
  width: 100%;
  background-color: #eee;
  border-radius: 20px;
  overflow: hidden;
}
.skill-fill {
  height: 24px;
  width: 0;
  background: linear-gradient(90deg, #16A085, #1abc9c);
  text-align: right;
  padding-right: 10px;
  color: white;
  font-weight: bold;
  line-height: 24px;
  border-radius: 20px;
  animation: fillAnimation 2s forwards;
}
.skill-fill:hover {
  background: linear-gradient(90deg, #1abc9c, #16A085);
}

@keyframes fillAnimation {
  from { width: 0; }
  to { width: var(--level); }
}
</style>

<div class="skill-container">
  <div class="skill-label">Python</div>
  <div class="skill-bar">
    <div class="skill-fill" style="--level:70%;">70%</div>
  </div>
</div>

<div class="skill-container">
  <div class="skill-label">Java</div>
  <div class="skill-bar">
    <div class="skill-fill" style="--level:65%;">65%</div>
  </div>
</div>

<div class="skill-container">
  <div class="skill-label">JavaScript</div>
  <div class="skill-bar">
    <div class="skill-fill" style="--level:60%;">60%</div>
  </div>
</div>

<div class="skill-container">
  <div class="skill-label">SQL</div>
  <div class="skill-bar">
    <div class="skill-fill" style="--level:65%;">65%</div>
  </div>
</div>

<div class="skill-container">
  <div class="skill-label">Streamlit</div>
  <div class="skill-bar">
    <div class="skill-fill" style="--level:75%;">75%</div>
  </div>
</div>

<div class="skill-container">
  <div class="skill-label">JSF / PrimeFaces</div>
  <div class="skill-bar">
    <div class="skill-fill" style="--level:60%;">60%</div>
  </div>
</div>
"""

st.markdown(skill_html, unsafe_allow_html=True)

# ---------------- TOOLS ----------------
st.subheader("🧰 Tools & Technologies")
st.markdown(
    """
- Git & GitHub  
- SQLite & MySQL  
- Streamlit Cloud  
- Visual Studio Code  
- Linux & Windows  
"""
)

# ---------------- PROJECTS ----------------
st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
st.header("🛠️ Projects & Academic Work")
st.markdown(
    """
**📌 Student Registration System**  
JSF-based web application with dynamic forms, validations, and database integration.

**📌 Data Processing Pipeline**  
ETL pipeline using Python and SQLite for structured data storage and analysis.

**📌 Streamlit Dashboards**  
Interactive dashboards for data visualization and reporting.

**📌 Group Research Project (BICT321)**  
Corporate dataset analysis focusing on insights and decision support.
"""
)

# ---------------- PUBLICATIONS ----------------
st.header("📚 Research & Publications")
st.info(
    """
Currently developing academic research skills.  
Future publications will focus on ICT systems, data analytics, and applied computing research.
"""
)

# ---------------- ACHIEVEMENTS ----------------
st.header("🏆 Achievements & Activities")
st.markdown(
    """
- Participant in **AI Hackathon Bootcamp** – University of Mpumalanga  
- Group award recipient for innovation and teamwork  
- **Student Mentor** providing academic support and guidance  
"""
)

# ---------------- CV DOWNLOAD ----------------
st.header("📄 Curriculum Vitae")
st.write("You can download my full CV below:")
with open("RhulaniMalapeResume2026.pdf", "rb") as file:
    st.download_button(
        label="📥 Download My CV",
        data=file,
        file_name="RhulaniMalapeResume2026.pdf",
        mime="application/pdf"
    )

# ---------------- CONTACT ----------------
st.markdown('<a id="contact"></a>', unsafe_allow_html=True)
st.header("📫 Contact Information")
st.markdown(
    """
- 📧 [Email](mailto:rhulaneruske203@gmail.com)  
- 💻 [GitHub](https://github.com/Rhulani19)  
- 🔗 [LinkedIn](https://linkedin.com/in/rhulani-malape-882086393)  
"""
)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<center style='color:#888;'>© 2026 | Researcher Profile • Built with Streamlit Cloud</center>",
    unsafe_allow_html=True
)
