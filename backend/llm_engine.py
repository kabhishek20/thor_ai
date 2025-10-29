# backend/llm_engine.py
import subprocess
import sys

MODEL_NAME = "llama3"

def init_llm():
    print(f"✅ LLM Engine initialized using Ollama model: {MODEL_NAME}")
    return {"model": MODEL_NAME}


def llm_query(prompt: str, system_role: str = "translator") -> str:
    """
    Sends a prompt to Ollama and returns a clean English command (UTF-8 safe).
    """
    if system_role == "translator":
        system_prompt = (
            "You are an intelligent voice assistant command normalizer. "
            "The user might speak in Hindi, English, or mixed Hinglish. "
            "Convert it into a **clear, short English command** that a computer can understand.\n\n"
            "Guidelines:\n"
            "- Only output the final English command. No explanations.\n"
            "- Be concise (max 10 words).\n"
            "- Examples:\n"
            "  'भाई यूट्यूब खोलो' → 'open YouTube'\n"
            "  'समय क्या है' → 'what is the time'\n"
            "  'chrome kholo aur google pe cats search karo' → 'open Chrome and search cats on Google'\n"
            "  'volume badhao' → 'increase the volume'"
        )
    else:
        system_prompt = "You are a helpful AI assistant."

    full_prompt = (
        f"{system_prompt}\n\n"
        f"User said: {prompt}\n\n"
        f"Output: (only the final English command, nothing else)"
    )

    try:
        process = subprocess.Popen(
            ["ollama", "run", MODEL_NAME],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8"  # ✅ Force UTF-8 encoding
        )

        stdout, stderr = process.communicate(input=full_prompt)

        if stderr:
            print(f"⚠️ Ollama stderr: {stderr.strip()}")

        output = stdout.strip()

        if "Output:" in output:
            output = output.split("Output:")[-1].strip()

        output = output.replace('"', '').replace("'", "").strip()
        return output

    except Exception as e:
        print(f"❌ Ollama LLM error: {e}")
        return prompt


if __name__ == "__main__":
    init_llm()
    test_inputs = [
        "भाई यूट्यूब खोलो",
        "समय क्या है",
        "chrome kholo aur google pe cats search karo",
        "volume badhao",
        "light off kar do"
    ]
    for s in test_inputs:
        print(f"\n🗣️ Input: {s}")
        print(f"💬 English Command: {llm_query(s)}")
