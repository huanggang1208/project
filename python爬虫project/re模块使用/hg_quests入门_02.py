import requests

url = 'https://fanyi.baidu.com/sug'
s = input('输入你想翻译的关键词：')
kw = {
    'kw': s
}
resp = requests.post(url, data=kw)
print(resp.json())
resp.close()






