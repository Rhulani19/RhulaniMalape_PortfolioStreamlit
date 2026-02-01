import streamlit as st

def render_navigation():
    st.write("### 🔗 Navigation")
    cols = st.columns(5)

    with cols[0]:
        if st.button("About"):
            st.markdown('<a id="about"></a>', unsafe_allow_html=True)

    with cols[1]:
        if st.button("Research"):
            st.markdown('<a id="research"></a>', unsafe_allow_html=True)

    with cols[2]:
        if st.button("Skills"):
            st.markdown('<a id="skills"></a>', unsafe_allow_html=True)

    with cols[3]:
        if st.button("Projects"):
            st.markdown('<a id="projects"></a>', unsafe_allow_html=True)

    with cols[4]:
        if st.button("Contact"):
            st.markdown('<a id="contact"></a>', unsafe_allow_html=True)

    st.markdown("---")
