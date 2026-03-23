import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HUGGINGFACE_API_KEY"),
)
def query_huggingface(prompt):
    try:
        response = client.chat.completions.create(
            model="katanemo/Arch-Router-1.5B:hf-inference",
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"
if __name__ == "__main__":
    user_input = input("Enter your prompt: ")
    print("Response:")
    print(query_huggingface(user_input))