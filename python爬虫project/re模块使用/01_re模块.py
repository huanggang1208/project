import re

# findall:匹配字符串中所有符合正则的内容
lst = re.findall(r"\d+", "我的电话号码是1234245")
print(lst)

# finditer：匹配字符串所有内容【返回的是迭代器】,从迭代器中拿到的内容需要.group()
it = re.finditer(r"\d+", "我的电话号码是1234245")
print(it)
for i in it:
    print(i.group())

# search返回的结果是match对象，拿数据需要.group(),只能匹配到第一个数字类型
s = re.search(r"\d+", "我的电话号码是1234245,工作手机上229")
print(s.group())

# match是从头开始匹配
r = re.match(r"\d+", "我的电话号码是1234245,wod司法339")
print(r)

# 预加载正则表达式
obj = re.compile(r"\d+")
ret = obj.finditer("我的电话号码是1234245,工作手机上229")
for i in ret:
    print(i.group())

# （？P<分组名字>正则)能单独从正则匹配的内容中进一步提取内容
s = """<title>周杰伦</title><dic>稻花香<dic><span id= '1'>\
    <title>林俊杰</title><dic>背对背拥抱<dic><span id= '2'>" \
    <title>陈奕迅</title><dic>十年<dic><span id= '3'>"""
# re.S 让.能匹配换行符
obj2 = re.compile(r"<title>(?P<name>.*?)</title><dic>(?P<代表作>.*?)<dic><span id= '(?P<id>\d+)'>", re.S)
result = obj2.finditer(s)
for i in result:
    print(i.group("name", "代表作", "id"))