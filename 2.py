import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses using pairs (patterns and responses)
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm just a bot, but I'm doing fine!", "I'm good, how about you?"]),
    (r"what is your name?", ["I'm a chatbot!", "You can call me ChatBot."]),
    (r"bye|goodbye|byy|by", ["Goodbye!", "See you later!", "Bye! Have a great day!"]),
    (r"(.*)", ["I'm not sure how to respond to that.", "Can you ask something else?", "Interesting! Tell me more."]),
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Start conversation
print("ChatBot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("ChatBot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("ChatBot:", response)
