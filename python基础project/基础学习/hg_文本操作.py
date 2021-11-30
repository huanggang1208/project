# hamlet单词出现频次
def getText():
    txt = open("E://pycharm/project/文档TXT/Hamlet.txt", "r", ).read()
    # 将文档所有字母转化为小写
    txt = txt.lower()
    # 利用遍历循环将所有标点符号转化为空格
    for ch in '!@#$%^&*+_-,./?[]{};\\|~`:=':
        txt = txt.replace(ch, " ")
    return txt


hamletTxt = getText()
# 用以空格为空格符将所有单词划分为字符串列表
words = hamletTxt.split()
# 用字典类型统计单词出现的次数
counts = {}  # 定义一个空字典
for word in words:  # 遍历TXT中所有单词
    # .get:当字典中有其中一个单词则+1，没有这个单词则添加这个单词值为0再+1
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
# 将所有出现过的单词排序，reverse=true表示从大到小排列
items.sort(key=lambda x: x[1], reverse=True)

# 遍历统计前十出现的单词和出现次数
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))


