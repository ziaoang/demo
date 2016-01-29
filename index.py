# encoding=utf-8

import gensim

import sys
reload(sys)
sys.setdefaultencoding("utf8")

from flask import *
#import api

app = Flask(__name__)
app.secret_key = 'GHS^&UHUY&TGY'

def myRender(html):
	return render_template('head.html') + html + render_template('foot.html')

@app.route('/', methods=["GET", "POST"])
def index():
	if request.method == "POST":
		sentence_raw = request.form["sentence"]
		sentence_seg = None
		#sentence_seg = api.segment(sentence_raw)
		contexts = None
		#contexts = api.run(sentence_raw)
		return myRender(render_template("index.html", raw=sentence_raw, seg=sentence_seg, contexts=contexts))
	return myRender(render_template("index.html"))

if __name__ == '__main__':
	app.run(debug=True)
