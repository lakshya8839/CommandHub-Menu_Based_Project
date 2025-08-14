import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Linux Tasks", layout="wide")

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
st.markdown("## ------ Linux Tasks--------")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3># Write a blog post on companies using Linux</h3>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_linux-cloudcomputing-aws-activity-7351879656649773056-2Hiu?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
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
        <h3># Choose 5 GUI programs in Linux and find out the commands working behind them</h3>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_linux-guitocli-opensource-activity-7349081712619896834-7AuX?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
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
        <h3># Find the command working behind the Ctrl+C and Ctrl+Z interrupt signals</h3>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_linux-ctrlc-ctrlz-activity-7351957669328416769-Tfe0?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)
