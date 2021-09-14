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



