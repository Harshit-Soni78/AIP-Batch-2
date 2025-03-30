import langid
from deep_translator import GoogleTranslator

def detect_language(text):
    """Detect the language of the input text."""
    lang, confidence = langid.classify(text)
    return lang, confidence

def translate_text(text, source_language=None, target_language='english'):
    """
    Translate text from source language to target language.
    If source_language is not provided, it will be auto-detected.
    """
    # Normalize target language
    target_lang_map = {
        'english': 'en',
        'french': 'fr',
        'spanish': 'es',
        'german': 'de',
        'italian': 'it',
        'portuguese': 'pt',
        'arabic': 'ar',
        'chinese': 'zh-CN',
        'japanese': 'ja',
        'korean': 'ko',
        'russian': 'ru',
        'hindi': 'hi'
    }
    
    # Convert full language name to code
    target_code = target_language.lower()
    if target_code in target_lang_map:
        target_code = target_lang_map[target_code]
    
    # Auto-detect source language if not provided
    if not source_language:
        detected_lang, confidence = detect_language(text)
        source_language = detected_lang
        source_info = f"Detected language: {source_language} (confidence: {confidence:.2f})"
    else:
        # Convert source language name to code if needed
        if source_language.lower() in target_lang_map:
            source_language = target_lang_map[source_language.lower()]
        source_info = f"Source language: {source_language}"
    
    # Google Translator has a character limit, so split into chunks
    max_chunk_size = 5000
    chunks = [text[i:i+max_chunk_size] for i in range(0, len(text), max_chunk_size)]
    
    translated_chunks = []
    for chunk in chunks:
        try:
            translator = GoogleTranslator(source=source_language, target=target_code)
            translated_chunk = translator.translate(chunk)
            translated_chunks.append(translated_chunk)
        except Exception as e:
            # Fallback: try without specifying source language
            try:
                translator = GoogleTranslator(source='auto', target=target_code)
                translated_chunk = translator.translate(chunk)
                translated_chunks.append(translated_chunk)
            except:
                translated_chunks.append(f"[Translation error: {str(e)}]")
    
    translated_text = "".join(translated_chunks)
    
    # Prepare the output with metadata
    output = []
    output.append(f"TRANSLATION\n")
    output.append(source_info)
    output.append(f"Target language: {target_language}")
    output.append("\n" + "="*50 + "\n")
    output.append(translated_text)
    
    return "\n".join(output)
