import requests

# 原URL过长https://movie.douban.com
# /j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=1
url = 'https://movie.douban.com/j/chart/top_list'
which = input("你想看的页数（20的倍数）：")
# 重新封装参数
pram = {'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': which,  # 翻页的参数
        'limit': 20}
header = {'user-agent': 'Mozilla/5.0'}
resp = requests.get(url=url, headers=header, params=pram)
print(resp.json())
resp.close()  # 关掉resp
