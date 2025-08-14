import streamlit as st
from pathlib import Path

st.set_page_config(page_title="ML Tasks", layout="wide")

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
st.markdown("## ------ ML Projects--------")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3> Titanic Model(Ml-Project)</h3>
        
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("-> view project", key="cmd_btn", use_container_width=True):
        st.switch_page("pages/streamlit_titanic_model.py")

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3> Salary Prediction(Ml-Project)</h3>
        
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("-> View Project", key="docker_btn", use_container_width=True):
        st.switch_page("pages/streamlit_salary_predict.py")

st.markdown("## ------ ML Projects--------")

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3> Find different techniques of data imputation</h3>     
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_linuxworld-internshipexperience-day10-activity-7344047721441333249-FLtq?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
        <h3> Find what happens to the weight of dropped category in categorical variable</h3>      
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_linuxworld-internshipexperience-day10-activity-7344047721441333249-FLtq?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

col5, col6 = st.columns(2)

with col5:
    st.markdown("""
    <div class="feature-card">
        <h3>Find an LLM model, try to find its API and find out its internal structure like layers, neurons, activation functions. Try to create your own LLM model</h3>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_genai-geminiapi-webscraping-activity-7350052616640356352-igLw?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

