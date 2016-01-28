# encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf8")

from flask import *
import jieba
#jieba.load_userdict("static/files/userdict.txt")

#import w2v

app = Flask(__name__)
app.secret_key = 'GHS^&UHUY&TGY'

POOL = []
for line in open("/var/www/demo/static/files/all_statistic.txt"):
	t = line.strip().split('\t')
	cy, cnt = t[0], int(t[1])
	if cnt >= 1000:
		POOL.append(cy)


def myRender(html):
	return render_template('head.html') + html + render_template('foot.html')

@app.route('/', methods=["GET", "POST"])
def index():
	if request.method == "POST":
		sentence = request.form["sentence"]
		seg_list = jieba.cut(sentence.strip().replace(' ', ''))
		result = "/ ".join(seg_list)
		words = result.split("/ ")
		cylist = []
		for i in range(len(words)):
			if words[i] in POOL:
				context = []
				neighbor = [[], [], []]
				neighbor[1].append(words[i])
				for j in [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]:
					if i+j >= 0 and i+j < len(words):
						context.append(words[i+j])
						if j < 0:
							neighbor[0].append(words[i+j])
						else:
							neighbor[2].append(words[i+j])
				#neighbor.append(w2v.score(context))
				neighbor.append([])
				cylist.append(neighbor)
		return myRender(render_template("index.html", raw=sentence, res=result, cylist=cylist))
	return myRender(render_template("index.html"))

if __name__ == '__main__':
	app.run(debug=True)
