import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Python tasks", layout="wide")

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
st.markdown("## ------ Python Tasks--------")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3># Send WhatsApp message using Python</h3>      
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_linuxworld-week3wrap-pythonautomation-activity-7347501273870454785-UY1L?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3># Send email using Python</h3>        
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_linuxworld-week3wrap-pythonautomation-activity-7347501273870454785-UY1L?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)


col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3># Make a phone call using Python</h3>     
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_linuxworld-week3wrap-pythonautomation-activity-7347501273870454785-UY1L?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
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
        <h3># Search on Google using Python and get the output</h3>  
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_docker-vlc-guiindocker-activity-7350209251950157824-iwKi?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
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
        <h3># Post on Instagram / X (Twitter) / Facebook using Python</h3>      
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_linuxworld-week3wrap-pythonautomation-activity-7347501273870454785-UY1L?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class="feature-card">
        <h3># Go on a website and download the entire data using Python</h3>    
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_linuxworld-week3wrap-pythonautomation-activity-7347501273870454785-UY1L?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)



col7, col8 = st.columns(2)

with col7:
    st.markdown("""
    <div class="feature-card">
        <h3># Technical difference between Tuple and List</h3>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_pythonlearning-tuplevslist-dailylearning-activity-7352199400791724032-r8_L?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

with col8:
    st.markdown("""
    <div class="feature-card">
        <h3># Create your own digital image using Python</h3>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_vimaldaga-linuxworld-constantefforts-activity-7345048117857218560-QCH3?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

