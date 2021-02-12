import os
import random

import json
import yfinance as yf
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

def get_good_sentence():
	f = open('1.txt','r')
	x = f.readlines()
	random.shuffle(x)
	return x[1]

def get_bad_sentence():
	f = open('2.txt','r')
	x = f.readlines()
	random.shuffle(x)
	return x[1]

def do_task(s, key, log, reference_keywords):
	try:
		if key == "command":
			s = s[-1]
			f = open('open.txt','r')
			x = f.readlines()
			f.close()
			for i in x:
				if i.split('--__')[0] == s:
					log.text += get_good_sentence() + "\n"
					os.system(i.split('--__')[1])
					return

		if key == "mean":
			f = json.load(open('data.json'))
			print(f[s[-1]])
			log.text += "The meaning of " + str(s[-1]) + " is - " + f[s[-1]][0] + "\n"
			return

		if key == "stock":
			d = {'apple':'AAPL', 'googl':'GOOG', 'microsoft':'MSFT', 'amazon':'AMZN', 'gamestop':'GME'}
			if s[-1] in d.keys():
				stock = d[s[-1]]
			else:
				stock = s[-1]
			tick = yf.Ticker(stock)
			df = tick.history(period = str(1) + 'd')
			log.text += 'Most Recent close value of ' + s[-1] + " is at " + str(round(df.loc[:,'Close'][0],2)) + "\n"
			return

		if key == "googl":
			query_builder = ""
			query_builder+=s[-1]
			s = s[:-1]
			while s[-1] not in reference_keywords:
				query_builder = s[-1]+"%20" + query_builder
				s = s[:-1]
			os.system("xdg-open http://google.com/search?q="+query_builder)

	except Exception as ex:
		log.text += "I'm sorry I looked for it, but can't find it.\n"
		print(ex)

def get_score(list1, list2):
	score = 0
	for i in list1:
		if i in list2:
			score += 1
	return score

def get_suitable(s):
	s = s.lower()
	stop_words = set(stopwords.words('english'))
	stop_words.remove("about")
	word_tokens = word_tokenize(s)
	filtered_sentence = [w for w in word_tokens if not w in stop_words]
	filtered_sentence = []
	stemmer = PorterStemmer()
	for w in word_tokens:
	    if w not in stop_words:
	        filtered_sentence.append(stemmer.stem(w))
	return filtered_sentence

def command(s, log):
	keywords = get_suitable(s)

	reference_keywords = [
	["kernel", "bash", "console", "launch", "open", "start", "run", "command"],
	["synonym", "word", "mean"],
	["company", "market", "share", "value", "stock"],
	["search", "about", "know", "what", "find", "googl"]
	]

	for i in range(len(reference_keywords)):
		reference_keywords[i] = [get_score(keywords, reference_keywords[i])] + reference_keywords[i]
	reference_keywords = sorted(reference_keywords, key = lambda x : x[0], reverse = True)
	print(keywords)
	if reference_keywords[0][0] > 0:
		do_task(keywords, reference_keywords[0][-1], log, reference_keywords[0])
	else:
		f = open('2.txt','r')
		x=f.readlines()
		random.shuffle(x)
		log.text += x[1]
		return
