from chatterbot import ChatBot
bot = ChatBot(
    'Nihir',  
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'],
)
from chatterbot.trainers import ChatterBotCorpusTrainer
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')
name=input("Enter Your Name: ")
print("Hi "+name+", how can I help you?")
while True:
    request=input(name+':')
    if request=='Bye' or request =='bye':
        print('Nihir: Bye')
        break
    else:
        response=bot.get_response(request)
        # get_reponses() is a method of chatbot instance
        print('Nihir:',response)

#Output
"""


Enter Your Name: Sam
Hi Sam, how can I help you?
Sam:Tell me some history
Nihir: history has two broad interpretations, depending on whether you accept the role of individuals as important or not.
Sam:What is a computer
Nihir: A computer is an electronic device which takes information in digital form and performs a series of operations based on predetermined instructions to give some output.
Sam:Tell me a joke
Nihir: Did you hear the one about the mountain goats in the andes? It was "ba a a a a a d".
Sam:Can you feel?
Nihir: Maybe I can. I am a fairly sophisticated piece of software.
Sam:bye
Nihir: Bye

"""

