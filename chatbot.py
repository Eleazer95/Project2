from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

my_bot = ChatBot(
    name="ETxBot",
    read_only=True,
    logic_adapters=["chatterbot.logic.MathematicalEvaluation", "chatterbot.logic.BestMatch"]
)

small_talk = [
    "how old are you",
    "I am a months old",
    "what's your age?",
    "I am a couple of months old",
    "hi there",
    "hi",
    "how are you?",
    "I'm good you?",
    "How is the weather today?",
    "I really can't tell, It depends on your location and time zone.",
    "When were you created?",
    "I was created on November 16th, in the year 2020.",
    "What programming laguage was used to create you?",
    "Python programming language was used for my creation",
    "What questions can you answer?",
    "I can answer as many answers I was programmed to answer",
    "are you friendly",
    "Yes I am",
    "Crack me up will you?",
    "Why is 6 afraid of 7? because 7 ate 9",
    "Crack me up will you?",
    "you look like my chinese friend 'ugh lee'",
    "how do you do?",
    "i'm cool.",
    "fine, you?",
    "always cool",
    "i'm okay",
    "glad to hear that",
    "i'm fine",
    "glad to hear that",
    "i feel awesome",
    "excellent, glad to hear that."
    "not so good",
    "sorry to hear that",
    "what's your name?",
    "I'm ETxBot. ask me a math problem please.",
    "who created you?",
    "I was created by Eleazer Ayuk, a Software Engineer",
    "who made you?",
    "I was made by Eleazer Ayuk, a Software Engineer",
    "I feel great",
    "I also feel great too.",
    
]

math_talk_1 = [
    "pythagorean theorem",
    "a squared plus b squared equals c squared"
]

math_talk_2 = [
    "law of cosines",
    "c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)"
]

list_trainer = ListTrainer(my_bot)

for item in (small_talk, math_talk_1, math_talk_2):
    list_trainer.train(item)


corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train("chatterbot.corpus.english")

while True:
    try:
        bot_input = input("You: ")
        bot_response = my_bot.get_response(bot_input)
        print(f"{my_bot.name}: {bot_response}")
    except:(KeyboardInterrupt, EOFError, SystemExit)
    
