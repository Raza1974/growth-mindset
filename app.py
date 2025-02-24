import streamlit as st
import random
import time

# Growth Mindset Quotes
quotes = [
    "💡 Mistakes are proof that you are trying.",
    "🚀 Failure is simply the opportunity to begin again, this time more intelligently.",
    "🔥 Hard work beats talent when talent doesn’t work hard.",
    "🌟 The only limit to our realization of tomorrow is our doubts of today.",
    "🎯 Challenges are what make life interesting. Overcoming them is what makes life meaningful.",
    "💪 Growth and comfort do not coexist.",
    "🌱 Strive for progress, not perfection.",
    "🔥 The only way to do great work is to love what you do."
]

# Set Page Configuration
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱", layout="centered")

# Custom Styling
st.markdown(
    """
    <style>
        body {
            background-color: #f5f7fa;
        }
        .title {
            font-size: 42px;
            background: -webkit-linear-gradient(left, #1E88E5, #388E3C);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: bold;
            text-align: center;
            margin-bottom: 10px;
        }
        .subheader {
            font-size: 22px;
            color: #424242;
            text-align: center;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .quote {
            font-size: 20px;
            font-style: italic;
            color: #388E3C;
            text-align: center;
            margin: 15px 0;
            background-color: #e8f5e9;
            padding: 10px;
            border-radius: 10px;
        }
        .footer {
            text-align: center;
            font-size: 16px;
            color: #757575;
            margin-top: 30px;
        }
        .footer a {
            color: #1E88E5;
            text-decoration: none;
            font-weight: bold;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title
st.markdown('<div class="title">🌱 Growth Mindset Challenge</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Every challenge is a step toward growth. Keep going! 🚀</div>', unsafe_allow_html=True)

# Display Random Motivational Quote
if "quote" not in st.session_state:
    st.session_state.quote = random.choice(quotes)

st.markdown(f'<div class="quote">"{st.session_state.quote}"</div>', unsafe_allow_html=True)

if st.button("🔄 Get New Quote"):
    st.session_state.quote = random.choice(quotes)
    st.rerun()

# User Inputs
st.subheader("📝 Your Reflection")
challenge = st.text_area("💭 What challenge did you face today?", placeholder="Describe your challenge...")
lesson = st.text_area("📚 What did you learn from it?", placeholder="Share your lesson...")

# Submit Button
if st.button("✅ Submit Your Growth"):
    if challenge and lesson:
        with st.spinner("Processing..."):
            time.sleep(1.5)
        st.success("🎉 Great! You're embracing a growth mindset! Keep learning and evolving. 💡")

        # Simulate progress in growth mindset
        progress = st.progress(0)
        for percent in range(1, 101):
            time.sleep(0.02)
            progress.progress(percent)

    else:
        st.warning("⚠️ Please fill in both fields before submitting.")

# Footer with Projects
st.markdown(
    """
    <div class="footer">
         *Keep pushing your limits! Growth is a journey, not a destination.  
         *Stay curious, embrace challenges, and celebrate progress.  
         *Every small step you take leads to great success. Keep thriving! </div>
    """,
    unsafe_allow_html=True
)

