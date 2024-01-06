#make sure to install --> pip install transformers

from transformers import pipeline

def calculate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return str(e)

def main():
    calculator = pipeline("text2text-generation", model="EleutherAI/gpt-neo-2.7B")

    print("AI Calculator Chatbot: Hello! I'm here to help you with calculations. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("AI Calculator Chatbot: Goodbye! Have a great day.")
            break

        # Use the chatbot model to generate a response
        bot_response = calculator(f"Calculate {user_input}")[0]['generated_text'].replace("Output:", "").strip()

        # Display the result to the user
        print("AI Calculator Chatbot:", bot_response)

        # If the response contains a numeric result, evaluate it
        if any(char.isdigit() for char in bot_response):
            result = calculate_expression(bot_response)
            print("Result:", result)

if __name__ == "__main__":
    main()
