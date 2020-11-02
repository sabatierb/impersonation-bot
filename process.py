#Handling the main processing of the tweets

def censorTheBot(sentence):
    #Censoring the output, 
    #If it contains a banned word/phrase the bot with return true
    with open('bannedWords.txt', 'r') as reader:
        for line in reader.readlines():
            if line in sentence:
                return True
    #Only comes here when theres no banned words/phrases
    return False

def censorTheUser(sentence):
    if censorTheBot(sentence):
        return True
    else:
        pass