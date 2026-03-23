from openai_example import query_openai
from groq_example import query_groq
from huggingface_example import query_huggingface
from gemini_example import query_gemini
from cohere_example import query_cohere
def main():
    print("Choose API:")
    print("1. OpenAI")
    print("2. Groq")
    print("3. Hugging Face")
    print("4. Gemini")
    print("5. Cohere")
    choice = input("Enter choice: ")
    prompt = input("Enter your prompt: ")
    if choice == "1":
        print(query_openai(prompt))
    elif choice == "2":
        print(query_groq(prompt))
    elif choice == "3":
        print(query_huggingface(prompt))
    elif choice == "4":
        print(query_gemini(prompt))
    elif choice == "5":
        print(query_cohere(prompt))
    else:
        print("Invalid choice")
if __name__ == "__main__":
    main()