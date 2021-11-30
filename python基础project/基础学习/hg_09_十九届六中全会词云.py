# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_09_十九届六中全会词云.py

import jieba
import wordcloud

f = open("E://pycharm/project/文档TXT/十九届六中全会.txt", "r", encoding="utf-8")
exclude = {"的", "是", "和", "我们"}
t = f.read()
f.close()
ls = jieba.lcut(t)

txt = " ".join(ls)
w = wordcloud.WordCloud(width=1000, height=700, background_color="white",
                        font_path="msyh.ttc", stopwords=exclude)
w.generate(txt)
w.to_file("十九届六中全会.png")
