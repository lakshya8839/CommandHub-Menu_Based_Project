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

# Header
st.markdown("## ------ Kubernetes Tasks --------")

# Task cards
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3># Create a blog on case studies of why companies use Kubernetes and the benefits they get</h3>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_pinterest-kubernetes-docker-activity-7347302854144991232-pYtH?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE" 
           target="_blank" class="view-btn">
            View On LinkedIn
        </a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3># Run the same code in your environment and try to launch more use cases of multi-tier websites</h3>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_microservicesarchitecture-redis-postgresql-activity-7352934887210864641-hegf?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE" 
           target="_blank" class="view-btn">
            View On LinkedIn
        </a>
    </div>
    """, unsafe_allow_html=True)
