def chatbot_response(user_input):
    user_input = user_input.lower()   # Convert to lowercase for matching
    
    if user_input == "hello" or user_input == "hi":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks! How about you?"
    elif user_input == "fine":
        return "Have a good day"
    elif user_input == "bye":
        return "Goodbye! Have a nice day"
    else:
        return "Sorry, I don't understand that."

# Main program
print("Chatbot: Hello! Type 'bye' to end the chat.")
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Chatbot:", response)
    
    if user_input.lower() == "bye":
        break
