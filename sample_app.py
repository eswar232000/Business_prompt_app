import streamlit as st
from transformers import pipeline

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="International Business Marketing Prompt Application",
    page_icon="🌍",
    layout="wide"
)

# ============================================================
# TITLE
# ============================================================

st.title("🌍 International Business Marketing Prompt Application")

st.markdown("""
Generate globally marketable advertising content using Generative AI.

This application creates:
- Global-ready product titles
- Powerful marketing slogans
- Advertising descriptions from multiple expert perspectives
""")

# ============================================================
# SIDEBAR SETTINGS
# ============================================================

st.sidebar.header("⚙️ AI Settings")

max_tokens = st.sidebar.slider(
    "Max New Tokens",
    min_value=50,
    max_value=500,
    value=250
)

temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.1,
    max_value=1.0,
    value=0.7
)

# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    generator = pipeline(
        "text-generation",
        model="HuggingFaceTB/SmolLM2-360M-Instruct"
    )

    return generator

generator = load_model()

# ============================================================
# USER INPUT
# ============================================================

st.subheader("📦 Product Information")

product_name = st.text_input(
    "Enter Product Name",
    placeholder="Example: Smart Fitness Watch"
)

product_category = st.selectbox(
    "Select Product Category",
    [
        "Technology",
        "Healthcare",
        "Fashion",
        "Education",
        "Food & Beverage",
        "Finance",
        "Automobile",
        "Travel",
        "Sports",
        "Beauty"
    ]
)

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

tone = st.selectbox(
    "Marketing Tone",
    [
        "Professional",
        "Luxury",
        "Friendly",
        "Innovative",
        "Emotional",
        "Premium",
        "Corporate"
    ]
)

# ============================================================
# GENERATE BUTTON
# ============================================================

if st.button("🚀 Generate International Marketing Content"):

    if product_name.strip() == "":
        st.warning("Please enter a product name.")

    else:

        # ============================================================
        # PROMPT TEMPLATE
        # ============================================================

        prompt = f"""
You are an international business marketing strategist.

Create globally marketable advertising content
for the following product.

PRODUCT DETAILS:
Product Name: {product_name}
Category: {product_category}
Target Market: {target_market}
Marketing Tone: {tone}

TASKS:

1. Generate a Global-Ready Product Title

2. Generate a Powerful Marketing Slogan

3. Generate Advertising Descriptions from:
   - Digital Marketing Expert
   - Luxury Brand Strategist
   - Global Sales Consultant

REQUIREMENTS:
- Use persuasive international branding
- Make content emotionally engaging
- Ensure global audience compatibility
- Use professional marketing language
- Keep content attractive and modern

FORMAT:

GLOBAL PRODUCT TITLE:
...

MARKETING SLOGAN:
...

DIGITAL MARKETING EXPERT:
...

LUXURY BRAND STRATEGIST:
...

GLOBAL SALES CONSULTANT:
...
"""

        # ============================================================
        # MODEL GENERATION
        # ============================================================

        with st.spinner("Generating AI Marketing Content..."):

            result = generator(
                prompt,
                max_new_tokens=max_tokens,
                temperature=temperature,
                do_sample=True
            )

            output = result[0]["generated_text"]

        # ============================================================
        # DISPLAY OUTPUT
        # ============================================================

        st.success("Content Generated Successfully!")

        st.markdown("## 🌍 Generated International Marketing Content")

        st.write(output)

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown("""
### 📘 Technologies Used
- Streamlit
- Hugging Face Transformers
- Generative AI
- Prompt Engineering
""")
