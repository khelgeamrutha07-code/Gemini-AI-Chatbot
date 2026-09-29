import streamlit as st
from dotenv import load_dotenv
import os
from google import genai
load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_key)
st.set_page_config(
    page_title="Gemini AI Chatbot",
    layout="centered",
)
st.title("Gemini AI Chatbot")
st.write("Ask Gemini anything")
prompt=st.text_area(
    "Enter your prompt:",
    placeholder="Explain Artificial Intelligence"
)
if st.button("Generate Response"):
    if prompt:
        with st.spinner("Gemini is thinkiing..."):
            response=client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )
        st.success("Response generated!")
        st.write(response.text)
    else:
        st.warning("please enter a prompt.")


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap');

/* ============ BACKGROUND: animated aurora ============ */
.stApp {
    background: #05050f;
    font-family: 'Inter', sans-serif;
    color: #e8e8f5;
    overflow-x: hidden;
}
.stApp::before, .stApp::after {
    content: "";
    position: fixed;
    border-radius: 50%;
    filter: blur(110px);
    z-index: 0;
    pointer-events: none;
}
.stApp::before {
    width: 620px; height: 620px;
    background: radial-gradient(circle, #7c3aed, #4f46e5 60%, transparent 70%);
    top: -180px; left: -160px;
    opacity: .55;
    animation: drift1 16s ease-in-out infinite alternate;
}
.stApp::after {
    width: 560px; height: 560px;
    background: radial-gradient(circle, #ec4899, #f97316 60%, transparent 70%);
    bottom: -200px; right: -160px;
    opacity: .40;
    animation: drift2 19s ease-in-out infinite alternate;
}
@keyframes drift1 { to { transform: translate(180px, 120px) scale(1.2); } }
@keyframes drift2 { to { transform: translate(-160px, -100px) scale(1.15); } }

[data-testid="stHeader"] { background: transparent; }
footer, #MainMenu { visibility: hidden; }

/* ============ MAIN GLASS CARD ============ */
.block-container {
    position: relative;
    z-index: 1;
    max-width: 800px;
    margin-top: 3rem;
    padding: 3rem 2.8rem 3rem 2.8rem !important;
    border-radius: 32px;
    background: linear-gradient(145deg, rgba(255,255,255,0.10), rgba(255,255,255,0.03));
    border: 1px solid rgba(255,255,255,0.14);
    backdrop-filter: blur(28px) saturate(160%);
    -webkit-backdrop-filter: blur(28px) saturate(160%);
    box-shadow:
        0 30px 80px rgba(0,0,0,0.55),
        inset 0 1px 0 rgba(255,255,255,0.18);
    animation: rise .9s cubic-bezier(.2,.8,.2,1) both;
}
@keyframes rise {
    from { opacity: 0; transform: translateY(30px) scale(.98); }
    to   { opacity: 1; transform: none; }
}

/* ============ TITLE ============ */
h1 {
    font-family: 'Space Grotesk', sans-serif !important;
    text-align: center;
    font-size: 3.2rem !important;
    font-weight: 700 !important;
    letter-spacing: -0.03em;
    padding-bottom: .2rem !important;
    background: linear-gradient(110deg, #ffffff 0%, #c4b5fd 30%, #f9a8d4 55%, #fdba74 75%, #ffffff 100%);
    background-size: 250% auto;
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shimmer 6s linear infinite;
    filter: drop-shadow(0 0 22px rgba(196,181,253,0.35));
}
@keyframes shimmer { to { background-position: 250% center; } }

/* Subtitle */
.stApp .block-container [data-testid="stMarkdownContainer"] p {
    line-height: 1.75;
    font-size: 1.04rem;
}
.stApp .block-container > div > div > div > div:nth-child(2) [data-testid="stMarkdownContainer"] p {
    text-align: center;
    color: #a1a1c2;
    font-size: 1.12rem;
    margin-bottom: 1.6rem;
}

/* ============ TEXT AREA ============ */
.stTextArea label p {
    font-family: 'Space Grotesk', sans-serif;
    color: #ddd6fe !important;
    font-weight: 600;
    font-size: .95rem;
    letter-spacing: .02em;
}
.stTextArea [data-baseweb="textarea"],
.stTextArea [data-baseweb="base-input"] {
    background: transparent !important;
    border: none !important;
    border-radius: 20px !important;
}
.stTextArea textarea {
    background: rgba(8,8,25,0.55) !important;
    color: #fff !important;
    border: 1px solid rgba(255,255,255,0.14) !important;
    border-radius: 20px !important;
    padding: 20px 22px !important;
    min-height: 160px;
    font-size: 1.05rem;
    line-height: 1.65;
    box-shadow: inset 0 2px 12px rgba(0,0,0,0.4);
    transition: all .3s ease;
}
.stTextArea textarea::placeholder { color: #6b6b8f; }
.stTextArea textarea:focus {
    border-color: #a78bfa !important;
    background: rgba(12,12,35,0.7) !important;
    box-shadow:
        0 0 0 4px rgba(167,139,250,0.20),
        0 0 45px rgba(139,92,246,0.35),
        inset 0 2px 12px rgba(0,0,0,0.4) !important;
}

/* ============ BUTTON ============ */
.stButton > button {
    position: relative;
    overflow: hidden;
    width: 100%;
    margin-top: .6rem;
    border: none;
    border-radius: 18px;
    padding: 1rem 1.4rem;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    letter-spacing: .03em;
    color: #fff;
    background: linear-gradient(100deg, #6366f1, #a855f7, #ec4899, #f97316);
    background-size: 250% auto;
    box-shadow:
        0 14px 40px rgba(168,85,247,0.45),
        inset 0 1px 0 rgba(255,255,255,0.35);
    transition: all .4s ease;
}
.stButton > button::after {
    content: "";
    position: absolute;
    top: 0; left: -80%;
    width: 50%; height: 100%;
    background: linear-gradient(120deg, transparent, rgba(255,255,255,0.45), transparent);
    transform: skewX(-20deg);
    transition: left .7s ease;
}
.stButton > button:hover {
    background-position: right center;
    transform: translateY(-4px) scale(1.01);
    box-shadow: 0 20px 55px rgba(236,72,153,0.55), inset 0 1px 0 rgba(255,255,255,0.4);
    color: #fff;
}
.stButton > button:hover::after { left: 130%; }
.stButton > button:active { transform: translateY(0) scale(.98); }
.stButton > button:focus:not(:active) {
    color: #fff;
    border: none;
    box-shadow: 0 0 0 4px rgba(168,85,247,0.4), 0 14px 40px rgba(168,85,247,0.45);
}

/* ============ ALERTS ============ */
[data-testid="stAlert"] {
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.14);
    backdrop-filter: blur(14px);
    margin-top: 1.2rem;
    animation: rise .5s ease both;
}

/* ============ RESPONSE TEXT ============ */
.stMarkdown strong { color: #fff; }
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
    font-family: 'Space Grotesk', sans-serif;
    color: #fff;
    -webkit-text-fill-color: #fff;
    background: none;
    animation: none;
    filter: none;
    font-size: 1.35rem !important;
    text-align: left;
    letter-spacing: -0.01em;
}
.stMarkdown code {
    background: rgba(255,255,255,0.10);
    color: #f9a8d4;
    padding: 2px 8px;
    border-radius: 8px;
}
.stMarkdown pre {
    background: #07071a !important;
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 16px;
}
.stMarkdown a { color: #c4b5fd; }

/* ============ SPINNER + SCROLLBAR ============ */
.stSpinner > div { color: #c4b5fd; }
::-webkit-scrollbar { width: 9px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(#6366f1, #ec4899);
    border-radius: 10px;
}

/* ============ MOBILE ============ */
@media (max-width: 640px) {
    .block-container { padding: 2rem 1.3rem !important; margin-top: 1rem; border-radius: 24px; }
    h1 { font-size: 2.2rem !important; }
}
</style>
""", unsafe_allow_html=True)
