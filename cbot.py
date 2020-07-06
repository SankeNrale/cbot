from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

cbot = ChatBot('cbot')

corpus_trainer = ChatterBotCorpusTrainer(cbot)
list_trainer = ListTrainer(cbot)

corpus_trainer.train('chatterbot.corpus.english')


print('Type Something to Begin...')
while True:
	try:
		user_input = input()
		bot_response = cbot.get_response(user_input)
		print(bot_response)
	except (KeyboardInterrupt, EOFError, SystemExit):
		break
