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

# Sidebar
st.sidebar.title("🚀 CommandHub")
st.sidebar.markdown("---")

# Navigation
pages = {
    "🏠 Dashboard": "app.py",
    "💻 Commands": "pages/All_Commands.py",
    "🐳 Docker Commands": "pages/All_Commands.py", 
    "🤖 AI Agents": "pages/Ai_agent_streamlit.py",
    "✨ Javascript Tasks": "pages/Javascript_tasks.py",
    "💬 Chatbot": "pages/Chatbot.py",
    "🧠 ML Projects": "pages/streamlit_titanic_model.py"
}

st.sidebar.markdown("### Navigation")
for page_name, page_file in pages.items():
    if st.sidebar.button(page_name, key=page_name, use_container_width=True):
        if page_name != "🏠 Dashboard":
            st.switch_page(page_file)

st.sidebar.markdown("---")

# Main Dashboard
st.markdown("""
<div class="main-header" >
    <h1>------- Welcome to CommandHub --------</h1>
    <p>All Projects at one place (developed by Lakshya Chalana)</p>
    <p><strong>Execute • Manage • Deploy • Analyze</strong></p>
</div>
""", unsafe_allow_html=True)

st.image("assets/flutter.png", use_container_width=True)


st.markdown("---")

# Feature Cards
st.markdown("## ------ ALL Projects And Tasks--------")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3># Command Launcher</h3>
        <p>Unified interface to run and monitor commands across Linux, Windows and Docker with execution logs and history for repeatable workflows.</p>
        <ul>
            <li>Multi-platform command execution (Linux / Windows / Docker)</li>
            <li>Real-time output streaming and logs</li>
            <li>Command history and repeatable workflows</li>
            <li>SSH remote execution support</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("-> Launch Commands", key="cmd_btn", use_container_width=True):
        st.switch_page("pages/All_Commands.py")

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3># Docker Commands</h3>
        <p>Handy Docker CLI examples and recipes to build, run, inspect and troubleshoot containerized applications.</p>
        <ul>
            <li>Container lifecycle (run, stop, rm)</li>
            <li>Image build and optimization tips</li>
            <li>Volume and network configuration examples</li>
            <li>Log inspection and debugging commands</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("-> Run Docker Commands", key="docker_btn", use_container_width=True):
        st.switch_page("pages/All_Commands.py")

col21, col22 = st.columns(2)

with col21:
    st.markdown("""
    <div class="feature-card">
        <h3># Aws Tasks</h3>
        <p>Practical AWS CLI snippets and automation samples for common cloud operations and resource management.</p>
        <ul>
            <li>EC2 instance lifecycle and management</li>
            <li>S3 bucket and object operations</li>
            <li>IAM users, roles and policy handling</li>
            <li>Automation scripts for routine tasks</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("-> View Tasks", key="aws_btn", use_container_width=True):
        st.switch_page("pages/AWS_tasks.py")

with col22:
    st.markdown("""
    <div class="feature-card">
        <h3># Docker tasks</h3>
        <p>Project-focused Docker task examples: Dockerfile patterns, multi-stage builds, and deployment workflows.</p>
        <ul>
            <li>Dockerfile best practices and multi-stage builds</li>
            <li>CI/CD friendly image build pipelines</li>
            <li>Deployment and orchestration examples</li>
            <li>Registry push/pull and versioning tips</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("-> view tasks", key="docker2_btn", use_container_width=True):
        st.switch_page("pages/Docker_tasks.py")

col23, col24 = st.columns(2)

with col23:
    st.markdown("""
    <div class="feature-card">
        <h3># Jenkins Tasks</h3>
        <p>CI/CD pipeline snippets and Jenkins job configurations for automated building, testing and deployment.</p>
        <ul>
            <li>Pipeline-as-code examples (Jenkinsfile)</li>
            <li>Job templates for build and test stages</li>
            <li>Integration with Git, Docker and artifact stores</li>
            <li>Notification and reporting hooks</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("-> View Tasks", key="jenkins_btn", use_container_width=True):
        st.switch_page("pages/Jenkins_tasks.py")

with col24:
    st.markdown("""
    <div class="feature-card">
        <h3># Kubernetes tasks</h3>
        <p>kubectl commands and manifest examples to deploy, scale and troubleshoot workloads in Kubernetes clusters.</p>
        <ul>
            <li>Pod, Deployment and Service management</li>
            <li>Namespace and RBAC practices</li>
            <li>Autoscaling and resource tuning</li>
            <li>Debugging tools and log aggregation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("-> view tasks", key="k8s_btn", use_container_width=True):
        st.switch_page("pages/Kubernetes_tasks.py")

col25, col26 = st.columns(2)

with col25:
    st.markdown("""
    <div class="feature-card">
        <h3># Linux Tasks</h3>
        <p>Collection of essential Linux commands and admin workflows for file management, services, and troubleshooting.</p>
        <ul>
            <li>File and directory operations</li>
            <li>Permissions, users and groups</li>
            <li>Process and service monitoring</li>
            <li>Networking commands and diagnostics</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("-> View Tasks", key="linux_btn", use_container_width=True):
        st.switch_page("pages/Linux_tasks.py")

with col26:
    st.markdown("""
    <div class="feature-card">
        <h3># Python tasks</h3>
        <p>Reusable Python scripts and small utilities for automation, data handling and backend helpers.</p>
        <ul>
            <li>Script templates and CLI utilities</li>
            <li>Virtualenv/venv and packaging notes</li>
            <li>API integration and scraping examples</li>
            <li>Testing and debugging snippets</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("-> view tasks", key="python_btn", use_container_width=True):
        st.switch_page("pages/python_tasks.py")

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3># AI Agents</h3>
        <p>Multi-agent interfaces demonstrating task automation, tool use and model orchestration for practical problems.</p>
        <ul>
            <li>Task-specific agent implementations</li>
            <li>Tool and API integration</li>
            <li>Agent coordination and routing</li>
            <li>Interactive Streamlit frontends</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("# Try AI Agents", key="ai_btn", use_container_width=True):
        st.switch_page("pages/Ai_agent_streamlit.py")

with col4:
    st.markdown("""
    <div class="feature-card">
        <h3># Javascript tasks</h3>
        <p>Small JavaScript utilities and examples for DOM interaction, API calls, and frontend feature experiments.</p>
        <ul>
            <li>DOM manipulation & event handling</li>
            <li>Fetch/axios API call patterns</li>
            <li>Small UI widgets and interaction patterns</li>
            <li>Debugging and performance tips</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("-> view tasks", key="prompt_btn", use_container_width=True):
        st.switch_page("pages/Javascript_tasks.py")

col5, col6 = st.columns(2)

with col5:
    st.markdown("""
    <div class="feature-card">
        <h3># AI Chatbot</h3>
        <p>Conversational assistant prototypes built for Q&A, task help and lightweight workflow automation.</p>
        <ul>
            <li>Natural language understanding and responses</li>
            <li>Context-aware conversation memory</li>
            <li>Multiple model integrations</li>
            <li>Conversation export and logging</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button(" Start Chatting", key="chat_btn", use_container_width=True):
        st.switch_page("pages/Chatbot.py")

with col6:
    st.markdown("""
    <div class="feature-card">
        <h3># ML Projects</h3>
        <p>Interactive machine learning demos covering data preparation, model training and evaluation with visual insights.</p>
        <ul>
            <li>Data preprocessing pipelines</li>
            <li>Model training and validation</li>
            <li>Feature importance and explainability</li>
            <li>Interactive prediction demos</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button(" Explore ML", key="ml_btn", use_container_width=True):
        st.switch_page("pages/streamlit_titanic_model.py")

col7, col8 = st.columns(2)

with col7:
    st.markdown("""
    <div class="feature-card">
        <h3># DevOps Project 1</h3>
        <p>CI/CD from Scratch: end-to-end example integrating a Flask app with Jenkins and Docker for automated delivery.</p>
        <ul>
            <li>Flask application source and structure</li>
            <li>Jenkins pipeline (Jenkinsfile) examples</li>
            <li>Docker image build and registry steps</li>
            <li>Deployment and automation flow</li>
        </ul>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_devops-ciabrcd-jenkins-activity-7348006497106173954-wnHa?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE" target="_blank">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
        <a href="https://github.com/lakshya8839/Devops_Project_1">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Github
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

with col8:
    st.markdown("""
    <div class="feature-card">
        <h3># DevOps Project 2</h3>
        <p>Kubernetes and cloud-native patterns demonstrating orchestration, scaling and deployment best practices.</p>
        <ul>
            <li>Cluster deployment and configuration</li>
            <li>Helm/manifest examples</li>
            <li>Autoscaling and resource management</li>
            <li>CI/CD integration with clusters</li>
        </ul>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_devops-kubernetes-jenkins-activity-7352753287558803456-lDP0?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
        <a href="https://github.com/lakshya8839/kubernetes_project_1">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Github
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

col9, col10 = st.columns(2)

with col9:
    st.markdown("""
    <div class="feature-card">
        <h3># Microservices Architecture Project(Cache Memory)</h3>
        <p>Design and implementation of microservices with Redis cache and PostgreSQL persistence for scalable architectures.</p>
        <ul>
            <li>Service decomposition and APIs</li>
            <li>Caching strategies using Redis</li>
            <li>Database design and migrations (Postgres)</li>
            <li>Inter-service communication patterns</li>
        </ul>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_microservicesarchitecture-redis-postgresql-activity-7352934887210864641-hegf?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

with col10:
    st.markdown("""
    <div class="feature-card">
        <h3># DevOps Project 3</h3>
        <p>Advanced deployment examples covering autoscaling, resilience patterns and rollout strategies for production systems.</p>
        <ul>
            <li>Autoscaling configuration and policies</li>
            <li>Blue/green and rolling update strategies</li>
            <li>Health checks and readiness probes</li>
            <li>Monitoring and rollback procedures</li>
        </ul>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_lakshyachalana-kubernetes-autoscaling-activity-7355303283256647680-nI0V?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

col11, col12 = st.columns(2)

with col11:
    st.markdown("""
    <div class="feature-card">
        <h3># Streamlit Based Project(Event-ticket Booking App)</h3>
        <p>Streamlit demo for event discovery and ticket booking with simple flows for search, selection and order simulation.</p>
        <ul>
            <li>Event search and listing UI</li>
            <li>Ticket selection and booking workflow</li>
            <li>Order summary and mock payment flow</li>
            <li>Admin view for event management</li>
        </ul>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_streamlit-pythonproject-internshiplearning-activity-7341824533571506176-t82V?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

with col12:
    st.markdown("""
    <div class="feature-card">
        <h3># Gemini Expert Advisor(Gradio project)</h3>
        <p>Gradio interface showcasing prompt experiments and assistant behaviour tuning with the Gemini model family.</p>
        <ul>
            <li>Prompt templates and variations</li>
            <li>Interactive model comparison</li>
            <li>Session export and example prompts</li>
            <li>Use-case driven advisor demos</li>
        </ul>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_genai-gemini-gradio-activity-7345145243517800448-rQHZ?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

col13, col14 = st.columns(2)

with col13:
    st.markdown("""
    <div class="feature-card">
        <h3># Apache Server inside Docker</h3>
        <p>Containerized Apache HTTP server examples with custom virtual hosts, static site hosting and basic performance tips.</p>
        <ul>
            <li>Dockerized Apache setup and configuration</li>
            <li>Virtual host and site serving configuration</li>
            <li>Serving static assets and error handling</li>
            <li>Image size and performance considerations</li>
        </ul>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_apacheserver-docker-devops-activity-7348255132142211072-M9sA?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

with col14:
    st.markdown("""
    <div class="feature-card">
        <h3># Portfolio - Lakshya Chalana</h3>
        <p>Personal portfolio showcasing projects, skills, experience, and contact links in a modern layout.</p>
        <ul>
            <li>Projects catalogue with demos and repos</li>
            <li>Skills, certifications and experience highlights</li>
            <li>Responsive, dark-themed design elements</li>
            <li>Contact and social integration</li>
        </ul>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_lakshya-chalana-portfolio-activity-7348750625595105280-js4s?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
        <a href="https://lakshya-chalana-portfolio.netlify.app/">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 Visit Portfolio
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

col15, col16 = st.columns(2)

with col15:
    st.markdown("""
    <div class="feature-card">
        <h3># Agentic AI Usecase Project</h3>
        <p>Prototype agentic workflows that chain reasoning and tool usage to complete multi-step tasks end-to-end.</p>
        <ul>
            <li>Planning and action-selection pipelines</li>
            <li>Tool integration and execution monitoring</li>
            <li>Result validation and feedback loops</li>
            <li>Concrete use-case demonstrations</li>
        </ul>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_agenticai-genaiops-solana-activity-7349836475871469568-SuaX?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

with col16:
    st.markdown("""
    <div class="feature-card">
        <h3># Medicine info Chatbot(Web Scrapping Based Project)</h3>
        <p>Chatbot that aggregates verified medicine references via web scraping to answer basic queries with source attribution.</p>
        <ul>
            <li>Web scraping and data cleaning pipelines</li>
            <li>Question-answering over scraped content</li>
            <li>Source attribution and safety notes</li>
            <li>Search and quick-reference UI</li>
        </ul>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_genai-geminiapi-webscraping-activity-7350052616640356352-igLw?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

col17, col18 = st.columns(2)

with col17:
    st.markdown("""
    <div class="feature-card">
        <h3># Adding AI in Portfolio (Chatbot-project)</h3>
        <p>Pattern and integration guide for embedding a chat assistant into a portfolio site to showcase interactive demos.</p>
        <ul>
            <li>Embed chat UI with minimal footprint</li>
            <li>Session persistence and context handling</li>
            <li>Demo mode vs production mode considerations</li>
            <li>Authentication and privacy considerations</li>
        </ul>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_lakshyachalana-portfolioupdate-genai-activity-7351849919999102976-DMRb?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

with col18:
    st.markdown("""
    <div class="feature-card">
        <h3># Computer Vision Project(OpenCV Project)</h3>
        <p>Computer vision demos using OpenCV/MediaPipe for detection, tracking, and applied filters with real-time feedback.</p>
        <ul>
            <li>Object and face detection examples</li>
            <li>Pose tracking and overlays</li>
            <li>Real-time video processing tips</li>
            <li>Integration with ML models and pipelines</li>
        </ul>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_lakshyachalana-opencv-mediapipe-activity-7355280717305536513-JRVD?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

col19, col20 = st.columns(2)

with col19:
    st.markdown("""
    <div class="feature-card">
        <h3># Telegram Bot(Project)</h3>
        <p>Examples of Telegram bots for automations, message handling and simple workflows with webhook or polling setups.</p>
        <ul>
            <li>Command and message handler patterns</li>
            <li>Webhook vs polling deployment guides</li>
            <li>Notification and templating examples</li>
            <li>Error handling and rate-limiting tips</li>
        </ul>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_lakshyachalana-week6wrapped-linuxworldinternship-activity-7355432156875145216--gXu?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

with col20:
    st.markdown("""
    <div class="feature-card">
        <h3># Adding AI in Portfolio (Chatbot-project)</h3>
        <p>Alternate example and walkthrough for integrating a chatbot into a portfolio, focusing on UX and demo polish.</p>
        <ul>
            <li>UX-first chat embedding strategies</li>
            <li>Fallbacks and offline/demo behavior</li>
            <li>Styling to match portfolio themes</li>
            <li>Privacy and consent notices for demos</li>
        </ul>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_lakshyachalana-portfolioupdate-genai-activity-7351849919999102976-DMRb?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

col21, col22 = st.columns(2)

with col21:
    st.markdown("""
    <div class="feature-card">
        <h3># Backup Project(Company daily-usecase Project)</h3>
        <p>Company-oriented backup and automation tools designed for daily maintenance, log rotation and reliable restores.</p>
        <ul>
            <li>Scheduled backup scripts and cron jobs</li>
            <li>Restore and verification procedures</li>
            <li>Logging, alerting and monitoring</li>
            <li>Storage lifecycle and retention strategies</li>
        </ul>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_python-flask-automation-activity-7355805370142900225-vwmx?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

with col22:
    st.markdown("""
    <div class="feature-card">
        <h3># FireBase Project</h3>
        <p>Firebase authentication and backend examples for rapid prototyping of web/mobile features and auth flows.</p>
        <ul>
            <li>Email/password and social authentication patterns</li>
            <li>Realtime Database / Firestore usage examples</li>
            <li>Security rules and best practices</li>
            <li>Hosting and Cloud Functions scaffolding</li>
        </ul>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_firebase-authentication-passwordhashing-activity-7355878542368280576-nJ6S?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

col27, col28 = st.columns(2)
with col27:
    st.markdown("""
    <div class="feature-card">
        <h3># Apno ki Awaj (Jazbaa 4.O Project)</h3>
        <p>Product Portfolio Designed for the purpose of our Startup.</p>
        <ul>
            <li>Designed to showcase demo</li>
            <li>As per our prototype</li>
            <li>Will grow it as per our learnings</li>
            <li>Contact and social integration</li>
        </ul>
        <a href="https://www.linkedin.com/posts/lakshya-chalana-886306285_lakshyachalana-palaksaini-productportfolio-activity-7358524198371143680-UMJQ?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEVHYWYBuyhNONblNN_cYP0KU9JSzwHJAjE">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 View On Linkedin
            </button>
        </a>
        <a href="https://apnokiawaj.netlify.app/">
            <button style='margin-top: 10px; width: 100%; padding: 0.5em; border: none; border-radius: 5px;
                           background-color: #00B2FF; color: white; font-weight: bold; cursor: pointer;'>
                 Visit Portfolio
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #718096;">
    <p>Menu Based Project-Lakshya Chalana</P>
</div>
""", unsafe_allow_html=True)
