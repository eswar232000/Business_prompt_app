# =========================================================
# INTERNATIONAL BUSINESS MARKETING PROMPT APPLICATION
# =========================================================
# Developed using:
# Streamlit + Hugging Face Transformers + Generative AI
# =========================================================

import streamlit as st
from transformers import pipeline

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="International Business Marketing AI",
    page_icon="🌍",
    layout="wide"
)

# =========================================================
# CUSTOM CSS STYLING
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

h1 {
    color: #00D4AA;
    text-align: center;
    font-size: 42px;
}

h2, h3 {
    color: #00D4AA;
}

.stButton > button {
    background-color: #00D4AA;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    border: none;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #00B894;
}

.stTextInput > div > div > input {
    background-color: #262730;
    color: white;
    border-radius: 10px;
}

.output-box {
    background-color: #1E1E1E;
    padding: 25px;
    border-radius: 15px;
    margin-top: 20px;
    color: white;
    border: 2px solid #00D4AA;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================

st.title("🌍 International Business Marketing Prompt Application")

st.markdown("""
### AI-Powered Global Marketing Content Generator

This application automatically generates:

✅ Global-Ready Product Titles  
✅ Powerful Marketing Slogans  
✅ Advertising Content from Multiple Expert Perspectives  

### Advertising Perspectives:
- Digital Marketing Expert
- Brand Strategist
- International Sales Consultant

### Features:
- Professional Branding
- Emotional Engagement
- International Marketing Standards
- Persuasive Advertising
- Global Audience Compatibility
- Premium Business Tone

""")

# =========================================================
# LOAD HUGGING FACE MODEL
# =========================================================

@st.cache_resource
def load_model():

    generator = pipeline(
        "text-generation",
        model="gpt2"
    )

    return generator

generator = load_model()

# =========================================================
# SIDEBAR SETTINGS
# =========================================================

st.sidebar.title("⚙ AI Generation Settings")

temperature = st.sidebar.slider(
    "Creativity Level (Temperature)",
    0.1,
    1.0,
    0.8
)

max_tokens = st.sidebar.slider(
    "Maximum Output Length",
    100,
    500,
    300
)

# =========================================================
# USER INPUT SECTION
# =========================================================

st.markdown("## 🛍 Product Information")

product_name = st.text_input(
    "Enter Product Name",
    placeholder="Example: Smart Fitness Watch"
)

target_market = st.selectbox(
    "Select Target Market",
    [
        "Global Market",
        "Healthcare",
        "Education",
        "Technology",
        "Finance",
        "Fashion",
        "Automobile",
        "Retail",
        "Sports & Fitness"
    ]
)

# =========================================================
# GENERATE BUTTON
# =========================================================

if st.button("🚀 Generate International Marketing Content"):

    if product_name.strip() == "":

        st.warning("⚠ Please enter a product name.")

    else:

        # =========================================================
        # PROMPT TEMPLATE
        # =========================================================

        prompt = f"""
You are a world-class International Business Marketing Expert.

Generate professional international marketing content for the following product.

Product Name:
{product_name}

Target Market:
{target_market}

Generate the following:

1. A Global-Ready Product Title

2. A Powerful Marketing Slogan

3. Product Advertising Descriptions from:
   - Digital Marketing Expert
   - Brand Strategist
   - International Sales Consultant

Requirements:
- Professional branding
- Emotional engagement
- International marketing standards
- Persuasive advertising
- Global audience compatibility
- Premium business tone
- Clear and professional formatting

Format the response EXACTLY as follows:

Global-Ready Product Title:
<answer>

Powerful Marketing Slogan:
<answer>

Digital Marketing Expert:
<answer>

Brand Strategist:
<answer>

International Sales Consultant:
<answer>
"""

        # =========================================================
        # GENERATE OUTPUT
        # =========================================================

        with st.spinner("Generating AI Marketing Content..."):

            result = generator(
                prompt,
                max_length=max_tokens,
                do_sample=True,
                temperature=temperature,
                truncation=True
            )

            output = result[0]["generated_text"]

        # =========================================================
        # DISPLAY OUTPUT
        # =========================================================

        st.success("✅ Marketing Content Generated Successfully!")

        st.markdown("## 📢 Generated Marketing Content")

        st.markdown(f"""
        <div class="output-box">
        <pre>{output}</pre>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# SAMPLE OUTPUT SECTION
# =========================================================

st.markdown("---")

st.markdown("## 💡 Example Input")

st.info("Smart Fitness Watch")

st.markdown("""
### Example Output

Global-Ready Product Title:
FitPulse Global X Pro

Powerful Marketing Slogan:
"Empowering Every Moment Worldwide"

Digital Marketing Expert:
FitPulse Global X Pro combines intelligent health tracking,
premium design, and seamless connectivity to deliver the
ultimate fitness experience for modern global consumers.

Brand Strategist:
FitPulse creates a strong emotional connection between
innovation, wellness, and premium lifestyle branding,
positioning itself as a trusted global fitness technology brand.

International Sales Consultant:
FitPulse Global X Pro is optimized for international markets
with multilingual compatibility, universal usability, and
scalable global sales potential.
""")

# =========================================================
# DEPLOYMENT INSTRUCTIONS
# =========================================================

st.markdown("---")

st.markdown("## ☁ Deployment Instructions")

st.markdown("""
### Step 1: Create requirements.txt

Add the following libraries:

streamlit  
transformers  
torch  
sentencepiece

---

### Step 2: Upload Files to GitHub

Upload:
- app.py
- requirements.txt

---

### Step 3: Deploy in Streamlit Cloud

Go to:
https://streamlit.io/cloud

Then:
1. Click New App
2. Connect GitHub Repository
3. Select app.py
4. Click Deploy

""")

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("""
Developed using Streamlit + Hugging Face Transformers + Prompt Engineering
""")
