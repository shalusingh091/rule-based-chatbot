
import re
from datetime import datetime

def chatbot():
    print("🤖 Chatbot: Hello! I am your AI assistant. Type 'exit' to end chat.\n")
    
    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Chatbot: Goodbye! Have a great day 😊")
            break

        elif re.search(r"\b(hi|hello|hey)\b", user_input):
            print("Chatbot: Hello! How can I help you today?")

        elif re.search(r"your name", user_input):
            print("Chatbot: I am a Rule-Based AI Chatbot created using Python.")

        elif re.search(r"how are you", user_input):
            print("Chatbot: I'm just a bot, but I'm functioning perfectly! 😄")

        elif re.search(r"help", user_input):
            print("Chatbot: I can answer basic questions like greetings, my name, time, and simple queries.")

        elif re.search(r"time", user_input):
            current_time = datetime.now().strftime("%H:%M:%S")
            print("Chatbot: Current time is", current_time)

        else:
            print("Chatbot: Sorry, I don't understand that. Please try something else.")

if __name__ == "__main__":
    chatbot()
