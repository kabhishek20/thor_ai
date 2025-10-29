# backend/stt.py
import speech_recognition as sr
from backend.llm_engine import llm_query, init_llm

# Initialize LLM once
llm = init_llm()

def listen_and_transcribe(language_preference="auto", timeout=5, phrase_time_limit=7):
    """
    Listens to user's voice (English/Hindi/Hinglish), converts speech to text,
    and then normalizes it to a clean English command using the local LLM.
    """
    recognizer = sr.Recognizer()

    lang_map = {
        "auto": ["en-IN", "hi-IN"],  # try both
        "en": ["en-IN"],
        "hi": ["hi-IN"]
    }

    with sr.Microphone() as source:
        print("\n🎙️ Listening... (Speak in English or Hindi)")
        recognizer.adjust_for_ambient_noise(source, duration=0.8)

        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            print("🧠 Processing your speech...")

            text = None
            detected_lang = None

            # Try both languages for auto mode
            for lang in lang_map.get(language_preference, ["en-IN"]):
                try:
                    text = recognizer.recognize_google(audio, language=lang)
                    detected_lang = lang
                    break
                except sr.UnknownValueError:
                    continue

            if text is None:
                print("🤔 Could not understand the audio.")
                return None, None

            lang_display = "English 🇬🇧" if detected_lang == "en-IN" else "Hindi 🇮🇳"
            print(f"✅ Raw Speech Detected ({lang_display}): {text}")

            # Convert to English via LLM
            english_command = llm_query(text, system_role="translator")

            print(f"💬 Final English Command: {english_command}\n")
            return english_command, detected_lang

        except sr.WaitTimeoutError:
            print("⚠️ Listening timed out (no speech detected).")
            return None, None
        except sr.RequestError as e:
            print(f"❌ Speech recognition service error: {e}")
            return None, None


if __name__ == "__main__":
    print("🎧 Voice Assistant Test (Bilingual STT + LLM Normalization)")
    while True:
        command, lang = listen_and_transcribe(language_preference="auto")
        if command:
            print(f"🧾 Result: {command} | Language: {lang}\n")
        else:
            print("No valid speech detected.\n")
