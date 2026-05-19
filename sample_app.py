%%writefile app.py

import streamlit as st
from transformers import pipeline

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="International Business Marketing Prompt Application",
    page_icon="🌍",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #0f172a;
    color: white;
}

.stTextInput > div > div > input {
    background-color: #1e293b;
    color: white;
}

.stSelectbox > div > div {
    background-color: #1e293b;
    color: white;
}

.stButton button {
    background-color: #14b8a6;
    color: white;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    font-size: 18px;
}

.output-box {
    background-color: #111827;
    padding: 20px;
    border-radius: 12px;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================

st.title("🌍 International Business Marketing Prompt Application")

st.markdown("""
### AI-Powered Global Marketing Content Generator

This application generates:

✅ Global-Ready Product Title  
✅ Powerful Marketing Slogan  
✅ Advertising Descriptions from Three Expert Perspectives  

The generated content follows:
- International marketing standards
- Persuasive branding principles
- Emotional engagement strategies
- Global audience compatibility
""")

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.header("⚙️ AI Configuration")

temperature = st.sidebar.slider(
    "Temperature",
    0.1,
    1.0,
    0.7
)

max_tokens = st.sidebar.slider(
    "Max New Tokens",
    100,
    800,
    400
)

# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():

    generator = pipeline(
        task="text-generation",
        model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    )

    return generator

generator = load_model()

# =========================================================
# PRODUCT CATEGORY DATA
# =========================================================

category_examples = {

    "Technology": {
        "keywords": "AI-powered, smart innovation, digital lifestyle",
        "benefits": "automation, productivity, connectivity"
    },

    "Healthcare": {
        "keywords": "wellness, healthcare innovation, smart monitoring",
        "benefits": "health improvement, safety, patient care"
    },

    "Fashion": {
        "keywords": "luxury fashion, modern style, premium wear",
        "benefits": "style enhancement, confidence, elegance"
    },

    "Education": {
        "keywords": "smart learning, AI education, digital classroom",
        "benefits": "knowledge growth, learning efficiency"
    },

    "Food & Beverage": {
        "keywords": "organic quality, global taste, premium ingredients",
        "benefits": "healthy lifestyle, delicious experience"
    },

    "Finance": {
        "keywords": "secure finance, digital banking, smart investment",
        "benefits": "financial growth, secure transactions"
    },

    "Automobile": {
        "keywords": "smart mobility, future transportation, electric innovation",
        "benefits": "performance, sustainability, comfort"
    },

    "Travel": {
        "keywords": "luxury travel, smart tourism, global exploration",
        "benefits": "comfort, adventure, convenience"
    },

    "Sports": {
        "keywords": "high performance, athletic innovation, fitness technology",
        "benefits": "strength, endurance, active lifestyle"
    },

    "Beauty": {
        "keywords": "premium skincare, beauty innovation, self-care",
        "benefits": "confidence, beauty enhancement, wellness"
    }
}

# =========================================================
# USER INPUT
# =========================================================

st.subheader("📦 Product Information")

col1, col2 = st.columns(2)

with col1:

    product_name = st.text_input(
        "Enter Product Name",
        placeholder="Example: Smart Watch"
    )

    product_category = st.selectbox(
        "Select Product Category",
        list(category_examples.keys())
    )

with col2:

    target_market = st.selectbox(
        "Target Global Market",
        [
            "Global Audience",
            "North America",
            "Europe",
            "Asia",
            "Middle East",
            "Africa",
            "South America"
        ]
    )

    marketing_style = st.selectbox(
        "Marketing Style",
        [
            "Professional",
            "Luxury",
            "Modern",
            "Emotional",
            "Corporate",
            "Innovative"
        ]
    )

# =========================================================
# GENERATE CONTENT
# =========================================================

if st.button("🚀 Generate International Marketing Content"):

    if product_name.strip() == "":

        st.warning("Please enter a product name.")

    else:

        category_data = category_examples[product_category]

        # =========================================================
        # ADVANCED STRUCTURED PROMPT
        # =========================================================

        prompt = f"""
You are a world-class International Business Marketing Expert.

Generate highly professional international advertising content.

PRODUCT DETAILS:
Product Name: {product_name}
Category: {product_category}
Target Market: {target_market}
Marketing Style: {marketing_style}

CATEGORY KEYWORDS:
{category_data['keywords']}

CATEGORY BENEFITS:
{category_data['benefits']}

STRICT INSTRUCTIONS:

The response MUST EXACTLY contain the following sections:

1. GLOBAL-READY PRODUCT TITLE
- Create a premium global brand title
- Include modern branding language

2. POWERFUL MARKETING SLOGAN
- Emotional
- Memorable
- Internationally attractive

3. PRODUCT ADVERTISING DESCRIPTION

A. DIGITAL MARKETING EXPERT
Focus on:
- Social media branding
- Customer engagement
- Online visibility
- Digital growth

B. GLOBAL BRAND STRATEGIST
Focus on:
- International positioning
- Premium global branding
- Worldwide market appeal

C. SALES AND BUSINESS CONSULTANT
Focus on:
- Customer value
- Competitive advantage
- Business growth
- Product benefits

IMPORTANT:
- Ensure the content matches the product category
- Make the response realistic and premium
- Use professional business English
- Make every section unique
- Avoid repeating the same sentences

OUTPUT FORMAT:

=================================================
🌍 GLOBAL-READY PRODUCT TITLE
=================================================

=================================================
🔥 POWERFUL MARKETING SLOGAN
=================================================

=================================================
📱 DIGITAL MARKETING EXPERT
=================================================

=================================================
🌐 GLOBAL BRAND STRATEGIST
=================================================

=================================================
💼 SALES AND BUSINESS CONSULTANT
=================================================
"""

        # =========================================================
        # GENERATE RESPONSE
        # =========================================================

        with st.spinner("Generating Global Marketing Content..."):

            result = generator(
                prompt,
                max_new_tokens=max_tokens,
                temperature=temperature,
                top_p=0.95,
                do_sample=True
            )

            output = result[0]["generated_text"]

        # =========================================================
        # CLEAN RESPONSE
        # =========================================================

        if prompt in output:
            output = output.replace(prompt, "")

        # =========================================================
        # DISPLAY OUTPUT
        # =========================================================

        st.success("✅ International Marketing Content Generated Successfully")

        st.markdown(
            f"""
            <div class="output-box">
            <pre style="color:white; white-space: pre-wrap; font-size:16px;">
{output}
            </pre>
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown("""
### 📘 Technologies Used
- Streamlit
- Hugging Face Transformers
- Prompt Engineering
- Generative AI
- International Marketing AI
""")
