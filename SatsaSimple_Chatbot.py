class ChatBot:
    def __init__(self):
        self.questions = [
            "What's your name?",
            "How old are you?",
            "Where are you from?",
            "What's your favorite programming language?",
            "What's your favorite hobby?",
            "What's your favorite book?",
            "What's your favorite movie?",
            "What's your dream job?"
        ]

    def start_chat(self):
        print("Hello! I'm your friendly chatbot. Let's get to know each other.")
        for question in self.questions:
            response = input(question + " ")
            print("Interesting! You said: " + response)
        print("It was nice chatting with you!")

# Create a chatbot instance and start the chat
bot = ChatBot()
bot.start_chat()