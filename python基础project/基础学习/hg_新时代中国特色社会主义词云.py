# GovRptWordCloudv1.py
import jieba
import wordcloud

f = open("E://pycharm/project/文档TXT/新时代中国特色社会主义.txt", "r", encoding="utf-8")
exclude = {"的", "是", "和", "我们"}
t = f.read()
f.close()
ls = jieba.lcut(t)

txt = " ".join(ls)
w = wordcloud.WordCloud(width=1000, height=700, background_color="white",
                        font_path="msyh.ttc", stopwords=exclude)
w.generate(txt)
w.to_file("新中特词云.png")
