import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Docker Tasks", layout="wide")

# CSS for feature cards and buttons
st.markdown("""
<style>
.view-btn {
    display: inline-block;
    margin-top: 10px;
    width: 100%;
    padding: 0.6em;
    border: none;
    border-radius: 5px;
    background-color: #00B2FF !important;
    color: white !important;
    font-weight: bold;
    text-align: center;
    text-decoration: none;
    cursor: pointer;
}
.view-btn:hover {
    background-color: #0095d9 !important;
}
.feature-card {
    background: linear-gradient(145deg, #2d3748 0%, #4a5568 100%);
    padding: 1.5rem;
    border-radius: 15px;
    border: 1px solid #4a5568;
    margin: 1rem 0;
    transition: transform 0.3s ease;
}
.feature-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)

# Feature Cards
st.markdown("## ------ Docker Tasks--------")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3># Apache Server in Docker</h3>   
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_apacheserver-docker-devops-activity-7348255132142211072-M9sA?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE" 
           target="_blank" class="view-btn">
            View On LinkedIn
        </a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3># Docker in Docker(DinD)</h3>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_vimaldaga-linuxworld-constantefforts-activity-7345048117857218560-QCH3?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE" 
           target="_blank" class="view-btn">
            View On LinkedIn
        </a>
    </div>
    """, unsafe_allow_html=True)


col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3># Run any tool or technology in Docker</h3>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_docker-vlc-guiindocker-activity-7350209251950157824-iwKi?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE" 
           target="_blank" class="view-btn">
            View On LinkedIn
        </a>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
        <h3># run graphical software inside a Docker container</h3>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_docker-vlc-guiindocker-activity-7350209251950157824-iwKi?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE" 
           target="_blank" class="view-btn">
            View On LinkedIn
        </a>
    </div>
    """, unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3># a way to give sound card access to any program inside Docker</h3>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_docker-vlc-guiindocker-activity-7350209251950157824-iwKi?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE" 
           target="_blank" class="view-btn">
            View On LinkedIn
        </a>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
        <h3># a blog on a case study of why Docker is used by different companies</h3>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_docker-mysql-uberengineering-activity-7349342941301088256-9jXs?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE" 
           target="_blank" class="view-btn">
            View On LinkedIn
        </a>
    </div>
    """, unsafe_allow_html=True)
