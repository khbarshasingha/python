import requests

def wordrhym(word):
	paradic={}
	paradic["rel_rhy"]=word
	paradic["max"]=3
	baseurl="https://api.datamuse.com/words"
	res=requests.get(baseurl,params=paradic)
	word_ds=res.json()
	return [d['word'] for d in word_ds]

print(wordrhym("funny"))