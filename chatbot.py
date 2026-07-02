#the well structrued hashmap instead of if-else blocks
responses = {
    "hello": "Hi there! Welcome to Sidhdhant's chatbot. How can I assist you today?",
    "hi": "Hey! Are you ready to build some cool stuffs?",
    "what is your purpose": "I am a ruled based chatbot for predefined inputs.(Type 'help' for other predefined inputs)",
    "who created you": "I was designed by an AI Engineer Sidhdhant!",
    "help": "You can ask me about my purpose, who created me, or type 'exit' to turn me off.",
    "status": "Logic engine is working with a safe fallback."
}

def run_chatbot():
    print("🤖 Bot: Hello my self Sidhu . How can i help you?\n")
    #the main infinte working loop
    while True:
        #Input
        raw_input = input("You: ")
        clean_input = raw_input.lower().strip() # Normalise
        
        #Exit
        if clean_input == 'exit':
            print("🤖 Bot:Goodbye! See you again later.")
            break
            
        #Output
        reply = responses.get(clean_input, "🤖 Bot: I do not understand.")  #here we use .get() method for safety
        
        print(f"{reply}\n")


if __name__ == "__main__":
    run_chatbot()