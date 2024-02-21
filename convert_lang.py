from translate import Translator

def translate_text(text, source_lang, target_lang):
    translator = Translator(from_lang=source_lang, to_lang=target_lang)
    translation = translator.translate(text)
    return translation

text = "Hello, Rahul how are you?"
source_lang = "en"  # English
target_lang = "fr"  # French

translated_text = translate_text(text, source_lang, target_lang)
print(translated_text)

