# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#import gensim
import jieba
jieba.load_userdict("/var/www/demo/static/files/userdict.txt")

def load_model(filename):
	return None
	#return gensim.models.Word2Vec.load(filename)

def load_cy_dict(filename):
	cy_dict = {}
	for line in open(filename):
		t = line.strip().split('\t')
		cy, cnt = t[0], int(t[1])
		if cnt >= 1000:
			cy_dict[cy] = cnt
	return cy_dict

def loadContext(paragraph, cy_dict, window_size):
	contexts = []
	t = paragraph.strip().split("/ ")
	for i in range(len(t)):
		if t[i] in cy_dict:
			context = [[], [], []] # left, middle, right
			for j in range(-window_size, 0):
				if i+j >= 0:
					context[0].append(t[i+j])
			context[1].append(t[i])
			for j in range(1, window_size+1):
				if i+j < len(t):
					context[2].append(t[i+j])
			contexts.append(context)		
	return contexts

def inner_product(a, b):
	res = 0
	for i in range(len(a)):
		res += a[i] * b[i]
	return res

def rank(neighbor, model, cy_dict):
	context = []
	for w in neighbor:
		if w not in model:
			continue
		if len(context) == 0:
			for i in range(len(model[w])):
				context.append(model[w][i])
		else:
			for i in range(len(model[w])):
				context[i] += model[w][i]
	res = []
	if len(context) == 0: # no context can be used
		for cy in cy_dict:
			res.append([cy, cy_dict[cy]])
	else:
		for cy in cy_dict:
			res.append([cy, inner_product(model[cy], context)])
	res.sort(key=lambda a:a[1], reverse=True)
	return res

def segment(paragraph):
	seg_list = jieba.cut(paragraph.strip().replace(' ', ''))
	paragraph_seg = "/ ".join(seg_list)
	paragraph_seg = paragraph_seg.encode("utf-8")
	return paragraph_seg

def run(paragraph):
	window_size = 5
	cy_dict = load_cy_dict("static/files/all_statistic.txt")
	model = load_model("static/files/all_vector_small_sg.txt")

	res = []
	paragraph_seg = segment(paragraph)
	contexts = loadContext(paragraph_seg, cy_dict, window_size)
	for context in contexts:
		neighbor = context[0] + context[2]
		rank_list = rank(neighbor, model, cy_dict)
		context.append(rank_list[:5])
		res.append(context)
	return res

		
