from pymongo import MongoClient, ASCENDING
import numpy as np
import matplotlib.pyplot as plt
import datetime


client = MongoClient(
    'mongodb+srv://mathchaves:zoom4444@cluster0-wlooi.mongodb.net/test?retryWrites=true&w=majority')

database = client['test']
tweets = database['tweets']

emotions = ["sadness", "joy", "fear", "disgust", "anger"]

avarageEmotions = [0, 0, 0, 0, 0]

tts = [tweet for tweet in tweets.find()]

for l in range(0, 5):
    for p, tweet in enumerate(tts):
        # todos os tweets de um usuário
        tweetsFromUser = [i for i in tweets.find({"author": tweet['author']})]
        # Pra cada tweet, verificar
        date = datetime.datetime.now()
        time = 0
        if(avarageEmotions[l] == 0):
            time = date
        else:
            time = avarageEmotions[l]
        for i, k in enumerate(tweetsFromUser):
            try:
                print(emotions[l])
                if k['emotion']['emotion'] == emotions[l] and k['emotion']['emotion'] != tweetsFromUser[i + 1]['emotion']['emotion']:
                    time += (tweetsFromUser[i + 1]
                             ['createdAt'] - k['createdAt']) / (i + 1)
            except:
                pass
        if(avarageEmotions[l] == 0):
            time = time - date
        time = time / (p + 1)
        avarageEmotions[l] = time

print(avarageEmotions)
print(avarageEmotions[0].total_seconds())
