from twython import Twython
import json

def isInstruction(text):
	return True

twitter = Twython('mnXTJA098hiyNMRjTAzfVvYFp','s7Snej6d34wb56XoJrlkpvzl4JMMUMWxCwePFehfTtHpypnSmD', 
	'2913605392-I09ocdjCPKLBwZhAb3vYVlBVV5Nh5VgFDRBV2d8', 'SJkDce999NDxZLK7dvJVIAAae2BfXEbNZ4z3VXKkTameL')

new_tweets = []
for tweet in twitter.get_home_timeline():
	if (tweet['geo'] and isInstruction(tweet['text'])):
		print tweet['created_at'], tweet['text'], tweet['geo']
		new_tweets.append(tweet)