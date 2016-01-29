# encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf8")

import api

paragraph = "有一天晚上放学回来，我发现桌上摆着许多好吃的菜，那气氛好像是在等什么重要的客人。我急忙去问妈妈，妈妈说：“在等你奶奶。”正说着，奶奶骑着三轮车回来了。爸爸连忙迎上去，把奶奶的三轮车接了过来，妈妈也打来了一盆热水，让奶奶洗脸，然后把她扶到饭桌前坐下。这时，我从妈妈的口中得知，奶奶辛辛苦苦卖牙刷挣的钱都捐给了一位山区的失学儿童。那位失学儿童在重返校园的第一天，就给我们家寄来了一封感谢信，她在信中说，要以最好的成绩来报答我的奶奶。爸爸、妈妈准备这桌丰盛的晚餐，就是给奶奶“庆功”的！"

res_list = api.run(paragraph)

for res in res_list:
	print('-'*20)
	for v in res[0]:
		print(v)
	print('-'*20)
	print(res[1][0])
	print('-'*20)
	for v in res[2]:
		print(v)
	print('-'*20)
	for v in res[3]:
		print("%s\t%.4f"%(v[0], v[1]))
	
