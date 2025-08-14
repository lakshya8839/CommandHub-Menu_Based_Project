import streamlit as st
import json
import streamlit.components.v1 as components
from pathlib import Path

# Page config
st.set_page_config(
    page_title="CommandHub - Multi-Platform Interface",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
def load_css():
    css_file = Path("assets/styles.css")
    if css_file.exists():
        with open(css_file) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    else:
        # Fallback CSS
        st.markdown("""
        <style>
        .main-header {
           background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
   	   padding: 2rem;
    	   border-radius: 10px;
    	   margin-bottom: 2rem;
    	   text-align: center;
    	   color: white;
    	   display: flex;
    	   flex-direction: column;
    	   align-items: center;
    	   justify-content: center;
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
        .metric-card {
            background: linear-gradient(145deg, #1a202c 0%, #2d3748 100%);
            padding: 1rem;
            border-radius: 10px;
            text-align: center;
            border: 1px solid #4a5568;
        }
        .stButton > button {
            background: linear-gradient(145deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.5rem 1rem;
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }
        </style>
        """, unsafe_allow_html=True)

load_css()


# Feature Cards
st.markdown("## ------ AWS Tasks--------")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3># a blog on the AWS user case studies</h3>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_generativeai-adobefirefly-aws-activity-7348980563728359424-cZYW?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
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
        <h3># With the help of Boto3, launch and terminate EC2 instance</h3>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_cloudops-cloudcomputing-pythonautomation-activity-7349493851738296320-XS4s?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
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
        <h3># event-driven architecture</h3>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_aws-eventdrivenarchitecture-s3-activity-7353468381674512385-SLRm?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
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
        <h3># Connect Python to MongoDB service of AWS using Lambda</h3>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_reactjs-microservices-eda-activity-7351646233880375296-kU6d?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
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
        <h3># Find a way to upload an object to an S3 bucket without logging into AWS</h3>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_aws-eventdrivenarchitecture-s3-activity-7353468381674512385-SLRm?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)


