import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

HOST_PERSONAS = {
    "serious": "You are a strict, logical judge. Respond concisely with 'Yes' or 'No'.",
    "cheery": "You are a fun, friendly host who likes jokes but must answer only 'Yes' or 'No'."
}

async def does_guess_beat_seed(seed: str, guess: str, persona: str = "serious") -> str:
    prompt = f"Does '{guess}' beat '{seed}' in a creative rock-paper-scissors-style game? Answer only with Yes or No."
    system_message = HOST_PERSONAS.get(persona.lower(), HOST_PERSONAS["serious"])

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            max_tokens=3,
            temperature=0.7
        )
        answer = response["choices"][0]["message"]["content"].strip()
        return answer
    except Exception as e:
        print("OpenAI error:", e)
        return "Error"
