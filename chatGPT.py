import openai
import json

with open('Config.json', 'r' , encoding='utf-8') as f:
    ke = json.load(f)


def main():
    # Définissez votre clé API
    openai.api_key = ke["open_ia"]

    # Initialisez une liste vide pour stocker l'historique de la conversation
    conversation_history = []

    # Ajoutez un pré prompt à l'historique de la conversation
    pre_prompt = "Je suis là pour vous aider à résoudre des équations mathématiques. Quelle est l'équation que vous voulez résoudre ?"
    conversation_history.append({"speaker": "system", "message": pre_prompt})

    # Ajoutez un message utilisateur à l'historique de la conversation
    user_message = "2x + 3 = 7"
    conversation_history.append({"speaker": "user", "message": user_message})

    # Envoyez la requête à l'API ChatGPT
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=pre_prompt + "\n\n" + user_message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
        massage=conversation_history
    )

    # Ajoutez la réponse de l'API à l'historique de la conversation
    chatbot_message = response.choices[0].text
    conversation_history.append({"speaker": "chatbot", "message": chatbot_message})

    # Imprimez la réponse de l'API
    print(chatbot_message)

if __name__ == "__main__":
    main()