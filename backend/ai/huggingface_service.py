from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

client = InferenceClient(
    token=os.getenv("HUGGINGFACE_API_KEY")
)

SYSTEM_PROMPT = """
You are an advanced financial reasoning assistant.

You specialize in:
- Mutual funds
- SIP investing
- Portfolio diversification
- Risk analysis
- Retirement planning
- Long-term investing

Always:
- Explain clearly
- Mention risks
- Avoid unrealistic promises
- Promote disciplined investing
- Use beginner-friendly language
"""

def ask_huggingface(question):

    response = client.chat.completions.create(

        # model="mistralai/Mistral-7B-Instruct-v0.3",
        # model="HuggingFaceH4/zephyr-7b-beta",
        model="meta-llama/Llama-3.1-8B-Instruct",

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": question
            }
        ],

        max_tokens=500,
        temperature=0.3
    )

    return response.choices[0].message.content

if __name__ == "__main__":

    answer = ask_huggingface(
        "Suggest a SIP strategy for long-term wealth creation."
    )

    print(answer)