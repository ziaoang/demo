# encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf8")

import w2v

a = ["小时", "？", "”", "我爸", "简直", "：", "“", "嗯", "！", "”"]

print(w2v.score(a))

