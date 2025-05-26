import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize translator
translator = Translator()

# Set up Streamlit UI
st.set_page_config(page_title="🌍 Language Translator", layout="centered")
st.title("🌍 Language Translator")
st.write("Translate text from one language to another using Google Translate.")

# Input text
text_to_translate = st.text_area("Enter text to translate:")

# Languages (add 'Auto Detect' option)
lang_codes = {'Auto Detect': 'auto'}
lang_codes.update({
    'English': 'en', 'Spanish': 'es', 'French': 'fr', 'German': 'de',
    'Urdu': 'ur', 'Chinese (Simplified)': 'zh-cn', 'Arabic': 'ar',
    'Hindi': 'hi', 'Russian': 'ru'
})

# Language selection
src_lang = st.selectbox("From Language", list(lang_codes.keys()), index=0)
dest_lang = st.selectbox("To Language", list(lang_codes.keys())[1:], index=1)

# Translate Button
if st.button("Translate"):
    if text_to_translate.strip() != "":
        try:
            translated = translator.translate(
                text_to_translate,
                src=lang_codes[src_lang],
                dest=lang_codes[dest_lang]
            )
            detected_lang = LANGUAGES.get(translated.src, "Unknown").title()

            st.success("✅ Translation Successful!")
            st.markdown(f"**Detected Source Language:** {detected_lang}")
            st.markdown("**Translated Text:**")
            st.code(translated.text, language="markdown")

            # Copy-to-clipboard button (tip)
            st.info("💡 Tip: You can copy the translated text above!")

            # Download as text file
            st.download_button(
                label="📄 Download Translation",
                data=translated.text,
                file_name="translation.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"❌ Translation failed: {e}")
    else:
        st.warning("⚠️ Please enter some text to translate.")



