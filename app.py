
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    exit("Chave de API não configurada. Saindo...")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.0-flash')
chat = model.start_chat(history=[])

print("Bem-vindo ao Chatbot!")
print("Digite suas mensagens. Digite 'sair' para encerrar.")

while True:
    user_input = input("Você: ")

    if user_input.lower() == 'sair':
        print("Até logo!")
        break

    try:
        response = chat.send_message(user_input)
        print(f"Chatbot: {response.text}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        print("Por favor, tente novamente.")
        