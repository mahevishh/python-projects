import streamlit as st
from deep_translator import GoogleTranslator

# --- Setup ---
st.set_page_config(page_title="Hindi Font Preview", layout="centered")
st.title("🌐 English to Hindi Translator with Stylish Google Fonts")

# --- Input ---
english_text = st.text_area("Enter English text:")

# --- Google Fonts Links ---
google_fonts = {
    "Tiro Devanagari Hindi": "Tiro+Devanagari+Hindi",
    "Matangi": "Matangi",
    "Kalam": "Kalam",
    "Pragati Narrow": "Pragati+Narrow",
    "Modak": "Modak",
    "Palanquin Dark": "Palanquin+Dark",
    "Arya": "Arya",
    "Gotu": "Gotu",
    "Jaini Purva": "Jaini+Purva",
    "Annapurna SIL": "Annapurna+SIL"
}

# --- Include Google Fonts in HTML ---
font_links = "\n".join([
    f"<link href='https://fonts.googleapis.com/css2?family={font.replace(' ', '+')}&display=swap' rel='stylesheet'>"
    for font in google_fonts.values()
])
st.markdown(font_links, unsafe_allow_html=True)

# --- Translate and Display ---
if st.button("Translate"):
    if english_text.strip():
        translated = GoogleTranslator(source='en', target='hi').translate(english_text)

        st.success("✅ Translated to Hindi:")
        st.code(translated, language="text")

        for i, (name, font_url) in enumerate(google_fonts.items(), start=1):
            st.markdown(f"""
            <div style="font-family: '{name}', sans-serif;
                        font-size: 24px;
                        padding: 12px;
                        border: 1px solid #ccc;
                        border-radius: 10px;
                        margin-bottom: 16px;
                        background: #f9f9f9;">
                {translated}
            </div>
            <button onclick="navigator.clipboard.writeText('{translated}'); alert('✅ Copied!')"
                    style="padding:6px 12px; background:#007bff; color:white; border:none;
                           border-radius:6px; cursor:pointer; font-size:16px; margin-bottom:20px;">
                📋 Copy Font {i} ({name})
            </button>
            """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter some text to translate.")
