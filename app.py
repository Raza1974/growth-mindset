import streamlit as st
import random

# Growth Mindset Quotes
quotes = [
    "💡 Mistakes are proof that you are trying.",
    "🚀 Failure is simply the opportunity to begin again, this time more intelligently.",
    "🔥 Hard work beats talent when talent doesn’t work hard.",
    "🌟 The only limit to our realization of tomorrow is our doubts of today."
]

# Set Page Configuration
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱", layout="centered")

# Custom Styling
st.markdown(
    """
    <style>
        .title {
            font-size: 36px;
            color: #1E88E5;
            font-weight: bold;
            text-align: center;
        }
        .subheader {
            font-size: 20px;
            color: #424242;
            text-align: center;
        }
        .quote {
            font-size: 18px;
            font-style: italic;
            color: #388E3C;
            text-align: center;
            margin-top: 10px;
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
st.markdown(f'<div class="quote">"{random.choice(quotes)}"</div>', unsafe_allow_html=True)

# User Challenge Input
challenge = st.text_area("💭 What challenge did you face today?", placeholder="Describe your challenge...")

# User Reflection Input
lesson = st.text_area("📚 What did you learn from it?", placeholder="Share your lesson...")

if st.button("✅ Submit Your Growth"):
    if challenge and lesson:
        st.success("🎉 Great! You're embracing a growth mindset! Keep learning and evolving. 💡")
    else:
        st.warning("⚠️ Please fill in both fields before submitting.")

# Footer with Profile & Projects
st.markdown(
    """
    <div class="footer">
        🔗 **My Projects:**  
        - 🎨 <a href="https://portfolio-slide.vercel.app/" target="_blank">Portfolio Slide</a>  
        - 📝 <a href="https://resume-builder-phi-mauve.vercel.app/" target="_blank">Resume Builder</a>  
        - 📄 <a href="https://dynamic-resume-psi.vercel.app/" target="_blank">Dynamic Resume</a>  
        - 🖩 <a href="https://screen-calculator.vercel.app/" target="_blank">Screen Calculator</a>  
        - 💰 <a href="https://coin-market-cyan.vercel.app/" target="_blank">Coin Market</a>  
        - 🍖 <a href="https://mart-meat.vercel.app/" target="_blank">Mart Meat</a>  
    </div>
    """,
    unsafe_allow_html=True
)
