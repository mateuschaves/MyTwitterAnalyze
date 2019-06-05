from pymongo import MongoClient
client = MongoClient(
    'mongodb+srv://mathchaves:zoom4444@cluster0-wlooi.mongodb.net/test?retryWrites=true&w=majority')

database = client['test']
tweets = database['tweets']

# sadness, joy, fear, disgust, anger
emotionsCounterDataSet = [0, 0, 0, 0, 0]

for tweet in tweets.find():
    try:
        emotion = tweet['emotion']['emotion']
        if emotion == 'sadness':
            emotionsCounterDataSet[0] += 1
        elif emotion == 'joy':
            emotionsCounterDataSet[1] += 1
        elif emotion == 'fear':
            emotionsCounterDataSet[2] += 1
        elif emotion == 'disgust':
            emotionsCounterDataSet[3] += 1
        elif emotion == 'anger':
            emotionsCounterDataSet[4] += 1

    except KeyError as identifier:
        pass

print(emotionsCounterDataSet)
