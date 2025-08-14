import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Kubernetes Tasks", layout="wide")

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
st.markdown("## ------ Jenkins Tasks--------")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3># Create a blog or case study on how companies are using Jenkins and what benefits they are getting</h3>   
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_apacheserver-docker-devops-activity-7348255132142211072-M9sA?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE" 
           target="_blank" class="view-btn">
            View On LinkedIn
        </a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3># Create a job to install Docker and automatically launch the container</h3>
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
        <h3># Launch Kubernetes pods and expose them using Jenkins</h3>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_docker-vlc-guiindocker-activity-7350209251950157824-iwKi?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE" 
           target="_blank" class="view-btn">
            View On LinkedIn
        </a>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
        <h3># Set up a multi-node Kubernetes cluster automatically with Jenkins</h3>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_docker-vlc-guiindocker-activity-7350209251950157824-iwKi?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE" 
           target="_blank" class="view-btn">
            View On LinkedIn
        </a>
    </div>
    """, unsafe_allow_html=True)

