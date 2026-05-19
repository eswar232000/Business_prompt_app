# =========================================================
# INTERNATIONAL BUSINESS MARKETING PROMPT APPLICATION
# =========================================================

import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="International Business Marketing AI",
    page_icon="🌍",
    layout="centered"
)

# =========================================================
# CUSTOM CSS
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

.output-box {
    background-color: #1E1E1E;
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
    border: 2px solid #00D4AA;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================

st.title("🌍 International Business Marketing Prompt Application")

st.markdown("""
Generate:
- Global Product Titles
- Marketing Slogans
- Advertising Content
- Brand Strategy
- International Sales Description
""")

# =========================================================
# USER INPUT
# =========================================================

product_name = st.text_input(
    "Enter Product Name",
    placeholder="Example: FitPulse Global X Pro"
)

# =========================================================
# GENERATE CONTENT FUNCTION
# =========================================================

def generate_marketing_content(product):

    slogan = f'"Empowering Every Moment Worldwide with {product}"'

    digital_marketing = f"""
{product} combines intelligent innovation, premium design, and
advanced technology to deliver an exceptional global customer
experience. Built for modern consumers, the product enhances
lifestyle, productivity, and emotional engagement across
international markets.
"""

    brand_strategist = f"""
{product} creates a powerful emotional connection between
innovation, trust, and premium lifestyle branding. The brand
positions itself as a globally recognized solution that reflects
quality, reliability, and customer-centric excellence.
"""

    sales_consultant = f"""
{product} is strategically optimized for international business
expansion with multilingual compatibility, global usability,
and scalable market potential. Its premium positioning and
universal appeal make it highly competitive in worldwide markets.
"""

    return slogan, digital_marketing, brand_strategist, sales_consultant

# =========================================================
# GENERATE BUTTON
# =========================================================

if st.button("🚀 Generate Marketing Content"):

    if product_name.strip() == "":

        st.warning("Please enter a product name.")

    else:

        slogan, digital_marketing, brand_strategist, sales_consultant = generate_marketing_content(product_name)

        # =========================================================
        # DISPLAY OUTPUT
        # =========================================================

        st.success("Marketing Content Generated Successfully!")

        st.markdown(f"""
<div class="output-box">

<h3>🌍 Global-Ready Product Title</h3>
<p>{product_name}</p>

<h3>📢 Powerful Marketing Slogan</h3>
<p>{slogan}</p>

<h3>💡 Digital Marketing Expert</h3>
<p>{digital_marketing}</p>

<h3>🎯 Brand Strategist</h3>
<p>{brand_strategist}</p>

<h3>🌎 International Sales Consultant</h3>
<p>{sales_consultant}</p>

</div>
""", unsafe_allow_html=True)

# =========================================================
# SAMPLE OUTPUT
# =========================================================

st.markdown("---")

st.markdown("## 💡 Example Input")

st.info("FitPulse Global X Pro")

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("Developed using Streamlit + Python")
