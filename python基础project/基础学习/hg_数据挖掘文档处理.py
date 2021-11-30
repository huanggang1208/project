import pandas as pd
teenager_sns = pd.read_csv("E:/pycharm/project/文档TXT/teenager_sns.csv")
teenager = teenager_sns["age"].sort_values()
answer1 = teenager.head()
print(answer1)
answer2 = teenager.tail()
print(answer2)
