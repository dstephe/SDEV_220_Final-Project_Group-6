from chatterbot import ChatBot

bot = ChatBot(
    'Bell',#chatbot name
    storage_adaptor='',#what database system we are using
    #how it determines what to reponse with
    logic_adaptors=[ 
        'chatterbot.logic.SpecificResponseAdapter',#repsonses to specifc questiosn with specfic answers
        'chatterbot.logic.MathematicalEvaluation',#responses to math questions
        'chatterbot.logic.BestMatch'#matches the input with the best output
    ],
    database_url=''#location of database
)

#while loop to run bot
while True:
    try:
        bot_input = bot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break

#training template
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

trainer.train([
    '',
])