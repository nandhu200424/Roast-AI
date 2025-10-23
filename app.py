import streamlit as st
import os
from groq import Groq

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Limitly - Roast AI",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS STYLING
# ============================================================
st.markdown("""
<style>
/* Main container styling */
.main-header {
    font-size: 4rem;
    font-weight: bold;
    text-align: center;
    color: #ff6b6b;
    margin: 2rem 0;
    text-shadow: 3px 3px 6px rgba(0,0,0,0.5);
    background: linear-gradient(45deg, #ff6b6b, #ff8e8e, #ffa8a8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    display: block;
    z-index: 10;
    position: relative;
}

/* Chat message styling */
.stChatMessage {
    margin: 1rem 0;
    padding: 1rem;
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

/* User message styling */
.stChatMessage[data-testid="user-message"] {
    background: linear-gradient(135deg, #ff6b6b, #ff8e8e);
    color: white;
    margin-left: 20%;
}

/* Assistant message styling */
.stChatMessage[data-testid="assistant-message"] {
    background: linear-gradient(135deg, #2d2d2d, #1a1a1a);
    color: #ff6b6b;
    margin-right: 20%;
    border: 2px solid #ff6b6b;
}

/* Roast doodle animations */
.roast-doodle {
    font-size: 2rem;
    animation: bounce 2s infinite;
    display: inline-block;
}

@keyframes bounce {
    0%, 20%, 50%, 80%, 100% {
        transform: translateY(0);
    }
    40% {
        transform: translateY(-10px);
    }
    60% {
        transform: translateY(-5px);
    }
}

/* Sidebar styling */
.sidebar .sidebar-content {
    background: linear-gradient(180deg, #1a1a1a, #2d2d2d);
}

/* Button styling */
.stButton > button {
    background: linear-gradient(45deg, #ff6b6b, #ff8e8e);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.5rem 1rem;
    font-weight: bold;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(255, 107, 107, 0.5);
}

/* Chat input styling */
.stTextInput > div > div > input {
    border-radius: 15px;
    border: 2px solid #ff6b6b;
    padding: 0.5rem 1rem;
    font-size: 1.1rem;
}

/* Stats cards */
.stat-card {
    background: linear-gradient(135deg, #2d2d2d, #1a1a1a);
    padding: 1rem;
    border-radius: 10px;
    border: 1px solid #ff6b6b;
    margin: 0.5rem 0;
    text-align: center;
}

/* Roast intensity indicator */
.roast-intensity {
    background: linear-gradient(90deg, #ff6b6b, #ff8e8e, #ffa8a8);
    height: 10px;
    border-radius: 5px;
    margin: 0.5rem 0;
}

/* Quick roast buttons */
.quick-roast-btn {
    background: linear-gradient(45deg, #ff6b6b, #ff8e8e);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.5rem;
    margin: 0.25rem;
    font-size: 0.9rem;
    transition: all 0.3s ease;
}

.quick-roast-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 15px rgba(255, 107, 107, 0.4);
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# INITIALIZE GROQ CLIENT - FIXED VERSION
# ============================================================
def init_groq_client():
    """Initialize Groq client with proper error handling"""
    try:
        # Check if API key exists in secrets
        if "GROQ_API_KEY" not in st.secrets:
            st.error("⚠️ GROQ_API_KEY not found in Streamlit secrets!")
            st.info("Please add your Groq API key in Settings → Secrets")
            st.stop()
        
        api_key = st.secrets["GROQ_API_KEY"]
        
        # Validate API key format
        if not api_key or not isinstance(api_key, str):
            st.error("❌ Invalid API key format")
            st.stop()
        
        if not api_key.startswith("gsk_"):
            st.error("❌ API key should start with 'gsk_'")
            st.stop()
        
        # Initialize Groq client
        client = Groq(api_key=api_key)
        
        return client
        
    except Exception as e:
        st.error(f"❌ Error initializing Groq: {str(e)}")
        st.info("Please verify your API key at https://console.groq.com/keys")
        st.stop()

# Initialize client
try:
    client = init_groq_client()
except Exception as e:
    st.error(f"Failed to initialize client: {e}")
    st.stop()

# ============================================================
# SYSTEM PROMPT
# ============================================================
SYSTEM_PROMPT = """You are Limitly — a savage roast AI that roasts EVERYTHING users say with brutal honesty and dark humor.

YOUR JOB:
- Roast whatever the user says - their spending, their statement, their typos, their bragging, ANYTHING
- Be creative, witty, and savage
- Make it funny, not genuinely hurtful
- Keep responses short and punchy (40-60 words)
- End with a quick practical money tip if relevant, otherwise just roast

YOUR STYLE:
- Use clever insults and funny comparisons
- Point out the absurdity or stupidity of what they said
- Be sarcastic and playful
- Use rhetorical questions to mock them

RULES:
- NO jokes about: race, gender, religion, physical appearance
- If they mention DEBT, UNEMPLOYMENT, or MENTAL HEALTH → be supportive instead of roasting
- Otherwise, roast EVERYTHING mercilessly

Examples of your tone:
- "Oh, you think you're smart? Your grammar says otherwise."
- "₹12,000 on shopping? Are you building a mall or just bad at math?"
- "Saved ₹2000? Wow, at this rate you'll retire... never."
- "No spending this week? Either you're broke or finally learning. I'm betting on broke."

Be savage. Be funny. Make them laugh while crying."""

# ============================================================
# ROAST FUNCTION - IMPROVED ERROR HANDLING
# ============================================================
def get_roast(user_message):
    """Get roast response from Groq API"""
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.9,
            max_tokens=150,
        )
        return response.choices[0].message.content
        
    except Exception as e:
        error_str = str(e).lower()
        
        # Handle specific error types
        if "401" in error_str or "unauthorized" in error_str or "invalid" in error_str:
            return "❌ **API Key Error**: Your Groq API key is invalid or expired. Please create a new one at https://console.groq.com/keys and update your Streamlit secrets."
        elif "429" in error_str or "rate limit" in error_str:
            return "⚠️ **Rate Limit**: Too many requests. Please wait a moment and try again."
        elif "503" in error_str or "service unavailable" in error_str:
            return "⚠️ **Service Unavailable**: Groq API is temporarily down. Please try again in a few moments."
        else:
            return f"❌ **Error**: {str(e)}\n\nPlease check your API key and try again."

# ============================================================
# INITIALIZE SESSION STATE
# ============================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ============================================================
# UI - HEADER
# ============================================================
st.markdown("""
<div style="text-align: center; margin: 2rem 0;">
    <h1 style="font-size: 4rem; font-weight: bold; color: #ff6b6b; text-shadow: 3px 3px 6px rgba(0,0,0,0.5); margin: 0;">
        🔥 Limitly - Roast AI 🔥
    </h1>
</div>
""", unsafe_allow_html=True)
st.markdown("**Your savage roast bot. Say anything and get destroyed.**")

# Roast doodle display
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div style="text-align: center; margin: 1rem 0;">
        <span class="roast-doodle">😈</span>
        <span class="roast-doodle">🔥</span>
        <span class="roast-doodle">💀</span>
        <span class="roast-doodle">⚡</span>
        <span class="roast-doodle">🎯</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ============================================================
# UI - CHAT HISTORY
# ============================================================
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant":
            # Add roast doodle for assistant messages
            roast_doodles = ["😈", "🔥", "💀", "⚡", "🎯", "👹", "🤡", "💥"]
            import random
            doodle = random.choice(roast_doodles)
            st.markdown(f"{doodle} **Limitly:**")
        st.markdown(message["content"])

# ============================================================
# UI - CHAT INPUT
# ============================================================
if prompt := st.chat_input("Say anything... I dare you 🔥"):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f"**You:** {prompt}")
    
    # Get roast response with enhanced spinner
    with st.chat_message("assistant"):
        with st.spinner("🔥 Preparing your roast..."):
            roast = get_roast(prompt)
            # Add random roast doodle
            roast_doodles = ["😈", "🔥", "💀", "⚡", "🎯", "👹", "🤡", "💥"]
            import random
            doodle = random.choice(roast_doodles)
            st.markdown(f"{doodle} **Limitly:** {roast}")
    
    # Add assistant response to chat
    st.session_state.messages.append({"role": "assistant", "content": roast})

# ============================================================
# UI - SIDEBAR
# ============================================================
with st.sidebar:
    st.header("🔥 About Limitly")
    st.markdown("""
    **Limitly** is a savage roast AI that destroys everything you say with brutal honesty and dark humor.
    """)
    
    # Roast intensity slider
    st.subheader("⚙️ Roast Settings")
    roast_intensity = st.slider("🔥 Roast Intensity", 1, 10, 7, help="How savage should the roasts be?")
    
    # Roast intensity visual indicator
    intensity_width = (roast_intensity / 10) * 100
    st.markdown(f"""
    <div class="roast-intensity" style="width: {intensity_width}%;"></div>
    <small>Current Level: {roast_intensity}/10</small>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    
    # Stats section
    st.subheader("📊 Roast Stats")
    total_roasts = len([msg for msg in st.session_state.messages if msg["role"] == "assistant"])
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("🔥 Total Roasts", total_roasts)
    with col2:
        st.metric("💬 Messages", len(st.session_state.messages))
    
    # Roast doodles
    st.markdown("""
    <div style="text-align: center; margin: 1rem 0;">
        <span style="font-size: 2rem;">😈</span>
        <span style="font-size: 2rem;">🔥</span>
        <span style="font-size: 2rem;">💀</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.caption("Powered by Groq API | LLM: Llama 3.3 70B")
