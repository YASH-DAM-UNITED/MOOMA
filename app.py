import streamlit as st
import time
import streamlit.components.v1 as components

# =========================================================
# SYSTEM CONFIG
# =========================================================
st.set_page_config(
    page_title="MOOMA Portal",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# STATE INITIALIZATION
# =========================================================
if "lang" not in st.session_state: st.session_state.lang = "en"
if "authenticated" not in st.session_state: st.session_state.authenticated = True
if "show_mgmt_password" not in st.session_state: st.session_state.show_mgmt_password = False
if "show_hr_password" not in st.session_state: st.session_state.show_hr_password = False
if "mgmt_lock_until" not in st.session_state: st.session_state.mgmt_lock_until = 0

# Define your texts
texts = {
    "en": {
        "title": "M O O M A",
        "sub": "Operations management <br>just got easier.",
        "desc": "Welcome to the central command unit for MOOMA. Seamlessly organize branch metrics, manage shift requirements, and deploy localized branch parameters.",
        "btn_staff": "Staff Access →",
        "btn_hr": "HR Access →",
        "btn_admin": "Admin Access →"
    },
    "ar": {
        "title": "بـارت",
        "sub": "إدارة العمليات <br>أصبحت أسهل.",
        "desc": "أهلاً بك في وحدة التحكم المركزية لـ MOOMA. قم بتنظيم مقاييس الفروع، وإدارة متطلبات المناوبات، ونشر معايير الفروع بسهولة.",
        "btn_staff": "وصول الموظفين ←",
        "btn_hr": "وصول الموارد البشرية ←",
        "btn_admin": "وصول الإدارة ←"
    }
}

T = texts[st.session_state.lang]

def is_mgmt_locked():
    return time.time() < st.session_state.mgmt_lock_until

# =========================================================
# CSS ARCHITECTURE
# =========================================================
st.markdown("""<style>
/* Global Hidden Elements */
[data-testid="stSidebar"], [data-testid="collapsedControl"] { display: none !important; }
#MainMenu, footer, header { visibility: hidden; }

/* Transparencies */
.stApp, [data-testid="stAppViewContainer"], [data-testid="stMainBlockContainer"] { background: transparent !important; }

/* Desktop Master Styles */
.block-container { max-width: 100% !important; padding: 1rem 5rem !important; }
.mooma-logo { display: inline-block; animation: breathe-bold 2s ease-in-out infinite; background: linear-gradient(90deg, #640D14 0%, #640D14 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 900 !important; letter-spacing: -2px; }
.registered { font-size: 26px; font-weight: 900; color: #640D14 !important; position: relative; top: -39px; left: 8px; display: inline-block; }

/* Background */
.background-layer { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -9999; overflow: hidden; background-color: #F8FAFC; }
.orbit { position: absolute; border: 1px solid rgba(0, 0, 0, 0.2); border-radius: 50%; animation: spin linear infinite; left: 50%; top: 50%; transform: translate(-50%, -50%); }
.o1 { width: 200px; height: 200px; animation-duration: 20s; }
.o2 { width: 350px; height: 350px; animation-duration: 30s; }
.o3 { width: 500px; height: 500px; animation-duration: 40s; }
.o4 { width: 650px; height: 650px; animation-duration: 50s; }
.o5 { width: 800px; height: 800px; animation-duration: 65s; }

/* Cards & Buttons */
.card-glow { position: relative; padding: 2px; background: #FFFFFF; border-radius: 22px; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05); }
.card-content { background: #FFFFFF; border-radius: 20px; padding: 30px; }
div.stButton > button { height: 54px !important; border-radius: 50px !important; border: none !important; background: #640D14 !important; color: #FFFFFF !important; font-weight: 900 !important; text-transform: uppercase !important; letter-spacing: 2px !important; transition: all 0.4s ease !important; }
div.stButton > button:hover { transform: scale(1.05); background: #e3a857 !important; }

/* Keyframes */
@keyframes spin { from { transform: translate(-50%, -50%) rotate(0deg); } to { transform: translate(-50%, -50%) rotate(360deg); } }
@keyframes breathe-bold { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); } }
</style>""", unsafe_allow_html=True)

# =========================================================
# UI RENDER
# =========================================================
st.markdown("<div class='background-layer'><div class='orbit o1'></div><div class='orbit o2'></div><div class='orbit o3'></div><div class='orbit o4'></div><div class='orbit o5'></div></div>", unsafe_allow_html=True)

st.markdown(f"""
<h1 style='text-align: center; font-size: 88px; font-weight: 800; color: #111;'>
    <span class='mooma-logo'>{T['title']}</span><span class="registered">®</span>
</h1>
<h1 style='text-align: center; font-size: 58px; font-weight: 800; color: #111;'>{T['sub']}</h1>
<p style='text-align: center; font-size: 16px; color: #64748B; max-width: 520px; margin: 20px auto 40px auto;'>{T['desc']}</p>
""", unsafe_allow_html=True)

# Cards
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("<div class='card-glow'><div class='card-content' style='text-align:center;'><h3>Staff</h3>", unsafe_allow_html=True)
    if st.button(T['btn_staff'], use_container_width=True): st.switch_page("pages/staff_dashboard.py")
    st.markdown("</div></div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card-glow'><div class='card-content' style='text-align:center;'><h3>HR</h3>", unsafe_allow_html=True)
    if st.button(T['btn_hr'], use_container_width=True):
        st.session_state.show_hr_password = True
        st.rerun()
    st.markdown("</div></div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='card-glow'><div class='card-content' style='text-align:center;'><h3>Admin</h3>", unsafe_allow_html=True)
    if is_mgmt_locked():
        st.button("Locked 🔒", disabled=True, use_container_width=True)
    elif st.button(T['btn_admin'], use_container_width=True):
        st.session_state.show_mgmt_password = True
        st.rerun()
    st.markdown("</div></div>", unsafe_allow_html=True)

# Password Handling
if st.session_state.show_hr_password:
    with st.form("hr_form"):
        pwd = st.text_input("Password", type="password")
        if st.form_submit_button("Submit"):
            if pwd == st.secrets["HR_PASSWORD"]: st.switch_page("pages/staff_schedule.py")
            else: st.error("Invalid")

if st.session_state.show_mgmt_password:
    with st.form("admin_form"):
        pwd = st.text_input("Password", type="password")
        if st.form_submit_button("Submit"):
            if pwd == st.secrets["MANAGER_PASSWORD"]: st.switch_page("pages/management_dashboard.py")
            else: st.error("Invalid")
