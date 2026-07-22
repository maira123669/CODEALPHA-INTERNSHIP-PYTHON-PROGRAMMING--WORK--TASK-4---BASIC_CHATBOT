def get_bot_response(user_input):
    # Normalize input to lowercase for better matching
    user_input = user_input.lower().strip()

    # Predefined rules/replies
    if "hello" in user_input or "hi" in user_input:
        return "Hi! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a Python script, but I'm running perfectly! Thanks for asking."
    elif "your name" in user_input:
        return "I am AlphaBot, your friendly neighborhood rule-based assistant."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a fantastic day!"
    else:
        return "Hmm, I don't quite understand that. Could you try asking something else?"

def start_chatbot():
    print("--- AlphaBot Rules Chatbot ---")
    print("Type your message below. Type 'bye' to exit the chat.")
    print("------------------------------------------------")

    while True:
        user_message = input("\nYou: ")
        
        # Stop condition
        if user_message.lower().strip() == 'bye':
            print(f"Bot: {get_bot_response(user_message)}")
            break
            
        # Get and print bot response
        response = get_bot_response(user_message)
        print(f"Bot: {response}")

if __name__ == "__main__":
    start_chatbot()