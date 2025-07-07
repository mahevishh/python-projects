import streamlit as st
from deep_translator import GoogleTranslator

# --- App Setup ---
st.set_page_config(page_title="Hindi Font Preview", layout="centered")
st.title("🌐 English to Hindi Translator with Stylish Google Fonts")

# --- User Input ---
english_text = st.text_area("Enter English text:")

# --- Google Font List ---
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

# --- Load Google Fonts via HTML links ---
font_links = "\n".join([
    f"<link href='https://fonts.googleapis.com/css2?family={font_url}&display=swap' rel='stylesheet'>"
    for font_url in google_fonts.values()
])
st.markdown(font_links, unsafe_allow_html=True)

# --- Translation and Output ---
if st.button("Translate"):
    if english_text.strip():
        translated = GoogleTranslator(source='en', target='hi').translate(english_text)

        st.success("✅ Translated to Hindi:")
        st.code(translated, language="text")

        for i, (font_name, font_url) in enumerate(google_fonts.items(), start=1):
            st.markdown(f"""
                <div style="
                    font-family: '{font_name}', sans-serif;
                    font-size: 24px;
                    color: black;
                    padding: 12px;
                    border: 1px solid #ccc;
                    border-radius: 10px;
                    background: white;
                    margin-bottom: 10px;">
                    {translated}
                </div>
                <button onclick="navigator.clipboard.writeText(`{translated}`); alert('✅ Copied!')"
                    style="padding: 6px 12px; background: #007bff; color: white; border: none;
                           border-radius: 6px; font-size: 16px; cursor: pointer; margin-bottom: 30px;">
                    📋 Copy Font {i} ({font_name})
                </button>
            """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter some text to translate.")
