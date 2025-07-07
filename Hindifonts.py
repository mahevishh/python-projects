import streamlit as st
from googletrans import Translator
import streamlit.components.v1 as components

st.set_page_config(page_title="Hindi Font Translator", layout="centered")
st.title("🌐 English ➜ Hindi Translator with 10 Google Fonts")

# Google Fonts to use
google_fonts = {
    "Tiro Devanagari Hindi": "'Tiro Devanagari Hindi', serif",
    "Matangi": "'Matangi', cursive",
    "Kalam": "'Kalam', cursive",
    "Pragati Narrow": "'Pragati Narrow', sans-serif",
    "Modak": "'Modak', cursive",
    "Palanquin Dark": "'Palanquin Dark', sans-serif",
    "Arya": "'Arya', sans-serif",
    "Gotu": "'Gotu', sans-serif",
    "Jaini Purva": "'Jaini Purva', cursive",
    "Annapurna SIL": "'Annapurna SIL', serif"
}

# Embed Google Font links + styles
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Tiro+Devanagari+Hindi&family=Matangi&family=Kalam&family=Pragati+Narrow&family=Modak&family=Palanquin+Dark&family=Arya&family=Gotu&family=Jaini+Purva&family=Annapurna+SIL&display=swap" rel="stylesheet">

<style>
.font-box {
    font-size: 24px;
    padding: 12px;
    border: 1px solid #ddd;
    border-radius: 8px;
    background: #f7f7f7;
    margin-bottom: 16px;
}
.copy-btn {
    padding: 8px 16px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 16px;
    cursor: pointer;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

translator = Translator()
eng_text = st.text_area("✏️ Enter English text:")

if st.button("Translate"):
    if eng_text.strip():
        hindi_text = translator.translate(eng_text, src="en", dest="hi").text
        st.success("✅ Translated to Hindi:")
        st.code(hindi_text, language="text")

        for i, (font_name, css_font) in enumerate(google_fonts.items(), start=1):
            st.markdown(f"""
                <div class="font-box" style="font-family: {css_font};">
                    {hindi_text}
                </div>
            """, unsafe_allow_html=True)

            components.html(f"""
                <button class="copy-btn" onclick="navigator.clipboard.writeText(`{hindi_text}`); alert('✅ Copied!')">
                    📋 Copy Font {i} ({font_name})
                </button>
            """, height=60)
    else:
        st.warning("⚠️ Please enter some English text.")
