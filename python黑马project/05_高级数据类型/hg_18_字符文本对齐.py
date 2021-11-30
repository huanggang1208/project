poem = ["静夜思",
        "李白",
        "床前明月光",
        "疑是地上霜",
        "举头望明月",
        "低头思故乡",
        ]

for poem_str in poem:

    # center是居中的使用方法
    # print(poem_str.center(14))
    # ljust是向左靠齐的使用方法
    print("| %s |" % poem_str.ljust(14, "　"))
    # rjust是向右靠齐的使用方法
    # print(poem_str.rjust(14))