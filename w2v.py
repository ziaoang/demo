# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import gensim

def loadModel():
	return gensim.models.Word2Vec.load("/var/www/demo/static/files/all_vector_small_sg.txt")

def loadPOOL():
	POOL = {}
	for line in open("statistic/all.txt"):
		t = line.strip().split('\t')
		cy, cnt = t[0], int(t[1])
		if cnt >= 1000:
			POOL[cy] = cnt
	return POOL

def inner_product(a, b):
	res = 0
	for i in range(len(a)):
		res += a[i] * b[i]
	return res

def score(neighbor):
	POOL = loadPool()
	MODEL = loadModel()
	context = []
	for w in neighbor:
		if w not in MODEL:
			continue
		if len(context) == 0:
			for i in range(len(MODEL[w])):
				context.append(MODEL[w][i])
		else:
			for i in range(len(MODEL[w])):
				context[i] += MODEL[w][i]
	res = []
	for cy in POOL:
		res.append([cy, inner_product(MODEL[cy], context)])
	res.sort(key=lambda a:a[1], reverse=True)
	return res[:10]
