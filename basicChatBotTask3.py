import nltk
from nltk.chat.util import Chat, reflections
from datetime import datetime

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

class ImprovedChatbot(Chat):
    def __init__(self, pairs, reflections={}):
        super().__init__(pairs, reflections)
        self.context = None

    def respond(self, input_text):
        response = super().respond(input_text)
        if self.context:
            response = f"{self.context} {response}"
            self.context = None
        return response

    def set_context(self, context):
        self.context = context

def get_time_of_day():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning! "
    elif 12 <= current_hour < 18:
        return "Good afternoon! "
    else:
        return "Good evening! "

patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am good, thank you!', 'I am doing well. How about you?']),
    (r'what is your name', ['I am a chatbot. You can call me ChatGPT.', 'I don\'t have a name. You can just call me Chatbot.']),
    (r'your age|how old are you', ['I don\'t have an age. I am a computer program.']),
    (r'bye|goodbye|ok bye', ['Goodbye!', 'Have a great day!', 'See you later.']),
    (r'see you', ['Goodbye!', 'Have a nice day!', 'Take care!']),
    (r'(.*)', ['That\'s interesting!', 'Tell me more...', 'I am not sure I understand.']),
]

# Create an improved chatbot using the defined patterns
chatbot = ImprovedChatbot(patterns, reflections)

# Begin the chat
print("Hello! I'm a simple chatbot.")
print("You can start a conversation with me or type 'bye' to exit.")
print("Feel free to ask about my name, age, or just chat with me!")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye! Have a great day.")
        break
    else:
        # Set context based on user input
        if 'time' in user_input:
            chatbot.set_context(get_time_of_day())
        
        # Get response from the chatbot
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
