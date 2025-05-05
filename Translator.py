from googletrans import Translator

# Create a Translator object
translator = Translator()

# Translate some text
result = translator.translate("Hello, how are you?", src='en', dest='es')

# Print the translated text
print("Original:", result.origin)
print("Translated:", result.text)
